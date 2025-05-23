# 🔮 Lotofácil Predictor — IA preditiva de jogos com Streamlit + Machine Learning

![Badge](https://img.shields.io/badge/status-ativo-green) ![Badge](https://img.shields.io/badge/projeto-na%20ra%C3%A7a-blue)

**Projeto criado por [Diego Oliveira](https://github.com/seu-usuario) com suporte do ChatGPT, voltado para gerar jogos inteligentes da Lotofácil, com base em análise de dados, IA e interface web interativa.**

---

## 🧠 O que esse projeto faz?

- Simula concursos da Lotofácil com base estatística
- Treina um modelo de Random Forest para prever dezenas com maior probabilidade
- Gera jogos automaticamente com 15 dezenas
- Salva cada jogo no banco SQLite (`jogos.db`)
- Permite consulta ao histórico via terminal ou web
- Exporta os jogos para `.csv`
- Interface amigável com Streamlit
- 100% rodando na nuvem

---

## 🧱 Estrutura do Projeto

lotofacil-predictor/
├── app.py # Interface web com Streamlit
├── scripts/
│ ├── gerar_jogos.py # Modelo preditivo, salvamento em banco e .txt
│ └── consultar_jogos.py # Consulta via terminal
├── resultados/ # Jogos gerados (.txt) e banco de dados (.db)
├── requirements.txt # Pacotes necessários para rodar o projeto
├── README.md # Você está aqui

---

## 🧪 Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- SQLite
- pandas
- numpy
- scikit-learn

---

## 🚀 Como rodar localmente (em Codespaces ou VS Code)

# Clone o repositório
git clone https://github.com/seu-usuario/lotofacil-predictor
cd lotofacil-predictor

# Instale as dependências
pip install -r requirements.txt

# Rode a interface
streamlit run app.py

## 🌐 Como testar online (via Streamlit Cloud)

Suba o projeto no seu GitHub
- Vá em https://share.streamlit.io
- Clique em “New App”
- Escolha o repositório e defina app.py como arquivo principal
- Clique em Deploy e pronto!

## 📥 Exportação de dados

Todos os jogos são salvos em resultados/jogos.db
Você pode exportar todos para .csv com um botão na interface
Os .txt com cada jogo também ficam salvos na pasta resultados/

## 📌 Próximos passos

- Integrar dados reais da Caixa (concursos oficiais)
- Criar simulador de acertos com base no histórico
- Implementar análise de frequência e calor dos números
- Criar botão de múltiplos jogos
- Versão mobile e painel de bolões

## 🛠️ Feito na cara e na coragem
Esse projeto foi construído no braço com apoio da IA, mas com entendimento linha por linha de cada funcionalidade. É um exemplo claro de como aprender tecnologia aplicando algo real, útil e com potencial de monetização.

# 📄 Licença
MIT — Livre para estudar, adaptar e melhorar. Mas se for usar pra vender, lembra de dar os créditos. 😉

Diego Oliveira | 2025


