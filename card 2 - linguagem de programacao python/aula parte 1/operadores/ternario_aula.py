# Declaracao e atribuicao
lockdown = False
grana = 130

# status sera 'Em casa' se (lockdown for True OU grana for menor ou igual a 100)
# Caso contrário, sera 'Uhuuuu'.
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

# Como lockdown eh False E grana (130) nao eh <= 100, temos False.
# Portanto, status recebe o valor do 'else'.
print(f'O status eh {status}')