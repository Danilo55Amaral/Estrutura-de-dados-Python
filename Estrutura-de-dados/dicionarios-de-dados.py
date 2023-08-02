# Criação e acesso aos dados

# Criando dicionários 
# Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves 
# são únicas em uma dada instância do dicionário. Dicionários são delimitados por 
# chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas. 

# PS - Para ser uma chave válida para o dicionário o objeto tem que ser imutável.

# Exemplo 
pessoa = {"nome": "Danilo", "idade": 27} 

# Mesma declaração a cima porém ao invés de {} estou utilizando o constutor dict.
pessoa = dict(nome="Danilo", idade=27) 

# Outra maneira é quando já se tem um dicionário criado e queremos adicionar mais 
# uma chave:valor a ele.
pessoa["telefone"] = "5555-2323" 

print(pessoa) # {'nome': 'Danilo', 'idade': 27, 'telefone': '5555-2323'}

# Acesso aos dados 
# Os dados são acessados e modificados através da chave. Eu estou acessando os 
# valores note que não existe atribuição quando eu acesso.
# Exemplo 
dados = {"nome": "Danilo", "idade": 27, "telefone": "5555-2323"}

print(dados["nome"]) # "Danilo"
print(dados["idade"]) # 27 
print(dados["telefone"]) # 5555-2323 

# Note que quando eu acesso e utilizo o operador de atribuiçao eu posso 
# modificar o valor.
dados["nome"] = "Mychelle"
dados["idade"] = 18 
dados["telefone"] = 5255-2323

print(dados) # {'nome': 'Mychelle', 'idade': 18, 'telefone': 2932}

# Dicionários aninhados 
# Dicionários podem armazenar qualquer tipo de objeto Python como valor, 
# desde que a chave para esse valor seja um objeto imutável como (strings e números).
# Exemplo 
contatos = {
    "danilo345@gmail.com": {"nome": "Danilo", "telefone": "2222-3333"},
    "bill345@gmail.com": {"nome": "Bill", "telefone": "2452-3563"},
    "chappie345@gmail.com": {"nome": "Chappie", "telefone": "2782-3553"},
    "melaine345@gmail.com": {"nome": "Melaine", "telefone": "3342-3345", "extra": {"a": 1}},
}

print(contatos["bill345@gmail.com"]["telefone"]) # 2452-3563

#  Outra forma também é armazenando em uma variável.
telefone = contatos["bill345@gmail.com"]["telefone"]
print(telefone) # 2452-3563

extra = contatos["melaine345@gmail.com"]["extra"]["a"]
print(extra) # 1 

# Iterar dicionários 
# A forma mais comum para percorrer os dados de um dicionário é 
# utilizando o comando for
# Exemplo 1
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)
# Exemplo 2 
for chave, valor in contatos.items():
    print(chave, valor)

# Veja o Resultado:
# danilo345@gmail.com {'nome': 'Danilo', 'telefone': '2222-3333'}
# bill345@gmail.com {'nome': 'Bill', 'telefone': '2452-3563'}
# chappie345@gmail.com {'nome': 'Chappie', 'telefone': '2782-3553'}
# melaine345@gmail.com {'nome': 'Melaine', 'telefone': '3342-3345', 'extra': {'a': 1}}
# ====================================================================================================
# danilo345@gmail.com {'nome': 'Danilo', 'telefone': '2222-3333'}
# bill345@gmail.com {'nome': 'Bill', 'telefone': '2452-3563'}
# chappie345@gmail.com {'nome': 'Chappie', 'telefone': '2782-3553'}
# melaine345@gmail.com {'nome': 'Melaine', 'telefone': '3342-3345', 'extra': {'a': 1}}