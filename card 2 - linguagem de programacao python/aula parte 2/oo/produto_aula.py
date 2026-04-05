class Produto:

   # Metodo construtor: define os valores iniciais do objeto
   def __init__(self, nome, preco = 1.99, desc = 0):
      
      self.nome = nome
      # O uso de __ (duplo underscore) indica um atributo privado
      self.__preco = preco
      self.desc = desc

   # @property: Transforma um metodo em um "atributo" (Getter)
   # Permite ler o valor de __preco como se fosse um atributo comum: p1.preco
   @property
   def preco(self):
      return self.__preco
   
   # @setter: Permite a alteracao de valor (Setter)
   # aplica as regras de negócio (validação)
   @preco.setter
   def preco(self, novo_preco):
      if novo_preco > 0:
         self.__preco = novo_preco

   # Atributo calculado: Nao existe no __init__, mas eh gerado sob demanda
   @property
   def preco_final(self):
      return (1 - self.desc) * self.preco
   
# Instanciando os objetos
p1 = Produto('Caneta', 10, 0.1)
p2 = Produto('Caderno', 14, 0.5)

# Usando o setter
p1.preco = 70.89
p2.preco = 17.99

# Imprime o nome, o preco, o desconto e o preco final das instancias de produto
print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)