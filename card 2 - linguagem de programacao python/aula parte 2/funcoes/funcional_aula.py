# Define uma funcao de soma
def soma(a, b):
   return a + b

# Define uma funcao de subtracao
def sub(a, b):
   return a - b

# Funcoes como Objetos: Atribuindo uma funcao a uma variavel
# Aqui, 'somar' passa a apontar para o mesmo codigo que 'soma'
somar = soma
print(somar(3, 4))

# Esta funcao recebe outra funcao ('fn') como um argumento
def operacao_aritmetica(fn, op1, op2):
   return fn(op1, op2)

# Passando a funcao 'soma' como parametro
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

# Passando a funcao 'sub' como parametro
resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

def soma_parcial(a):

   # processamente pesado 1 - 10s
   # processamente pesado 2 - 10s
   # processamente pesado 3 - 40s

   # Esta funcao interna "lembra" do valor de 'a' mesmo apos
   # soma_parcial ter terminado sua execucao.
   def concluir_soma(b):
      return a + b # 10s
   
   # Retorna a funcao interna, nao o resultado da funcao principal
   return concluir_soma

# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s

soma_1 = soma_parcial(1) # 1m

# O valor de 'a' (que eh 1) ja esta "salvo" em soma_1.
r1 = soma_1(2) # 10s
r2 = soma_1(3) # 10s
r3 = soma_1(4) # 10s

# O primeiro par de parenteses chama a funcao externa, 
# o segundo chama a funcao interna retornada.
resultado_final = soma_parcial(10)(12)
print(resultado_final, r1, r2, r3)