# Declaracao e Atribuicao
a = 3
b = 4.4

# Soma um int 3 com um float 4.4. O resultado eh um float 7.4
print(a + b)

# Declaracao e Atribuicao
texto = 'Sua idade eh...'
idade = 23

# f-string: Uma forma interpolar variaveis dentro de um texto.
# O Python substitui o que estah entre { } pelos valores das variaveis
print(f'{texto} {idade}')

# Declaracao e Atribuicao
saudacao = 'bom dia '

# Multiplicação de strings: O Python repete o texto o número de vezes especificado.
# Imprime: bom dia bom dia bom dia
print(3 * saudacao)

# Declaracao e Atribuicao
PI = 3.14

# input(): Recebe um valor do usuario como texto (str).
# float(): Converte esse texto em um numero decimal para que possamos fazer os calculos
raio = float(input('Informe o raio da circunferencia: '))

# pow(base, expoente): Funcao para potencia (raio ao quadrado)
area = PI * pow(raio, 2)

# Imprime o resultado final usando f-string
print(f'A area da circuferencia eh {area} m2')