# Criação e acesso aos dados.

# Criando Listas 
# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 
# Podemos criar listas utilizando o construtor list, a função range ou colocando 
# valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis,
# portanto podemos alterar seus valores após a criação. 

# Exemplo 
frutas = ["laranja", "maca", "uva"] # Forma mais comum e utilizada para declarar uma lista.
print(frutas)

frutas = [] # Também pode ser declarada uma lista vazia.
print(frutas)

letras = list("python") # Declarando com constructor list porém esse método ele não coloca um 
# objeto python por exemplo dentro, ele coloca uma lista em que cada letra é um elemento.
# esse tipo de constructor pede um argumento iterável. String é um elemento iteravel.
print(letras)

numeros = list(range(10)) # Aqui foi utilizada a função range que pega o 10 e cria uma série de 
# elementos de 0 a 9
print(numeros)

carro = ["Ferrari", "F8", 4500000, 2023, 29000, "Recife", True] # lista com vários tipos de dados 
print(carro)

# Acesso direto 
# A lista é uma sequência, portanto podemos acessar seus dados utilizando índices.
# Contamos o índice de determinada sequência a partir do zero.

# Exemplo  
frutas = ["maçã", "laranja", "uva", "pera"] 
print(frutas[0]) # maçã 
print(frutas[2]) # uva 

# Índices negativos 
# Sequências suportam indexação negativa. A contagem começa em -1 que vai pegar sempre o 
# ultimo elemento da lista. 
# Exemplo 
print(frutas[-1]) # pera 
print(frutas[-3]) # laranja 

# Listas aninhadas 
# Listas podem armazenar todos os tipos de objetos em Python, portanto podemos ter listas 
# que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas, Matrizes),
# e acessar informando os índices de linha e coluna.
# Exemplo  
# Nesse exemplo temos uma matriz 3 x 3 ==> 3 linhas por 3 colunas.
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2 
print(matriz[-1][-1]) # "c" 

# Fatiamento 
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma 
# sequência. Para isso basta passar o índice inicial e/ou final para acesar o conjunto. 
# Podemos ainda informar quantas posições o cursor deve "pular" no acesso.
# Exemplo 
lista = ["p", "y", "t", "h", "o", "n"]

# A partir do índice 2, como não passei nada após o : ele vai pegar todo o resto da lista.
lista[2:] # ["t", "h", "o", "n"]

# O oposto antes do : não passei nada então ele vai exibir do início, após o : eu informei 2
# esse será índice de parada. 
lista[:2] # ["p", "y"] 

# índice inicial e índice final. 
lista[1:3] # ["y", "t"]

# Eu usei o terceiro parâmetro que é o intervalo, no caso aqui ele conta no intervalo de 2 em 2
lista[0:3:2] # ["p", "t"]

# Esse caso é um caso de excessão onde tudo é colocado como vazio, é utilizado para fazer uma 
# cópia exata da lista.
lista[::] # ["p", "y", "t", "h", "o", "n"]

# Trazendo uma cópia da lista invertida, é conhecido como técnica de espelhamento.
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

# OBS- lembre que o 0 é um índice.

# Iterar listas
# A forma mais comum para percorrer os dados de umalista é utilizando o comando for.

# Exemplo 
carros = ["Tesla", "Camaro", "Onix"]

for carro in carros:
    print(carro)

# Função enumerate 
# As vezes é necessário saber qual o índice do objeto dentro do laço for.
# Para isso podemos usar a função enumerate.
# Exemplo 
# Quando utilizamos o enumerate passamos o iterável para esse método, e ele
# vai retornar dois valores um é o contator que no exemplo foi indice, esse contador 
# começa a partir do índice zero, e o outro é o nome que damos ao item da iteração.

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de listas
# A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova 
# lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando
# alguma modificação nos elementos de uma lista existente.

# Exemplo 
# Filtro versão 1 
# Nesse exemplo pegamos todos os números pares da lista numeros, para isso criamos uma lista vazia 
# chamada pares onde vamos armazenar os itens pares, em seguida eu faço uma iteração em cima da lista 
# numeros, em seguida eu utilizei um if para verificar se o número é par, se a confição for true ele vai 
# pegar o elemento e fazer um append que adiciona o valor onde queremos.

numeros = [1, 30, 21, 2, 9, 65, 34] 
pares = [] 

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


print(pares)

# O Python também consegue fazer isso de maneira ainda mais prática utilizando Compreensão de listas
# temos a mesma lista de números, em seguida a lista pares com a instrução de Compreensão, vamos analisar
# ======> [numero for numero in numeros if numero % 2 == 0] primeira parte ==> numero => é o retorno que é 
# o que irá compor essa lista que será gerada, a segunda parte ==> for numero in numeros => é a iteração, só 
# as duas primeiras partes são obrigatórias, a terceira parte ==> if numero % 2 == 0 => utilizamos por que 
# queremos fazer um filtro e por isso utilizamos o if

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Modificando valores versão 1
# Exemplo
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [] 

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

# Modificando valores versão 2
# Exemplo utilizando Compreensão
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)