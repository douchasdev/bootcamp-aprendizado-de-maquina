# O reduce eh usado para aplicar uma operacao cumulativa a todos os itens de uma lista
from functools import reduce

# Lista de dicionarios representando a base de dados (dataset)
alunos = [

   {'nome': 'Ana', 'nota' : 7.2},
   {'nome': 'Breno', 'nota' : 8.1},
   {'nome': 'Claudia', 'nota' : 8.7},
   {'nome': 'Pedro', 'nota' : 6.4},
   {'nome': 'Rafael', 'nota' : 6.7}
]

# Define uma funcao anonima (lambda) que recebe dois valores e retorna a soma deles
somar = lambda a, b: a + b

# Cria uma nova lista apenas com os dicionarios dos alunos que tiraram 7 ou mais
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]

# Extrai apenas o valor numerico das notas da lista de aprovados
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]

# Imprime a lista de dicionarios dos alunos aprovados
print(alunos_aprovados)

# O reduce aplica a funcao 'somar' sucessivamente: ((0 + nota1) + nota2) ...
# O '0' no final eh o valor inicial (initializer) para evitar erros em listas vazias
total = reduce(somar, notas_alunos_aprovados, 0)

# Calcula e imprime a media das notas dos alunos aprovados
print(total / len(alunos_aprovados))


