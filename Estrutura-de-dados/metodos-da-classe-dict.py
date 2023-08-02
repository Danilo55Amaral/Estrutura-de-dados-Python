# Métodos da classe dict 

contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"},
    "bill345@gmail.com": {"nome": "Bill", "telefone": "2452-3563"},
    "chappie345@gmail.com": {"nome": "Chappie", "telefone": "2782-3553"},
    "melaine345@gmail.com": {"nome": "Melaine", "telefone": "3342-3345", "extra": {"a": 1}},
}

# Método Clear 
# Esse método é utilizado quando queremos limpar o dicionário, ele apaga todos 
# os elementos do dicionário.
# Exemplo 
contatos.clear()
print(contatos) # {}

# Método copy 
# Esse método cria uma cópia do dicionário, além de copiar também podemos fazer 
# alterações na cópia. É utilizado quando se tem um dicionário e se quer manipular 
# ele e não se quer alterar os dados do dicionário original.
# Exemplo 
contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"},
}

copia = contatos.copy()
copia["danilo345@gmail.com"] = {"nome": "Dan"}

print(contatos["danilo345@gmail.com"]) # {'nome': 'Danilo', 'telefone': '2222-3333'}
print(copia["danilo345@gmail.com"]) # {'nome': 'Dan'}

# Método fromkeys 
# Esse método cria chaves em duas situações, a primeira é quando se quer criar chaves ao 
# dicionário e só se quer colocar a chave lá sem valor, você deve passar apenas as chaves 
# que quer que seja criada e será criada com  valor none.
# A segunda maneira é quando se quer criar um conjunto de chaves, e se quer colocar um valor 
# padrão nela.

# Exemplo primeira situação 
print(dict.fromkeys(["nome", "telefone"])) # 'nome': None, 'telefone': None}
# Exemplo segunda situação.
print(dict.fromkeys(["nome", "telefone"], "vazio")) # {'nome': 'vazio', 'telefone': 'vazio'}
# Ps- Se o dicionário for existente usamos o nome do dicionário, se ele não for usamos o dict.

# Método get 
# Esse método é uma outra forma de acessar valores dentro do dicionário. Quando não sabemos se 
# um método existe ou não dentro do dicionário, quando não utilizamos o get e o elemento não existe ele 
# irá retornar um keyError informando que a chave informada não existe, como vemos na linha 55, quando 
# utilizamos o get e o elemento não existe ele irá retornar um none, uma outra função interessante do get 
# é que podemos passar um valor padrão para ele caso ele não encontre a chave, vemos isso na linha 58.
# Exemplo 
contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"}
}

# print(contatos["chave"]) # KeyError 
print(contatos.get("chave")) # None 
print(contatos.get("chave", {})) # {} 
print(contatos.get("danilo345@gmail.com", {})) # {'nome': 'Danilo', 'telefone': '2222-3333'}

# Método items
# Esse método retorna uma lista de tuplas, é bem util quando queremos fazer um for e iterar
# sobre esses valores do dicionário.
# Exemplo
print(contatos.items()) # dict_items([('danilo345@gmail.com', {'nome': 'Danilo', 'telefone': '2222-3333'})])

# Método keys 
# Esse método retorna só as chaves do dicionário.
# Exemplo 
resultado = contatos.keys() 
print(resultado) # dict_keys(['danilo345@gmail.com']) 
# Exemplo 2  
novo_dicionario = {"a": 100, 1: "teste", "b": "python"} 
print(novo_dicionario.keys()) # dict_keys(['a', 1, 'b'])

# Método pop 
# Esse método remove uma chave do dicionário. Esse método também permite passar 
# um valor padrão a ser retornado caso a chave não exista.
# Exemplo 
print(contatos.pop("danilo345@gmail.com")) # {'nome': 'Danilo', 'telefone': '2222-3333'}
print(contatos.pop("danilo345@gmail.com", {})) # {}

resultado = contatos.pop("danilo@gmail.com" , "Não encontrado na base de dados.") 
print(resultado) # Não encontrado na base de dados.

# Método popitem 
# É semelhante ao pop porém a diferença é que não informamos qual é a chave e ele 
# vai retirando os intems na sequência. Caso ele não encontre mais chaves ele retornar 
# um KeyError.
# Exemplo 
contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"},
}

resultado_popitem = contatos.popitem() 
print(resultado_popitem) # ('danilo345@gmail.com', {'nome': 'Danilo', 'telefone': '2222-3333'})
# print(contatos.popitem()) # KeyError

# Método setdefault 
# Se o atributo não estiver no dicionário ele adiciona com o valor que é colocado como 
# segundo parametro, se o atributo existir no dicionário ele retorna o valor do atributo 
# e não altera ele.
# Exemplo 
contato = {"nome": "Danilo", "tefelone": "2222-9999"}

print(contato.setdefault("nome", "Giovanna")) # Danilo
print(contato) # {'nome': 'Danilo', 'tefelone': '2222-9999'}

print(contato.setdefault("idade", 28)) # 28
print(contato) # {'nome': 'Danilo', 'tefelone': '2222-9999', 'idade': 28}

# Método update 
# Esse método permite atualizar o dicionário utilizando outro dicionário, quando 
# fixemos um update com uma chave que já existe, ele fará um update com essa chave,
# se for feito um update adicionando um novo dicionário e ele possuir chaves que não 
# existem no dicionário original ele vai atualizar o dicionário original.
# Exemplo 
contatos.update({"danilo345@gmail.com": {"Nome": "Dan"}})
print(contatos) # {'danilo345@gmail.com': {'Nome': 'Dan'}

contatos.update({"einstein@gmail.com": {"nome": "Einstein", "telefone": "5533-2222"}})
print(contatos) # {'danilo345@gmail.com': {'Nome': 'Dan'}, 'einstein@gmail.com': {'nome': 'Einstein', 'telefone': '5533-2222'}}

# Método values 
# Esse método retorna apenas os valores das chaves do dicionáro.
# exemplo 
contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"},
    "bill345@gmail.com": {"nome": "Bill", "telefone": "2452-3563"},
    "chappie345@gmail.com": {"nome": "Chappie", "telefone": "2782-3553"},
    "melaine345@gmail.com": {"nome": "Melaine", "telefone": "3342-3345", "extra": {"a": 1}},
}

print(contatos.values()) # dict_values([{'nome': 'Danilo', 'telefone': '2222-3333'}, 
# {'nome': 'Bill', 'telefone': '2452-3563'}, {'nome': 'Chappie', 'telefone': '2782-3553'}, 
# {'nome': 'Melaine', 'telefone': '3342-3345', 'extra': {'a': 1}}])


# Método in 
# Método usado para vefificação, é uma boa prática para verificar se uma chave existe 
# ou não no dicionário.
# Exemplo 
print("danilo345@gmail.com" in contatos) # True 
print("bill345@gmail.com" in contatos) # True
print("idade" in contatos["danilo345@gmail.com"]) # False 
print("telefone" in contatos["melaine345@gmail.com"]) # True

# Exemplo 2
resultado_in = "danilo345@gmail.com" in contatos 
print(resultado_in)

resultado_in = "bill345@gmail.com" in contatos 
print(resultado_in)

resultado_in = "idade" in contatos["danilo345@gmail.com"]
print(resultado_in)

resultado_in = "telefone" in contatos["melaine345@gmail.com"]
print(resultado_in)

# Método del 
# Uma outra forma de tirar um valor do dicionário, basta passar o objeto que 
# queremos remover.
# Exemplo 
del contatos["danilo345@gmail.com"]["telefone"]
del contatos["chappie345@gmail.com"]

print(contatos) # {'danilo345@gmail.com': {'nome': 'Danilo'}, 'bill345@gmail.com': 
#  {'nome': 'Bill', 'telefone': '2452-3563'}, 'melaine345@gmail.com': 
#  {'nome': 'Melaine', 'telefone': '3342-3345', 'extra': {'a': 1}}}