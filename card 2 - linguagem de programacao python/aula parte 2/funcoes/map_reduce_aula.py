from functools import reduce

# 'delta' fica "salvo" no escopo desta funcao
def somar_nota(delta):

   def somar(nota):

      # A nota recebida sera somada ao delta fixado
      return nota + delta
   
   return somar

# Cria uma lista
notas = [6.4, 7.2, 5.4, 8.4]

# retorna uma funcao que sempre soma 1.5
notas_finais_1 = map(somar_nota(1.5), notas)

# retorna uma funcao que sempre soma 1.6
notas_finais_2 = map(somar_nota(1.6), notas)

print(list(notas_finais_1))
print(list(notas_finais_2))

# Define uma funcao de soma
def somar(a, b):
   return a + b

# Reduz a lista a um unico valor: a soma de todas as notas originais
total = reduce(somar, notas, 0)

# Saida: 27.4
print(total)