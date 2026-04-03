class Contador:

   # Atributo de Classe: Compartilhado por todas as instancias
   contador = 0

   # Metodo de Instancia
   # Precisa do 'self' porque opera em um objeto especifico (c1, c2, etc.)
   def inst(self):
      return 'Estou bem!'

   # Metodo de Classe (@classmethod)
   # Nao recebe o objeto (self), mas recebe a propria classe (cls)
   # Eh usado para manipular atributos que pertencem a classe toda
   @classmethod
   def inc(cls):
      cls.contador += 1
      return cls.contador
   

   @classmethod
   def dec(cls):
      cls.contador -= 1
      return cls.contador
   
   # Metodo Estatico (@staticmethod)
   # Nao recebe nem 'self' nem 'cls'. É apenas uma função comum 
   # que pertence a classe, mas nao mexe nos dados dela
   @staticmethod
   def mais_um(n):
      return n + 1

# Criamos uma instancia (objeto)
c1 = Contador()

# Chamada via instancia
print(c1.inst())

# Chamamos os metodos de classe diretamente pela Classe (sem precisar de instancias)
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())

# Chamamos o metodo estatico
print(Contador.mais_um(99))