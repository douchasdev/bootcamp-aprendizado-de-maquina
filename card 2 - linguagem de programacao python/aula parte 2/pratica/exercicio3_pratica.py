# Imagine que voce tem uma lista de objetos da classe Funcionario, onde cada um tem nome, 
# cargo e salario.

# 1. O atributo salario deve ser protegido (__salario) e acessado via @property.

# 2. Use filter para selecionar apenas os funcionários que ganham acima de R$ 5.000,00

# 3. Use reduce para somar o custo total da folha de pagamento apenas desses funcionários 
# filtrados.

from functools import reduce

class Funcionario:

   def __init__(self, nome, cargo, salario):
      self.__nome = nome
      self.__cargo = cargo
      self.__salario = salario

   # O decorador @property transforma o metodo em um "getter"
   # Isso permite acessar 'funcionario.nome' como se fosse um atributo
   @property
   def nome(self):
      return self.__nome
   
   @property
   def cargo(self):
      return self.__cargo
   
   @property
   def salario(self):
      return self.__salario
   
# Criando uma lista
equipe = [
    Funcionario("Alice", "Gerente", 8500.00),
    Funcionario("Bob", "Analista", 4800.00),
    Funcionario("Carla", "Desenvolvedora", 9200.00),
    Funcionario("Diego", "Estagiário", 2000.00),
    Funcionario("Elena", "Coordenadora", 7500.00)
]

# Filtra a lista original baseada em uma condicao logica.
# A lambda recebe cada objeto 'funcionario' e verifica se o salario > 5000
acima_cinco_mil = list(filter(lambda funcionario : funcionario.salario > 5000, equipe))

for funcionario in acima_cinco_mil:
   print(funcionario.nome)

print('')

# Aqui, estamos "extraindo" apenas os valores numericos (salarios) dos objetos filtrados
salarios = list(map(lambda funcionario : funcionario.salario, acima_cinco_mil))

print(f'Salarios: {salarios}')
print('')

# Reduz uma lista a um unico valor
# 'a' eh o acumulador (que começa em 0) e 'b' eh o próximo item da lista de salarios
folha_de_pagamento = reduce(lambda a, b : a + b, salarios, 0)

print(f"Custo total dos salários acima de R$ 5.000,00: R$ {folha_de_pagamento:.2f}")
