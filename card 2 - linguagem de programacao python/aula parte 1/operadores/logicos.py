# Declaracao e atribuicao
b1 = True
b2 = False
b3 = True

# Operador 'and' (E): So retorna True se todos forem verdadeiros
# Como b2 eh False, o resultado final eh False
print(b1 and b2 and b3)

# Operador 'or' (OU): Retorna True se pelo menos um for verdadeiro
# Como b1 e b3 sao True, o resultado eh True
print(b1 or b2 or b3)

# Operador 'not' (NAO): Inverte o valor
# O que era True vira False
print(not b1)

# O que era False vira True
print(not b2)

# Combinacao: b1(True) e nao-b2(True) e b3(True), entao o resultado eh True
print(b1 and not b2 and b3)

# Declaracao e atribuicao
x = 3
y = 4

# b1(True) AND not b2(True) AND (3 < 4)(True), entao o resultado final eh True
print(b1 and not b2 and x < y)