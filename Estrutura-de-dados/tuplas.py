# Tuplas 

# Criação e acesso aos dados.

# Criando tuplas
# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que 
# tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe
# tuple, ou colocando valores separados por vírgula de parenteses. É indicado sempre colocar 
# uma virgula ao final. 

# Exemplo 
frutas = ("laranja", "pera", "uva",) 

letras = tuple("python") 

numeros = tuple([1, 2, 3, 4]) # Passando uma lista para uma tupla. 

pais = ("Brasil",) # Declarando uma tupla apenas utilizando a virgula.

# Acesso direto 
# A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. 
# Contamos o índice de determinada sequência a partir do zero. 
# Exemplo 
frutas = ("maçã", "laranja", "uva", "pera",) 
print(frutas[0]) # maçã 
print(frutas[2]) # uva 

# Índices negativos 
# Sequências suportam indexação negativa. A contagem começa em -1. 
# ele começa a contar do ultimo elemento.
frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[-1]) # pera 
print(frutas[-3]) # laranja 

# Tuplas aninhadas 
# Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que 
# armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e 
# acessar informando os índices de linha e coluna.
# Exemplo 
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0]) # (1, "a", 2) 
print(matriz[0][0]) # 1 
print(matriz[0][-1]) # 2 
print(matriz[-1][-1]) # "c"

# Fatiamento
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores 
# de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar
# o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
# Exemplo 
# Semelhante a lista temos um start, um step e um stop.
tupla = ("p", "y", "t", "h", "o", "n",) 

print(tupla[2:]) # ('t', 'h', 'o', 'n')
print(tupla[:2]) # ('p', 'y')
print(tupla[1:3]) # ('y', 't')
print(tupla[1:3]) # ('y', 't')
print(tupla[0:3:2]) # ('p', 't')
print(tupla[::]) # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) # ('n', 'o', 'h', 't', 'y', 'p')

# Iterando a tupla é igual a lista 
carros = ("Onix", "Tracker", "Corolla",)

for carro in carros:
    print(carro)

# Enumerate com Tupla 
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Métodos da classe tuple
# Por se imutável a tupla tem bem menos métodos que a lista veja exemplos.

# count
# Contar quantos elementos tem em uma tupla.
cores = ("vermelho", "azul", "verde", "azul",)

print(cores.count("vermelho")) # 1 
print(cores.count("azul")) # 2
print(cores.count("verde")) # 1 

# index 
# Saber em qual opção o objeto está ocupando na tupla.
linguagens = ("python", "js", "c", "java", "csharp",) 

print(linguagens.index("java")) # 3
print(linguagens.index("python")) # 0 

# len 
# quantos elementos tem na tupla.
print(len(linguagens)) # 5