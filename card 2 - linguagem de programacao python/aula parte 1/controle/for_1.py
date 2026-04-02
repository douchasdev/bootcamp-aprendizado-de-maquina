# Gera numeros de 0 a 9
for i in range(10):
   print(i)

# Pula linha
print('')

# Comeca no 1 e vai ate o 10
for i in range(1, 11):
   print(i)

print('')

# Comeca no 1, vai ate < 100, pulando de 7 em 7
for i in range(1, 100, 7):
   print(i)

print('')

# Faz uma contagem regressiva de 20 ate 1, de 3 em 3
for i in range(20, 0, -3):
   print(i)

print('')

# Cria uma lista
nums = [2, 4, 6, 8]

# Percorre cada elemento da lista. end=' ' mantém a impressão na mesma linha
for n in nums:
   print(n, end=' ')

print('')

# Declaracao e atribuicao
texto = 'Python eh muito massa!'

# Strings sao sequencias, o for percorre cada caractere (incluindo espaços)
for letra in texto:
   print(letra, end=' ')

print('')

# No Set, o for percorre apenas os elementos ÚNICOS {1, 2, 3, 4}.
for n in {1, 2, 3, 4, 4, 4}:
   print(n, end=' ')

print('')

# Cria um dicionario
produto = {
   'nome' : 'Caneta',
   'preco' : 8.80,
   'desc' : 0.5
}

# Iterar direto no dicionario percorre apenas as chaves.
for atrib in produto:
   print(atrib, '==>', produto[atrib])

print('')

# Pega chave e valor ao mesmo tempo
for atrib, valor in produto.items():
   print(atrib, '==>', valor)

print('')

# Ignora as chaves e percorre apenas os valores
for valor in produto.values():
   print(valor, end=' ')

print('')

# Ignora os valores e percorre apenas as chaves
for atrib in produto.keys():
   print(atrib, end=' ')
