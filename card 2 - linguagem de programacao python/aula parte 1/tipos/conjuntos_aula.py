# Imprime o conjunto {1, 2, 3}
print({1, 2, 3})

# Retorna <class 'set'>: O Python identifica chaves como um 'set'
print(type({1, 2, 3}))

# Cria um set chamado 'conj' 
conj = {1, 2, 3, 3, 3, 3, 3}

#print(conj[1]) ERRO Sets nao sao indexados

# Imprime {1, 2, 3}. Por ser set, as duplicadas sao removidas
print(conj)

# Como as duplicadas sao ignoradas, retorna o valor(tamanho) 3
print(len(conj))