# Crie um sistema de login simplificado

# 1. Defina uma variavel senha = 'python123'
# 2. Use um laço while que fale para o usuario digitar uma senha
# 3. Se ele digitar a senha correta, imprima "Acesso Concedido" e use o break para sair
# 4. Se ele errar, imprima "Senha Incorreta, tente novamente"
# 5. Use um contador para permitir apenas 3 tentativas. Se esgotar, imprima "Conta Bloqueada"

# Define a senha correta
senha = 'python123'

# Define o número maximo de tentativas
tentativas = 3

# Enquanto ainda houver tentativas disponiveis
while tentativas > 0:

   # Solicita que o usuario digite a senha
   # Mostra quantas tentativas ainda restam
   senha_digitada = input(f'Digite a senha ({tentativas} tentativas restantes): ')

   # Verifica se a senha digitada esta correta
   if senha_digitada == senha:
      print('Acesso Concedido') # mensagem de sucesso
      break # sai do loop imediatamente

   else:
      
      # Se a senha estiver incorreta, diminui o número de tentativas em 1
      tentativas -= 1

      # Verifica se ainda restam tentativas
      if tentativas > 0:
         print('Senha Incorreta, tente novamente')

      # Caso nao tenha mais tentativas
      else:
         print('Conta Bloqueada') # bloqueia o acesso
   
