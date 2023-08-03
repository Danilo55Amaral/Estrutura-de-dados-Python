# Funções Parte 2 

# Parâmetros especiais
# Por padrão, argumentos podem ser passados para uma função Python 
# tanto por posição quanto explicitamente pelo nome. Para uma melhor 
# legibilidade e desempenho, faz sentido restringir a maneira pelo qual 
# argumentos possam ser passados, assim um desenvolvedor precisa apenas 
# olhar para a definição da função para determinar se os itens são passados 
# por posição, por posição e nome, ou por nome.

# Positional only 
# Neese tipo os parâmtros => modelo, ano e placa, é obrigatório passar sem o 
# parâmetro nomeado, após o / podemos passar parâmetros nomeados, no caso 
# fica a critériodo do desenvolvedor passar ou não após o /

def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # Válido 

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # Inválido

# Keyword only 
# Nessa versão utilizamos apenas parâmentros nomeados, utilizamos o * no início.

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # Válido

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
combustivel="Gasolina") # Inválido

# Keyword and positional only (Híbrido)
# Antes do / é passado por os parâmetros posição e após o * é passado parâmetros nomeados.

def criar_carro(modelo, ano, placa, /, *,  marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", 
combustivel="Gasolina") # Válido 

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", 
motor="1.0", combustivel="Gasolina") # Inválido

# Objetos de primeira classe 
# Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos 
# de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro
# para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc)
# e usar como valor de retorno para uma função (closures).
# Exemplo 
def somar(a, b):
    return a + b 

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) 
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20 

# Note que eu passei a função somar e não precisei executar ela abrindo e fechando parenteses
# apenas passei o nome da função, eu só precisei passar os parâmetros em funcao(a, b), extendemos 
# o comportamento da função somar. Note que eu consigo passar uma função como terceiro argumento 
# da função exibir_resultado. Posso fazer isso com várias funções diferentes. 
def somar(a, b):
    return a + b 

def subtrair(a, b):
    return a - b 

def test(a, b):
    return a*2 + b*3 

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) 
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20 
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 - 10 = 0 
exibir_resultado(10, 10, test) # O resultado da operação é 50

# Também dá para fazer isso esse apontamento da função atribuindo uma váriável.
op = somar 
print(op(1,23))

# Note que em Python a função se comporta como um objeto. 

# Escopo local e escopo global 
# Python trabalha com escopo local e global, dentro do bloco da função é local. 
# Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método 
# terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave 
# global, que informa ao interpretador que a varável que está sendo manipulada no escopo
# local é global. Essa NÂO é uma boa prática e deve ser evitada.

# Exemplo de variável com escopo global, note que ela está fora da função.
# Note que para utilizar essa variável de dentro da função é necessário utilizar o global.
salario = 2000 

def salario_bonus(bonus):
    global salario 
    salario += bonus 
    return salario 


novo_salario = salario_bonus(500) # 2500
print(novo_salario)

# Outro exemplo 
# Quando estamos utilizando o argumento por referência que é mutável é necessário criar uma 
# Cópia dele, para que ele não altere a referência externa. 
salario = 2000 

def salario_bonus(bonus):
    global salario 

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus 
    return salario 


lista = [1]
novo_salario = salario_bonus(500) # 2500
print(novo_salario)
print(lista)