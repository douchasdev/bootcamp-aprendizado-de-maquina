# Cria uma tupla chamada 'nomes'. Tuplas usam parênteses ( ).
# Tuplas aceitam elementos repetidos ('Ana')
nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana')

# Verifica se 'Bia' estah na tupla. Retorna True
print('Bia' in nomes)

# Acessa o primeiro elemento (indice 0). Imprime: Ana
print(nomes[0])

# Pega do indice 1 ate o 3 (o 3 eh excluido). Imprime: ('Bia', 'Gui')
print(nomes[1:3])

# Do indice 1 ate o penultimo (o -1 eh excluido). Imprime: ('Bia', 'Gui')
print(nomes[1:-1])

# Do indice 2 ate o final. Imprime: ('Gui', 'Leo', 'Ana')
print(nomes[2:])

# Do inicio ate o antepenultimo (o -2 eh excluido). Imprime: ('Ana', 'Bia', 'Gui')
print(nomes[:-2])

# Retorna 5 (total de elementos, incluindo duplicatas).
print(len(nomes))

# Retorna <class 'tuple'>
print(type(nomes))

# Imprime a tupla
print(nomes)