# Cria listas
pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

# Loops Aninhados: Para cada pessoa, percorre-se todos os adjetivos.
# Isso gera todas as combinacoes possíveis entre as duas listas.
for p in pessoas:
   for a in adjs:
      print(f'{p} eh {a}!')

# Pula linha
print('')

# pass eh um "marcador de lugar". Nao faz nada. 
# Eh usado quando a sintaxe exige um bloco de codigo, mas nao foi decidido o que colocar
for i in [1, 2, 3]:
   pass

# continue: Interrompe a iteracao atual e pula direto para a proxima volta do loop
# No caso, se for impar ignore. Resultado: 2, 4, 6, 8, 10
for i in range(1, 11):
   if i % 2 == 1:
      continue
   else:
      print(i)

print('')

# break: Interrompe o loop completamente e sai dele imediatamente
# Quando chegar em 5, o loop eh encerrado na hora
for i in range(1, 11):
   if i == 5:
      break
   else:
      print(i)

print('')

# Imprime "Fim!"
print("Fim!")