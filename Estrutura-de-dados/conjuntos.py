# Estrutura de dados set (Conjuntos) 

# Como criar conjuntos 

# Criando sets 
# Um set é uma coleção que não possui objetos repetidos, usamos set para
# representar conjuntos matemáticos ou eliminar itens duplicados de um 
# iterável. 

# Exemplo
# Utilizamos para eliminar elementos duplicados, geralmente utilizado quando 
# queremos eliminar registros duplicados. 
print(set([1, 2, 3, 1, 3, 4])) # {1, 2, 3, 4}
print(set("abacaxi")) # {"b", "a", "c", "x", "i"}
print(set(("palio", "gol", "celto", "palio",))) # {"gol", "celta", "palio"}

# Outra forma de se fazer um set é utilizando chaves veja:
linguagens = {"python", "java", "python"}
print(linguagens) # {'java', 'python'}

# Acessando os dados 
# Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar
# os seus valores é necessário converter o conjunto para lista.
# Exemplo 
numeros = {1, 2, 3, 2} # set 

numeros = list(numeros) # transformando em uma lista.
print(numeros[0]) # acessando o índice. 

# Iterar conjuntos 
# A forma mais comum para percorrer os dados de um conjunto é 
# utilizando o comando for.
# Exemplo 
carros = {"Onix", "Tracker", "Corrola"}

for carro in carros:
    print(carro)

# Função enumerate
# As vezes é necessário saber qual o índice do objeto dentro do laço for.
# Para isso podemos usar a função anumerate.
carros = {"Onix", "Tracker", "Corrola"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos da classe set 
# A Classe set possue vários outros recursos que também são intressantes.

# Método union 
# Pega conjuntos e fáz a união desses conjuntos.
# Exemplo
conjunto_a = {1, 2} 
conjunto_b = {3, 4} 

print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4} 

# Método intersection 
# A parte entre conjuntos que são iguais, ou seja estejam em todos os conjuntos.
# Exemplo 
conjunto_a = {1, 2, 3} 
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) # {2, 3}

# Método difference 
# tudo que está em um conjunto e não está no outro.
# Exemplo
print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

# Método diferença simétrica (symmetric_difference)
# Todos os elementos que não estão na interseção.
# Exemplo 
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# Método issubset 
# Se um conjunto é subconjunto de outro quer dizer que todos os elementos de 
# um conjunto a estão em um conjunto b.
# Exemplo 
conjunto_a = {1, 2, 3} 
conjunto_b = {4, 1, 2, 5, 6, 3}  

print(conjunto_a.issubset(conjunto_b)) # True 
print(conjunto_b.issubset(conjunto_a)) # False 

# Método issuperset 
# É o oposto do issubset, checa se todos os elementos de um conjunto b estão em 
# um conjunto a. 
# Exemplo 
print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True 

# Método isdisjoint 
# É quando os conjuntos não possuem intersecção, todos os elementos de um conjunto 
# não estão presentes dentro de outro conjunto.
# Exemplo 
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9} 
conjunto_c = {1, 0} 

print(conjunto_a.isdisjoint(conjunto_b)) # True 
print(conjunto_a.isdisjoint(conjunto_c)) # False

# Método add 
# Para inserir um elemento caso ele não exista.
# Exemplo 
sorteio = {1, 23} 

print(sorteio.add(25)) # {1, 23, 25} 
print(sorteio.add(42)) # {1, 23, 25, 42} 
print(sorteio.add(25)) # {1, 23, 25, 42} Se passar um elemento de já existe ele será ignorado.

# Método clear 
# Ele pega o set e limpa totalmente.
# Exemplo 
print(sorteio) # {1,23}
sorteio.clear()
print(sorteio) # {}

# Método copy
# Ele cria uma cópia 
# Exemplo 
print(sorteio) # {1, 23}
sorteio.copy()
print(sorteio) # {1, 23}

# Método discard 
# Esse método vai discartar um valor.
# Exemplo 
numeros = {1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0}

print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(numeros.discard(1)) 
print(numeros.discard(45)) # Não existe então ele não faz nada.
print(numeros) # {2, 3, 5, 6, 7, 8, 9, 0}

# Método pop 
# Ele vai tirando os elementos da lista sem a necessidade de passar argumento.
# Ele sempre vai tirar o elemento da frente.
# Exemplo 
numeros = {1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop()) # 0
print(numeros.pop()) # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

# Método remove 
# Ele remove o valor que eu passar como argumento. Se você tentar remover um elemento que 
# não exista ele irá retornar um key error.
# Exemplo 
numeros = {1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0)) # 0
print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Método len 
# Ele retorna o tamanho do conjunto. 
# Exemplo 
numeros = {1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0}

print(len(numeros)) # 10 

# Operador in 
# Também pode ser utilizado para verificar se um elemento está no conjunto. 
# Exemplo 
numeros = {1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 9, 0}

print(1 in numeros) # True 
print(10 in numeros) # False