# Preenchido -> True
a = 'valor'

# Zero numerico -> False
a = 0

# Diferente de zero -> True
a = -0.00001

# String vazia -> False
a = ''

# String com um espaco (nao esta vazia!) -> True
a = ' '

# Lista vazia -> False
a = []

# Dicionario vazio -> False
a = {}

# O conteudo da variável 'a' eh avaliado
# Se for considerado um valor "True", entra no if.
# Se for "False", cai no else.
if a:
   print('Existe!!!')

else:
   print('Nao existe ou zero ou vazio...')