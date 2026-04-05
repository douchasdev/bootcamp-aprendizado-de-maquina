# Retorna '__main__' se o arquivo for executado diretamente.
# Essa variável indica o nome do escopo onde o código está rodando
print(__name__)

# Retorna None (ou o nome do pacote).
# Indica a qual pacote o modulo pertence. Se for um script solto, sera None
print(__package__)

# Retorna 321
# A funcao abs() calcula o valor absoluto (ou modulo) de um numero, 
# ou seja, a distancia dele ate o zero, ignorando o sinal de menos
print(abs(-321))