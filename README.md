# 📊 Análise de Vendas de uma Loja (Python puro)

Relatório de vendas de uma loja de roupas, calçados e acessórios, desenvolvido **apenas com Python puro**: listas, dicionários, laços de repetição e estruturas condicionais, sem bibliotecas externas.

Este é o **primeiro projeto do meu portfólio com foco em análise de dados**. O objetivo foi praticar a lógica por trás de operações que depois aparecem em ferramentas como SQL, pandas e Excel (`SUM`, `AVG`, `GROUP BY`, `MAX/MIN` e `CASE WHEN`).

---

## O que o programa faz

| # | Funcionalidade | Como foi resolvida |
|---|---|---|
| 1 | Faturamento total | acumulador com `for` (preço × quantidade) |
| 2 | Ticket médio | faturamento total ÷ número de vendas |
| 3 | Produto mais vendido (em quantidade) | comparação com valor de referência |
| 4 | Faturamento por categoria | dicionário que agrupa e soma por chave |
| 5 | Maior e menor venda | comparação com o primeiro item da lista |
| 6 | Classificação de cada venda | `if / elif / else` |
| 7 | Relatório formatado no terminal | f-strings com alinhamento e casas decimais |

**Regra de classificação das vendas:**

- **Alta:** valor acima de R$ 300
- **Média:** valor entre R$ 100 e R$ 300
- **Baixa:** valor abaixo de R$ 100

---

## Conceitos utilizados

- Listas e dicionários (inclusive uma lista de dicionários)
- Laços `for`
- Condicionais `if / elif / else`
- Acumuladores e contadores
- Agrupamento de dados com dicionário
- Formatação de texto com f-strings

---

## Como executar

**Pré-requisito:** ter o [Python 3](https://www.python.org/downloads/) instalado. Não é necessário instalar nenhuma biblioteca.

```bash
# 1. Clone o repositório
git clone https://github.com/clararibz/projeto-analise-vendas-python.git

# 2. Entre na pasta
cd projeto-analise-vendas-python

# 3. Execute o programa
python main.py
```

> No Mac/Linux, se o comando `python` não funcionar, use `python3 main.py`.

---

## Exemplo de saída

```
==================================================
               RELATÓRIO DE VENDAS                
==================================================

Número de vendas: 15
Faturamento total da loja: R$ 5455.00
Ticket médio: R$ 363.67
Produto mais vendido: Bota - 9 unidades

Maior venda: Bota - R$ 990.00
Menor venda: Legging - R$ 120.00

Vendas por classificação: 
Altas: 7
Médias: 8
Baixas: 0

Faturamento por categoria:
Roupas    : R$ 2165.00
Calçados  : R$ 2025.00
Acessórios: R$ 1265.00
```

---

## Estrutura dos dados

Cada venda é um dicionário dentro de uma lista:

```python
{"produto": "Camiseta", "categoria": "Roupas", "preco": 50.0, "quantidade": 3}
```

---

## Premissas

- Cada item da lista representa **uma venda (uma compra) independente**.
- Os dados não têm identificação de cliente ou de pedido, então o **ticket médio** é calculado por venda (faturamento ÷ número de vendas), e não por cliente.
- Os dados são fictícios e foram criados para fins de estudo.

---

## Aprendizados

- Como agrupar e somar valores por categoria usando dicionários, a mesma ideia do `GROUP BY` no SQL.
- Por que o valor inicial de uma variável importa: para achar o **menor** valor, é preciso começar pelo primeiro item da lista, e não por zero.
- Como encontrar erros de lógica que **não geram mensagem de erro** (por exemplo, um nome de variável com uma letra a mais), conferindo os resultados com `print`.
- A diferença entre venda, cliente e unidade vendida ao calcular o ticket médio.
- Como padronizar a saída no terminal para produzir um relatório legível.

---

## 👩‍💻 Autora

Feito por [clararibz](https://github.com/clararibz) | [LinkedIn](www.linkedin.com/in/maria-clara-ribeiro-silva-482183368)
