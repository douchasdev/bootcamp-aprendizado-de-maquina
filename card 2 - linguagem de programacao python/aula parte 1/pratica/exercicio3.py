# Sequencias numericas e logica matematica

# 1. Crie uma lista chamada numeros usando list(range(1, 21))
# 2. Use um for para percorrer essa lista e imprima apenas os numeros que são múltiplos de 3
# 3. Crie uma nova variavel que receba apenas os ultimos 5 itens da lista original
# 4. Verifique se o numero 15 esta presente na lista original

# 1.

# Cria uma lista de 1 ate 20
numeros = list(range(1, 21))

# Imprime a lista
print(numeros)

print('')

# 2.

# Percorre cada numero da lista
for numero in numeros:

   # Verifica se o numero eh divisivel por 3 (resto da divisao igual a 0)
   if numero % 3 == 0:
      print(f'{numero} eh multiplo de 3')

print('')

# 3.

# Usa fatiamento (slice) para pegar os ultimos 5 elementos da lista
# O índice negativo -5 começa do final da lista
ultimo_cinco_itens = numeros[-5:]

# Imprime os ultimos 5 itens
print(f'Os ultimos 5 itens da lista sao: {ultimo_cinco_itens}')

print('')

# 4.

# Define o numero que queremos verificar
numero = 15

# Verifica se o numero esta dentro da lista usando o operador "in"
# Retorna True (verdadeiro) ou False (falso)
print(f'O numero 15 esta presente na lista? {numero in numeros}')