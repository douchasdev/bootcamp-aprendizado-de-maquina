# Cria uma lista chamada 'nums'. Listas usam colchetes [ ]
nums = [1, 2, 3]

# Retorna <class 'list'>
print(type(nums))

# O método .append() adiciona um elemento ao FINAL da lista
nums.append(3)
nums.append(4)
nums.append(500)

# Retorna 6 (quantidade total de elementos apos os appends).
print(len(nums))

# Operador 'in': Verifica se o numero 2 estah na lista. Retorna True
print(2 in nums)

# Altera o valor na posicao (índice) 3 para 100
# Python começa a contar do 0. O índice 3 era o segundo "3"
nums[3] = 100

# Insere o valor -200 na posicao 0, "empurrando" todos os outros para a direita
nums.insert(0, -200)

# Acessa o indice 6. Como adicionamos um item no inicio, a lista cresceu. Imprime 500
print(nums[6])

# Indices negativos começam do final para o começo

# Imprime: 500 (o ultimo elemento)
print(nums[-1])

# Imprime: 4 (o penultimo elemento)
print(nums[-2]) 

# Imprime a lista completa: [-200, 1, 2, 3, 100, 4, 500]
print(nums)