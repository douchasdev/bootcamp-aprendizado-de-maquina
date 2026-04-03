# Crie uma classe Produto que utilize @property para o preço e o nome. 
# Em seguida, crie uma função que retorna função chamada 
# gerar_calculadora_desconto(taxa)

# 1. A classe Produto deve ter nome e preco

# 2. A função gerar_calculadora_desconto(taxa) deve retornar uma função que 
# recebe um objeto Produto e retorna o preço dele com o desconto aplicado

# 3. Use map para aplicar uma calculadora de 10% de desconto em uma lista de 3 produtos 
# e imprima os novos preços

class Produto:

   def __init__(self, nome, preco):
      
      # Utilizamos o prefixo '__' (double underscore) para indicar atributos "privados"
      self.__nome = nome
      self.__preco = preco

   # O decorador @property transforma o metodo em um "getter"
   # Isso permite acessar 'produto.nome' como se fosse um atributo
   @property
   def nome(self):
      return self.__nome
   
   @property
   def preco(self):
      return self.__preco
   
   # O setter permite definir regras para a alteracao de um valor
   @preco.setter
   def preco(self, valor):
      if valor > 0:
         self.__preco = valor

# A funcao principal gurada o valor da taxa
def gerar_calculadora_desconto(taxa):

   # A funcao interna consegue acessar a 'taxa' da funcao externa
   def produto_com_desconto(produto):
      valor_com_desconto = produto.preco * (1 - taxa)
      return f'Produto: {produto.nome} | De: R$ {produto.preco:.2f} por R$ {valor_com_desconto:.2f}'
      
   return produto_com_desconto
   
# Criando a lista de objetos
carrinho = [
    Produto("Teclado", 250.00),
    Produto("Mouse", 150.00),
    Produto("Monitor", 1200.00)
]

# Aplicar 10% de desconto
dia_de_desconto = gerar_calculadora_desconto(0.10)

# O 'map' aplica a funcao 'dia_de_desconto' a cada item da lista 'carrinho'
produtos_com_desconto = map(dia_de_desconto, carrinho)

# Exibe o resultado
for produto in produtos_com_desconto:
   print(produto)
