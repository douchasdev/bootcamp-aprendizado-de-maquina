# O caractere '*' (args) permite passar um numero variavel de argumentos posicionais
# O Python empacota todos os valores recebidos em uma tupla chamada 'nums'
def soma(*nums):
   
   total = 0

   # Itera sobre a tupla para somar cada elemento
   for n in nums:
      total += n
   
   return total

# O caractere '**' (kwargs) permite passar um numero variavel de argumentos nomeados (chave=valor)
# O Python empacota esses argumentos em um dicionario chamado 'kwargs'
def resultado_final(**kwargs):

   # Usa um operador ternario para decidir o status com base na chave 'nota' do dicionário
   status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
   
   # Acessa as chaves 'nome' e o resultado da variavel 'status' para retornar a frase
   return f'{kwargs['nome']} foi {status}'