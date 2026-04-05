# Vai somar todas as notas digitadas
total = 0

# Vai contar quantas notas validas foram inseridas
qtde = 0

# Inicializada com 0 para entrar no loop
nota = 0

# O loop continuara executando enquanto a nota for diferente de -1
while nota != -1:
   nota = float(input('Informe a nota ou -1 para sair: '))

   # So processamos a nota se ela nao for o sinal de saida (-1)
   if nota != -1:
      qtde += 1
      total += nota

# apos sair do loop, calcula e exibe a media aritmetica.
print(f'A media da turma eh {total / qtde}')