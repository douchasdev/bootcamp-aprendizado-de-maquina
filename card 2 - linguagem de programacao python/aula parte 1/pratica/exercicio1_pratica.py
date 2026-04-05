# Você recebeu uma lista de dicionarios representando produtos em um estoque

# Lista de dicionários representando os produtos no estoque
estoque = [
    {'nome': 'Teclado', 'valor': 150.0, 'quantidade': 5},
    {'nome': 'Mouse', 'valor': 80.0, 'quantidade': 0},
    {'nome': 'Monitor', 'valor': 900.0, 'quantidade': 3},
    {'nome': 'Fone', 'valor': 120.0, 'quantidade': 10}
]

# Crie um laço for que percorra essa lista e para cada produto:

# 1. Imprima o nome do produto
# 2. Verifique se a quantidade eh maior que 0. Se for 0, imprima "FORA DE ESTOQUE"
# 3. Calcule o valor total em estoque para aquele produto (valor * quantidade) e 
   # mostre na tela

# 1.

# percorre cada dicionario da lista
for produto in estoque:

   # pega o valor da chave 'nome'
   nome = produto['nome']

   # imprime o nome do produto
   print(nome)

print('')

# 2.

# percorre novamente a lista
for produto in estoque:

   # pega o valor da chave 'nome'
   nome = produto['nome']

   # pega a quantidade do produto
   quantidade = produto['quantidade']

   # verifica se a quantidade é igual a 0
   if quantidade == 0:

      # imprime mensagem de produto fora de estoque
      print(f'Produto: {nome} | FORA DE ESTOQUE')

print('')

# 3.

# percorre a lista novamente
for produto in estoque:

   # nome do produto
   nome = produto['nome']

   # valor unitario
   valor = produto['valor']

   # quantidade disponivel
   quantidade = produto['quantidade']

   # calcula e imprime o valor total (valor * quantidade)
   print(f'Produto: {nome} | Quantidade: {quantidade} | Valor unitario: {valor} | Valor total em estoque: {valor * quantidade}')   
