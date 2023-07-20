#----------------------#
# VARIÁVEIS PRIMITIVAS #
#----------------------#

var1 = -7 # inteiro
var2 = 1.5 # float
var3 = True # booleano
var4 = "texto" # string

# DESCOBRINDO O TIPO DA VARIÁEL #

print (type(var1)) # type permite ver o tipo da variável
print (type(var2)) # type permite ver o tipo da variável
print (type(var3)) # type permite ver o tipo da variável
print (type(var4)) # type permite ver o tipo da variável

# OPERADORES ARITMÉTICOS #

print (1 + 1) # adição
print (1 - 1) # subtraçção
print (1 * 1) # multiplicação
print (1 / 1) # divisão
print (1 ** 1) # potenciação
print (1 // 1) # divisão inteira
print (1 % 1) # resto de divisão

# OPERADORES RELACIONAIS #

print (1 > 2) # maior que
print (1 < 2) # menor que
print (1 >= 2) # maior e igual a
print (1 <= 2) # menor e igual a
print (1 == 2) # é igual a
print (1 != 2) # é diferente de

#-------------------------#
# ENTRDE E SAÍDA DE DADOS #
#-------------------------#

nome = input("Qual o seu nome: ") # input capta uma entrada de dado
idade = input("Qual a sua idade: ") # input capta uma entrada de dado
print ("Olá", nome,", sua idade é", idade) # print apresenta um dado

#----------------------#
# TIPAGEM DE VARIÁVEIS #
#----------------------#

n1 = int(input("Digite um número: ")) # variável de tipo inteiro
n2 = int(input("Digite outro número: ")) # variável de tipo inteiro
soma = n1 + n2 # somando valores de variáveis
print("A soma é", soma) # primeiro método
print("A soma de {} e {} é {}".format(n1,n2.soma)) # segundo método
print(f"A soma é{soma}") # terceiro método

#--------------------#
# DESVIO CONDICIONAL #
#--------------------#

# EXEMPLO 1 #

idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Maior de idade")
else:
    print("Menor de idade")

print("Programa Encerrado")

# EXEMPLO 2 #

aluno = str(input("É aluno? [s/n]: ")) # variável do tipo string

if aluno == 's':
    print("Bem-vindo aluno")
elif aluno == 'n':
    print("Bem-vindo convidado")
else:
    print("Opção inválida")

print("Programa Encerrado")

#---------------------------#
# LAÇO DE REPETIÇÃO - WHILE #
#---------------------------#

cont = 1
num = int(input("Digite um número: "))
while cont <= num:
    print(cont)
    cont += 1 # mesmo que : cont = cont + 1
print("Programa encerrado")

#-------------------------#
# LAÇO DE REPETIÇÃO - FOR #
#-------------------------#

for i in range(0, 7):
    print(i) # não imprime o último número
print("Fim")

for i in range(1, 101, 2):
    print(i) # não imprime o último número
    if i==11:
        break # força o encerramento do laço
print("Fim")

#------------------------#
# IMPORTANDO BIBLIOTECAS #
#------------------------#

import math # usamos o import para importar
print(math.sqrt(25))

#----------------------------#
# ESTRUTURA DE DADOS - ARRAY #
#----------------------------#

# Criando e acessando um ado do ARRAY(Lista) #

nomes = ['Amanda','Bruno','Camila','Davi','Davi']
print(nomes[1])
print(nomes[3])

# Métodos de um ARRAY(Lista) #

nomes.cont('Camila') # conta a quantidade do item
nomes.index('Davi') # mostra o index do item
nomes.append('João') # adciona um item
nomes.reverse() # inverte a lista(de traz para frente)
nomes.sort() # ordena a lista(menor maior ou primeira letra)
