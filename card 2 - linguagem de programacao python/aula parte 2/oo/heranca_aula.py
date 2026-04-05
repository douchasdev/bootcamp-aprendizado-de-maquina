class Carro:

   def __init__(self):
      # Atributo privado: nao deve ser acessado diretamente
      self.__velocidade = 0

   # Getter para ler a velocidade
   @property
   def velocidade(self):
      return self.__velocidade
   
   # Aumento padrao de velocidade em 5 unidades
   def acelerar(self):
      self.__velocidade += 5
      return self.__velocidade
   
   # Reducao padrao de velocidade em 5 unidades
   def frear(self):
      self.__velocidade -= 5
      return self.__velocidade

# Heranca simples: O Uno herda tudo do Carro sem mudar nada
class Uno(Carro):
   pass

# Polimorfismo: A Ferrari herda de Carro, mas muda o comportamento de 'acelerar'
class Ferrari(Carro):
   # A Ferrari acelera 2x mais rapido
   def acelerar(self):
      super().acelerar()
      return super().acelerar()

# Instanciando uma Ferrari
c1 = Ferrari()

print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())

# O metodo frear nao foi sobrescrito, entao ele usa o padrao (reduz de 5 em 5)
print(c1.frear())
print(c1.frear())
print(c1.frear())