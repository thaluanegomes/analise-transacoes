# Analisador de Transações Suspeitas

Este projeto foi feito em Python com o objetivo de simular a análise de transações financeiras e detectar possíveis comportamentos suspeitos, com base em regras simples.

---

## 📂 Funcionalidades

- Leitura de dados simulados de transações em `.csv`
- Identificação de transações suspeitas por:
  - Valor alto (acima de R$ 3.000)
  - Transações do mesmo cliente em cidades diferentes no mesmo dia
- Geração automática de relatório `.csv`

---

## 🧪 Tecnologias usadas

- Python 3
- Biblioteca Pandas

---

## 📁 Estrutura do Projeto
  analise-transacoes/
├── dados/ # Contém o arquivo de transações simuladas (transacoes.csv)
├── src/ # Script principal (analise.py)
├── output/ # Relatório gerado com os dados suspeitos
├── README.md # Explicação do projeto
├── requirements.txt # Lista de bibliotecas instaladas

---

## ▶️ Como executar o projeto

1. No terminal, vá até a pasta do projeto:
cd ~/Documents/analise-transacoes
2. Crie e ative o ambiente virtual:
python3 -m venv venv
source venv/bin/activate  
3. Instale as dependências:
pip install pandas
4. Rode o Projeto: 
python3 src/analise.py
5. O relatório será salvo automaticamente em:
/output/relatorio_fraudes.csv
