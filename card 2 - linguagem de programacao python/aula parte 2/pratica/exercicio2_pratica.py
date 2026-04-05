# Crie uma classe base Veiculo com um @classmethod que conte quantos 
# veículos foram instanciados

# 1. Crie duas subclasses: Carro e Moto

# 2. A Moto deve ter um método acelerar que aumenta a velocidade em 10, 
# enquanto o Carro aumenta apenas 5 (use Polimorfismo).

# 3. # Crie um @staticmethod na classe base chamado converter_km_para_milhas(km) 
# que apenas faz o cálculo matemático (km x 0.62).

# Instancie um de cada, acelere-os e exiba o contador total da classe

class Veiculo:

   # Atributo de classe: compartilhado por todas as instancias e subclasses
   total_veiculos = 0

   # 'cls' refere-se à classe em si. Toda vez que chamado, incrementa o contador global
   @classmethod
   def registrar_veiculo(cls):
        cls.total_veiculos += 1
   
   # "Atributos privados"
   def __init__(self, modelo):
      self.__modelo = modelo
      self.__velocidade = 0

      # Chama o metodo de classe para contar a nova instancia
      Veiculo.registrar_veiculo()

   # O decorador @property transforma o metodo em um "getter"
   # Isso permite acessar 'veiculo.velocidade' como se fosse um atributo
   @property
   def velocidade(self):
      return self.__velocidade
   

   @property
   def modelo(self):
      return self.__modelo
   
   # Comportamento padrao: aumenta de 5 em 5
   def acelerar(self):
        self.__velocidade += 5
        return self.__velocidade
   
   # Metodos estaticos nao acessam atributos da classe (cls) nem da instancia (self)
   # Funcionam como funcoes utilitarias dentro do escopo da classe
   @staticmethod
   def converter_km_para_milhas(km):
        return km * 0.62
   
# O Carro herda tudo de Veiculo, inclusive o metodo acelerar (+5)
class Carro(Veiculo):
    pass

# Polimorfismo: A moto sobrescreve o metodo acelerar para ter seu proprio comportamento
class Moto(Veiculo):
    def acelerar(self):
        self._Veiculo__velocidade += 10
        return self._Veiculo__velocidade

# Instanciacao
c1 = Carro("Fusca")
m1 = Moto("Ninja 600")

# Testando o Polimorfismo
print(f"{c1.modelo} acelerando: {c1.acelerar()} km/h")
print(f"{m1.modelo} acelerando: {m1.acelerar()} km/h")

# Testando o Metodo Estatico
velocidade_em_milhas = Veiculo.converter_km_para_milhas(m1.velocidade)
print(f"Velocidade da moto em milhas: {velocidade_em_milhas:.2f}")

# Exibindo o Atributo de Classe via Class Method
print(f"Total de veículos na frota: {Veiculo.total_veiculos}")
