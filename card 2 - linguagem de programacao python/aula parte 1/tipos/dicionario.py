# Criando um dicionario. 
# 'nome', 'nota' e 'ativo' sao as CHAVES (keys).
# 'Pedro Henrique', '9.2' e True sao os VALORES (values).
aluno = {
   'nome' : 'Pedro Henrique',
   'nota' : '9.2',
   'ativo' : True
}

# Retorna <class 'dict'>: Abreviacao de 'dictionary'
print(type(aluno))

# Acessa o valor associado a chave 'nome'. Imprime: Pedro Henrique
print(aluno['nome'])

# Acessa o valor associado a chave 'nota'. Imprime: 9.2
print(aluno['nota'])

# Acessa o valor associado a chave 'ativo'. Imprime: True
print(aluno['ativo'])

# Retorna 3. No dicionario, o tamanho conta quantos pares (chave/valor) existem
print(len(aluno))