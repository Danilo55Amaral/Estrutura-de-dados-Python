# Métodos da Classe list

# Método append 
# Esse método é utilizado para inserir um novo elemento na lista.
# Exemplo 
lista = [] 

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

# Método clear 
# Esse método é utilizado para limpar a lista. 
# Exemplo 
lista = [1, "Python", [40, 30, 20]] 
print(lista) # [1, "Python", [40, 30, 20]] 

lista.clear() 
print(lista) # [] 

# Método copy 
# Esse método copia a lista porém com uma instância diferente 
# não é a mesma lista é uma copia como o nome já sugere.
# Exemplo 
lista = [1, "Python", [40, 30, 20]] 
l2 = lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]
print(id(l2), id(lista)) # Utilizando o método id eu consigo analisar o id das duas listas e 
# comprovar que embora sejam iguais não são a mesma. 

# Note que se eu alterar uma lista a outra não será alterada pois não são a mesma lista. 
l2[0] = 2 

print(l2) # [2, "Python", [40, 30, 20]]
print(lista) # [1, "Python", [40, 30, 20]]

# Método count
# Esse método é utilizado para contar quantas vezes um determinado objeto 
# aparece dentro da lista.
# Exemplo 
cores = ["vermelho", "azul", "verde", "azul"] 

print(cores.count("vermelho")) # 1
print(cores.count("azul")) # 2 
print(cores.count("verde")) # 1 

# Método extend 
# Esse método é utilizado para juntar listas, nesse método é passado o iterável, ele pega 
# a lista original e coloca tudo que for passado como lista dentro de extends.
# Exemplo 
linguagens = ["python", "js", "c"] 
print(linguagens) # ["python", "js" "c"] 

linguagens.extend(["java", "csharp"]) 
print(linguagens) # ["python", "js", "c", "java", "csharp"]

# Método index 
# Esse método retorna qual o index em que o elemento aparece a primeira vez.
# Exemplo 
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java")) # 3 
print(linguagens.index("python")) # 0 

# Método pop 
# Uma lista aqui já vem organizada como uma pilha, em uma pilha o ultimo 
# elemento que entrou na pilha é por padrão o primeiro que vai sair. Quando 
# utilizamos o pop ele remove o ultimo elemento que foi adicionado.
# Exemplo
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop()) # csharp
print(linguagens.pop()) # java 
print(linguagens.pop()) # c 

# Também é possivel passar para o pop o índice que quero remover.
print(linguagens.pop(0)) # python 

# Método remove 
# Esse método é uma outra forma de tirar elementos da lista porém diferente do pop 
# ao invés de passar o índice é passado o proprio objeto que queremos remover. 
# Exemplo
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")
print(linguagens) # linguagens = ["python", "js", "java", "csharp"]

# Método reverse
# Esse método pega a lista e faz o espelhamento exibindo ao contrário.
# Exemplo 
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse() 
print(linguagens) # ['csharp', 'java', 'c', 'js', 'python']

# Método sort 
# Esse método vai ordenar a lista. 
# Exemplo 
# A ordenação padrão ordena em ordem alfabetica. 
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort())

# Posso passar o reverse que vai ordenar de trás para frente.
print(linguagens.sort(reverse=True))

# Posso passar o key passando o lambda que é uma função anonima que para cada item ele 
# executa o seguinte código => x: len(x) onde o x será cada elemento da lista,  o len 
# vai contar quantos items cada elemento tem e vai ordenar do menor para o maior.
print(linguagens.sort(key=lambda x: len(x)))
      
# Também da para utilizar o key e o reverse juntos de uma vez.      
print(linguagens.sort(key=lambda x: len(x), reverse=True))

# Método len 
# Esse método ele mede o tamanho das cosias ou seja a quantidade de elementos.
# Exemplo 
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens)) # 5 

# Método sorted 
# Esse método também serve para ordenar iteráveis. Por se tratar de uma função 
# é necessário passar qual será o iterável que será ordenado, em seguida eu posso 
# fazer assim como no método sort.
# Exemplo 
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x))) # ['c', 'js', 'java', 'python', 'csharp']
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['python', 'csharp', 'java', 'js', 'c']
print(sorted(linguagens)) # ['c', 'csharp', 'java', 'js', 'python']