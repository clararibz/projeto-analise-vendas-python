# Objetivo: simular o relatório de vendas de uma pequena loja

vendas = [ # lista das vendas da loja em um mês
    {"produto": "Camiseta", "categoria": "Roupas", "preco": 50.0, "quantidade": 3},
    {"produto": "Tênis", "categoria": "Calçados", "preco": 200.0, "quantidade": 2},
    {"produto": "Saia", "categoria": "Roupas", "preco": 70.0, "quantidade": 4},
    {"produto": "Calça", "categoria": "Roupas", "preco": 90.0, "quantidade": 4},
    {"produto": "Sandália", "categoria": "Calçados", "preco": 45.0, "quantidade": 3},
    {"produto": "Vestido", "categoria": "Roupas", "preco": 60.0, "quantidade": 5},
    {"produto": "Macacão", "categoria": "Roupas", "preco": 70.0, "quantidade": 4},
    {"produto": "Short", "categoria": "Roupas", "preco": 75.0, "quantidade": 7},
    {"produto": "Salto alto", "categoria": "Calçados", "preco": 100.0, "quantidade": 5},
    {"produto": "Colar", "categoria": "Acessórios", "preco": 80.0, "quantidade": 2},
    {"produto": "Brinco", "categoria": "Acessórios", "preco": 95.0, "quantidade": 7},
    {"produto": "Pijama", "categoria": "Roupas", "preco": 50.0, "quantidade": 3},
    {"produto": "Boné", "categoria": "Acessórios", "preco": 55.0, "quantidade": 8},
    {"produto": "Legging", "categoria": "Roupas", "preco": 30.0, "quantidade": 4},
    {"produto": "Bota", "categoria": "Calçados", "preco": 110.0, "quantidade": 9},
]


# 1. Calcular o faturamento total (preço × quantidade de cada venda)
faturamento_total = 0

for venda in vendas:
    faturamento = venda["preco"] * venda["quantidade"]
    faturamento_total += faturamento

print(f"\nFaturamento total: {faturamento_total}\n")


# 2. Calcular o ticket médio (faturamento total ÷ número de vendas)
# quanto, em média, cada venda rendeu
total_vendas = len(vendas)
ticket_medio = faturamento_total / total_vendas

print(f"Ticket médio: {ticket_medio:.2f}\n")


# 3. Descobrir qual foi o produto mais vendido em quantidade
maior_quantidade = 0
mais_vendido = ""

for venda in vendas:
    if venda["quantidade"] > maior_quantidade:
        maior_quantidade = venda["quantidade"]
        mais_vendido = venda["produto"]

print(f'Produto mais vendido: {mais_vendido} - {maior_quantidade} unidades\n')


# 4. Calcular o faturamento por categoria usando um dicionário ({"Roupas": 450.0, "Calçados": 800.0}).
faturamento_categoria = {}
 
for venda in vendas:
    categoria = venda["categoria"]
    faturamento = venda["preco"] * venda["quantidade"]
 
    if categoria in faturamento_categoria:
        faturamento_categoria[categoria] += faturamento # O 'categoria' está sem aspas pois usa o VALOR da variavél
    else:
        faturamento_categoria[categoria] = faturamento

print(f"Faturamento por categoria: {faturamento_categoria}\n")


# 5. Mostrar a venda de maior valor e a de menor valor
maior_valor = vendas[0]["preco"] * vendas[0]["quantidade"]
menor_valor = maior_valor
produto_maior = vendas[0]["produto"]
produto_menor = vendas[0]["produto"]

for venda in vendas:
    valor_venda = venda["preco"] * venda["quantidade"]

    if valor_venda > maior_valor:
        maior_valor = valor_venda
        produto_maior = venda["produto"]

    if valor_venda < menor_valor:
        menor_valor = valor_venda
        produto_menor = venda["produto"]

print(f"Maior venda: {produto_maior} - R$ {maior_valor}")
print(f"Menor venda: {produto_menor} - R$ {menor_valor}\n")


# 6. Classificar cada venda com if/elif/else:
# “Alta” (acima de R$ 300), “Média” (entre R$ 100 e R$ 300) e “Baixa” (abaixo de R$ 100)
altas = 0
medias = 0
baixas = 0

print(f"Classificação das vendas:")

for venda in vendas:
    valor_venda = venda['preco'] * venda["quantidade"]
    if valor_venda > 300:
        classificacao = "Alta"
        altas += 1
    elif 100 <= valor_venda <= 300:
        classificacao = "Média"
        medias += 1
    else:
        classificacao = "Baixa"
        baixas += 1
        
    print(f"{venda['produto']:<12} R$ {valor_venda:>8.2f}  -> {classificacao}")


# 7. Imprimir um relatório formatado no terminal

print()
print('=' *50)
print(f"{'RELATÓRIO DE VENDAS':^50}")
print('=' *50)
print()
print(f"Número de vendas: {total_vendas}")
print(f"Faturamento total da loja: {faturamento_total}")
print(f"Ticket médio: {ticket_medio:.2f}")
print(f"Produto mais vendido: {mais_vendido} - {maior_quantidade} unidades")
print()
print(f"Maior venda: {produto_maior} - R$ {maior_valor:.2f}")
print(f"Menor venda: {produto_menor} - R$ {menor_valor:.2f}")
print()
print(f"Vendas por classificação: ")
print(f"Altas: {altas}\nMédias: {medias}\nBaixas: {baixas}")
print()
print("Faturamento por categoria:")
for categoria in faturamento_categoria:
    print(f"{categoria: <10}: {faturamento_categoria[categoria]:.2f}")
