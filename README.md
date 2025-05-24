# 🎯 Lotofácil Predictor — IA preditiva de jogos com Streamlit + Machine Learning

<p align="center">
  <img src="pasta_logo/logo.JPG" width="250" alt="Logo Lotofácil Predictor" />
</p>


# 🔮 Lotofácil Predictor — IA preditiva de jogos com Streamlit + Machine Learning

![Badge](https://img.shields.io/badge/status-ativo-green) ![Badge](https://img.shields.io/badge/projeto-na%20ra%C3%A7a-blue)

Projeto criado por **Diego de Jesus Oliveira** com apoio do ChatGPT.  
Gera jogos inteligentes da Lotofácil com base em dados históricos, machine learning e interface interativa na web.

---

## 🧠 O que esse projeto faz

- Simula concursos da Lotofácil com base estatística
- Treina modelo Random Forest para prever dezenas mais prováveis
- Gera jogos automaticamente com 15 dezenas
- Salva no banco SQLite (`jogos.db`)
- Permite consulta ao histórico (web e terminal)
- Exporta jogos para `.csv`
- Interface via **Streamlit**
- 100% rodando na nuvem

---

## 🧱 Estrutura do Projeto

lotofacil-predictor/
├── app.py # Interface web com Streamlit
├── scripts/
│ ├── gerar_jogos.py # Modelo preditivo + salvamento
│ └── consultar_jogos.py # Consulta via terminal
├── resultados/ # Jogos salvos (.txt) + banco (.db)
├── requirements.txt # Dependências
└── README.md # Você está aqui


---

## 🧪 Tecnologias Utilizadas

- Python 3.10+  
- Streamlit  
- pandas + numpy  
- SQLite  
- scikit-learn

---

## 🚀 Como rodar localmente

```
bash
git clone https://github.com/diego-jesus/lotofacil-predictor
cd lotofacil-predictor

pip install -r requirements.txt
streamlit run app.py
```

---

🌐 Testar online (Streamlit Cloud)

- Suba o projeto no GitHub
- Vá em share.streamlit.io
- Clique em New App
- Escolha o repositório e defina app.py como principal
- Clique em Deploy e pronto!

---

📥 Exportação de dados

- Jogos salvos em resultados/jogos.db
- Exportação via botão na interface (.csv)
- Cópia dos jogos em .txt dentro de resultados/

---

📌 Próximos passos

- Integrar dados reais da Caixa (concursos oficiais)
- Simulador de acertos com base no histórico
- Análise de frequência e calor dos números
- Gerar múltiplos jogos por rodada
- Versão mobile + painel de bolões

---

🛠️ Feito na coragem + dados

Esse projeto foi construído no braço, com apoio da IA e entendimento de cada linha de código.
Um exemplo de como aprender tecnologia aplicando algo real, útil e com potencial de monetização.

---

👨‍💻 Sobre mim
Sou Diego de Jesus Oliveira, analista de prevenção a fraudes em transição para dados.
Uso projetos como este para explorar, aprender e gerar valor real com dados, IA e curiosidade.

[Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/diego-jesus-317302178/)
