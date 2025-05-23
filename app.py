import streamlit as st
import sqlite3
import pandas as pd
from scripts.gerar_jogos import simular_concursos, concursos_para_df, treinar_modelo, prever_jogo, salvar_no_banco

st.set_page_config(page_title="Lotofácil Predictor", layout="centered")
st.title("🔮 Lotofácil Predictor")

# Conectar banco
def carregar_jogos():
    conn = sqlite3.connect("resultados/jogos.db")
    df = pd.read_sql_query("SELECT * FROM jogos ORDER BY id DESC", conn)
    conn.close()
    return df

st.markdown("---")

# Botão para gerar novo jogo
if st.button("🎲 Gerar novo jogo preditivo"):
    concursos = simular_concursos(1000)
    df = concursos_para_df(concursos)
    modelos = treinar_modelo(df)
    sugestao = prever_jogo(modelos, df.iloc[-1])
    salvar_no_banco(sugestao)
    st.success(f"Jogo gerado com sucesso: {', '.join(map(str, sugestao))}")

# Exibir últimos jogos
st.markdown("## Últimos jogos")
if st.button("📄 Ver últimos jogos cadastrados"):
    dados = carregar_jogos()
    if not dados.empty:
        st.dataframe(dados)
    else:
        st.info("Nenhum jogo encontrado no banco.")

# Exportar CSV
st.markdown("## Exportar Histórico")
if st.button("📥 Baixar jogos em CSV"):
    df_csv = carregar_jogos()
    csv = df_csv.to_csv(index=False).encode('utf-8')
    st.download_button("Clique para baixar", csv, "jogos_lotofacil.csv", "text/csv")

st.markdown("---")
st.caption("Feito por Diego Oliveira + ChatGPT ❤️")
