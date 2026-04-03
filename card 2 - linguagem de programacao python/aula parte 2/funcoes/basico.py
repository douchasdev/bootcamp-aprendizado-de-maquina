# Define uma funcao com parametros padrao (default arguments)
# Se nenhum valor for passado, nome sera 'Pessoa' e idade sera 20
def saudacao(nome = 'Pessoa', idade = 20):
   print(f'Bom dia {nome}! Vc nem parece ter {idade} anos!')

# Define uma funcao matematica simples
def soma_e_multi(a, b, x):
   return a + b * x

# Imprime o valor da variavel especial __name__
# Isso serve para saber se o arquivo está sendo executado diretamente ou importado
print(__name__)

# Garante que este codigo abaixo so execute se o arquivo for rodado diretamente (main)
# Se este arquivo for importado por outro, este bloco eh ignorado
if __name__ == '__main__':
   saudacao('Ana', idade = 30)