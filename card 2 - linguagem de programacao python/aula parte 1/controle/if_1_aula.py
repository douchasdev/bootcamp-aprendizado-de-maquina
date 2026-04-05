# Converte a entrada do usuario para float para permitir notas decimais
nota = float(input('Informe a nota do aluno: '))

# Usa um operador ternario para definir um booleano. 
# Se o usuario digitar 'y', comportado eh True; qualquer outra coisa, sera False.
comportado = True if input('Comportado (y/n): ') == 'y' else False

# Exige nota alta e comportamento bom.
if nota >= 9 and comportado:
   print('Duas palavras: para bens! :P')
   print('Quadro de honra')

# Se a primeira falhar, tenta esta: notas entre 7.0 e 8.9.
elif nota >= 7:
   print('Aprovado')

# Se as anteriores falharem, tenta esta: notas entre 5.5 e 6.9.
elif nota >= 5.5:
   print('Recuperacao')

# Notas entre 3.5 e 5.4
elif nota >= 3.5:
   print('Recuperacao + Trabalho')

# Se nenhuma das condicoes acima for atendida (nota < 3.5), cai aqui.
else:
   print('Reprovado')

# Imprime a nota
print(nota)