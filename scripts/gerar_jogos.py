# lotofacil_predictor - Projeto Preditivo de Jogos

# Estrutura base para modelagem, simulação e sugestão de jogos para Lotofácil
# Autor: Diego Oliveira + ChatGPT

import random
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
import sqlite3
import os

# ==============================
# Banco de dados SQLite para armazenar jogos

def salvar_no_banco(dezenas):
    conn = sqlite3.connect("resultados/jogos.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            dezenas TEXT
        )
    """)

    agora = datetime.now().strftime("%Y-%m-%d %H:%M")
    dezenas_str = ",".join(str(d) for d in dezenas)

    cursor.execute("INSERT INTO jogos (data_hora, dezenas) VALUES (?, ?)", (agora, dezenas_str))
    conn.commit()
    conn.close()

# ==============================
# Simulador de concursos aleatórios para testes

def simular_concursos(n=1000):
    concursos = [sorted(random.sample(range(1, 26), 15)) for _ in range(n)]
    return concursos

# Transformar concursos em dataframe binário para treino

def concursos_para_df(concursos):
    df = pd.DataFrame(0, index=range(len(concursos)), columns=[f"{i:02d}" for i in range(1, 26)])
    for idx, sorteio in enumerate(concursos):
        for num in sorteio:
            df.at[idx, f"{num:02d}"] = 1
    return df

# Treinar modelo para prever próximo jogo

def treinar_modelo(df):
    X = df[:-1]
    y = df.shift(-1).dropna().astype(int)
    modelos = {}
    for coluna in df.columns:
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X, y[coluna])
        modelos[coluna] = clf
    return modelos

# Gerar sugestão de jogo com base na previsão de probabilidades

def prever_jogo(modelos, ultima_linha):
    probs = []
    for col, modelo in modelos.items():
        prob = modelo.predict_proba([ultima_linha])[0][1]
        probs.append((col, prob))
    top_15 = sorted(probs, key=lambda x: x[1], reverse=True)[:15]
    return sorted([int(num) for num, _ in top_15])

# ==============================
# Execução principal
if __name__ == "__main__":
    concursos = simular_concursos(1000)
    df = concursos_para_df(concursos)
    modelos = treinar_modelo(df)
    sugestao = prever_jogo(modelos, df.iloc[-1])

    print("Sugestão de jogo preditivo:", sugestao)

    # Salvar em arquivo com data/hora
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nome_arquivo = f"resultados/jogo_{agora}.txt"
    with open(nome_arquivo, "w") as f:
        f.write(" ".join(str(n) for n in sugestao))

    # Salvar no banco de dados
    salvar_no_banco(sugestao)
