from functools import reduce

# Lista de dicionarios
alunos = [

   {'nome': 'Ana', 'nota' : 7.2},
   {'nome': 'Breno', 'nota' : 8.1},
   {'nome': 'Claudia', 'nota' : 8.7},
   {'nome': 'Pedro', 'nota' : 6.4},
   {'nome': 'Rafael', 'nota' : 6.7}
]

# Retorna True se a nota for maior ou igual a 7
aluno_aprovado = lambda aluno : aluno['nota'] >= 7

# Extrai apenas o valor numerico da nota do dicionario
obter_nota = lambda aluno: aluno['nota']

# Soma dois valores
somar = lambda a, b: a + b

# Filtra a lista original mantendo apenas quem passou (Ana, Breno, Claudia)
alunos_aprovados = list(filter(aluno_aprovado, alunos))

# Transforma a lista de objetos filtrados em uma lista de numeros (notas)
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))

# Saida: [7.2, 8.1, 8.7]
print(notas_alunos_aprovados)

# Reduz a lista de notas a um unico valor (a soma de todas elas)
# O '0' no final eh o valor inicial do acumulador
total = reduce(somar, notas_alunos_aprovados, 0)

# Saida: 8.0
print(total / len(alunos_aprovados))


