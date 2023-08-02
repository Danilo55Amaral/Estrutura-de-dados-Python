# Funções parte 1 

# Estudo aprofundado sobre funções

# O que são funções ? 
# Função é um bloco de código identificado por um nome e pode receber 
# uma lista de parâmetros, esses parâmetros podem ou não ter valores 
# padrões. Usar funções torna o código mais legível e possibilita o 
# reaproveitamento de código. Programar baseado em funções, é o mesmo 
# que dizer que estamos programando de maneira estruturada.

# A palavra reservada para funções no Python é def
# Utiliza a mesma estrutura de blocos utilizadas nas codicionais, iniciando o 
# Bloco com : e tudo que estiver identado para dentro da estrutura faz parte do 
# escopo do Bloco.

# Exemplo

# Essa função não possue nenhum argumento(parametro).
def exibir_mensagem():
    print("Olá mundo!")

# Nessa segunda função existe um parâmetro que chamei de nome.
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!") 

# Nessa terceira função existe um parâmtro com um valor padrão 
# caso não seja passado nenhum valor.
def exibir_mensagem_3(nome="Bill"):
    print(f"Seja bem vindo {nome}!")

# Só declarar a função não é o suficiente para que ela seja executada 
# é necessário chamar a função. Se a função possuir parametros é necessário 
# passar esses argumentos quando a função estiver sendo chamada.
exibir_mensagem()  # Olá mundo!
exibir_mensagem_2(nome="Mark") # Seja bem vindo Mark!
exibir_mensagem_3() # Seja bem vindo Bill!
exibir_mensagem_3(nome="Chappie") # Seja bem vindo Chappie!

# Retornando valores 
# Para retornar um valor, utilizamos a palavra reservada return. Toda função 
# Python retorna None por padrão. Diferente de outras linguagens de programação, 
# em Python uma função pode retornar mais de um valor.

# Exemplo 
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1 
    sucessor = numero + 1 

    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # 64 
print(retorna_antecessor_e_sucessor(10)) # (9, 11)

# Note que na minha função que tem mais de um retorno ele retorna os dados 
# dentro de uma tupla, isso por que a tupla é uma estrutura imutável. 

# Argumentos nomeados
# Funções também podem ser chamadas usando argumentos nomeados da forma 
# chave=valor.

# Exemplo 
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Forma sequêncial de se chamar, nesse caso pode haver erros invertendo alguns valores e 
# o Python não percebe se for o caso.
print(salvar_carro("Fiat", "Palio", 1999, "ABC-1234")) 

# Aqui como estamos usando argumentos nomeados é mais difícil para o desenvolvedor deixar 
# passar algum erro e acabar confundindo marca com modelo por exemplo.
print(salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234"))

print(salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}))

# Args e Kwargs 
# Podemos combinar parâmetros obrigatórios com args e Kwargs. Quando esses são definidos 
# (*args e **Kwargs), o método recebe os valores como tupla e dicionário respectivamente.
# *args os valores serão renderizados como uma tupla e **kwargs os valores vem em um dicionário de dados.
# Exemplo 
def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista) 
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 25 de Setembro de 2023",
    "Zen of Python", 
    "Beautiful is batter than ugly.",
      autor="Tim Poters",
      ano=1999
)