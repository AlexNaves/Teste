###### CAPA DE APRESENTAÇÃO #####
print('=-'*78)
print('Aluno: Rafael Novais de Miranda',' '*50,'Disciplina: AVANÇOS CIENTÍFICOS EM GENÉTICA E MELHORAMENTO DE PLANTAS I')
print('Professor: Vinicius Quintão Carneiro',' '*45,'Programa: Genética e Melhoramento de Plantas')
print('=-'*78)
print(' '*50, 'REO 01 - LISTA DE EXERCÍCIOS')
print('=-'*78)
print(' ')

##### Pacotes utilizados #####
import numpy as np

##### Número do exercício #####
print('EXERCÍCIO 01')

##### Questão 1.a #####
print('a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
print('Resposta:')
lista = [43.5, 150.30, 17, 28, 35, 79, 20, 99.07, 15]
vetor = np.array(lista)
print('Lista: {}'.format(lista))
print('Vetor: {}'.format(vetor))
print('O vetor é do tipo: {}'.format(type(vetor)))
print('-'*50)
print(' ')

##### Questão 1.b #####
print('b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print('Resposta:')
print('O vetor contém {} elementos.'.format(len(vetor)))
print('A média do vetor é {}'.format(np.mean(vetor)))
print('O valor máximo do vetor é {}'.format(max(vetor)))
print('O valor mínimo do vetor é {}'.format(min(vetor)))
print('A variância deste vetor é {}'.format(np.var(vetor)))
print('-'*50)
print(' ')

##### Questão 1.c #####
print('c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor da média deste.')
print('Resposta:')
media_vetor = np.mean(vetor)
novo_vetor = np.array((vetor-media_vetor)**2)
tipo_vetor = type(novo_vetor)
print(novo_vetor)
print(' ')
print('O vetor é do tipo: {}'.format(tipo_vetor))
print('-'*50)
print(' ')

##### Questão 1.d #####
print('d) Obtenha um novo vetor que contenha todos os valores superiores a 30.')
print('Resposta:')
print('O vetor que contém apenas valores superiores a 30: {}'.format(vetor[vetor>30]))
print('-'*50)
print(' ')

##### Questão 1.e #####
print('e) Identifique quais as posições do vetor original possuem valores superiores a 30')
print('Resposta:')
print('Vetor boleano indicando posições superiores a 30: {}'.format(vetor>30))
vetor_sup_30 = np.where(vetor>30)
print('As posições do vetor original que possuem valores superiores a 30 são: {}'.format(vetor_sup_30[0]))
print('-'*50)
print(' ')

##### Questão 1.f #####
print('f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
print('Resposta:')
prim = vetor [0]
quin = vetor [4]
ult = vetor [-1]
vetor_qf = [prim, quin, ult]
print('O vetor contendo os valores da primeira, quinta e última posição: {}'.format(vetor_qf))
print('-'*50)
print(' ')

##### Questão 1.g #####
print('g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações')
print('Resposta:')
it = 0
print('Considerando que o Python pondera a primeira posição sendo 0:')
for pos,valor in enumerate(vetor):
    it = it+1
    print('Iteração {} --> Na posição {} ocorre o valor {}'.format(it, pos, valor))
print('-'*50)
print(' ')

##### Questão 1.h #####
print('h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
print('Resposta:')
def somatorio_quadrado (vetor):
    somador = 0
    it = 0
    for el in vetor:
        print('Elemento: {}'.format(el))
        print('Somador: {}'.format(somador))
        somador = somador + el**2
        it = it + 1
        print('Iteração {} - Somatório: {}'.format(it, somador))
        print('_'*5)
        print(' ')
    return somador
print(vetor)
print(' ')
somatorio_quadrado(vetor)
print('-'*50)
print(' ')

##### Questão 1.i #####
print('i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
print('Resposta:')
valores = -1
print('Será realizado uma contagem até que o valor apresentado seja diferente de 3, começando pelo 0:')
while valores != 3:
    valores = valores + 1
    print(valores)
print('-'*50)
print(' ')

##### Questão 1.j #####
print('j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
print('Resposta:')
print('Sequência de valores: {}'.format(list(range(1, len(vetor), 1))))
print('-'*50)
print(' ')

##### Questão 1.h #####
print('h) Concatene o vetor da letra a com o vetor da letra j.')
print('Resposta:')
q1j = list(range(1, len(vetor), 1))
vetores_concatenados = np.concatenate((vetor, q1j), axis=0)
print(vetores_concatenados)
print('-'*50)
print(' ')


##### Número do exercício #####
print('EXERCÍCIO 02')

##### Questão 2.a #####
print('a) Declare a matriz abaixo com a biblioteca numpy.')
print(' '*50, '1 3 22')
print(' '*50, '2 8 18')
print(' '*50, '3 4 22')
print(' '*50, '4 1 23')
print(' '*50, '5 2 52')
print(' '*50, '6 2 18')
print(' '*50, '7 2 25')
print('Resposta:')
matriz = np.array([[1, 3, 22], [2, 8, 18], [3, 4, 22], [4, 1, 23], [5, 2, 52], [6, 2, 18], [7, 2, 25]])
print(matriz)
print('-'*50)
print(' ')

##### Questão 2.b #####
print('b) Obtenha o número de linhas e de colunas desta matriz')
print('Resposta:')
nl, nc = np.shape(matriz)
print('Número de linhas da matriz: {}'.format(nl))
print('Número de colunas da matriz: {}'.format(nc))
print('-'*50)
print(' ')

##### Questão 2.c #####
print('c) Obtenha as médias das colunas 2 e 3.')
print('Resposta:')
submatriz_col2 = matriz[:,1]
media_matriz_col2 = np.average(submatriz_col2)
print('Matriz considerando apenas coluna 2: {} e sua média é {}'.format(submatriz_col2, media_matriz_col2))
submatriz_col3 = matriz[:,2]
media_matriz_col3 = np.average(submatriz_col3)
print('Matriz considerando apenas coluna 3: {} e sua média é {}'.format(submatriz_col3, media_matriz_col3))
print('-'*50)
print(' ')

##### Questão 2.d #####
print('d) Obtenha as médias das linhas considerando somente as colunas 2 e 3')
print('Resposta:')

submatriz_l1 = matriz[0,[1,2]]
media_matriz_l1 = np.average(submatriz_l1)
print('A média da linha 1 considerando coluna 2 e 3: {}'.format(media_matriz_l1))


submatriz_l2 = matriz[1,[1,2]]
media_matriz_l2 = np.average(submatriz_l2)
print('A média da linha 2 considerando coluna 2 e 3: {}'.format(media_matriz_l2))
submatriz_l3 = matriz[2,[1,2]]
media_matriz_l3 = np.average(submatriz_l3)
print('A média da linha 3 considerando coluna 2 e 3: {}'.format(media_matriz_l3))
submatriz_l4 = matriz[3,[1,2]]
media_matriz_l4 = np.average(submatriz_l4)
print('A média da linha 4 considerando coluna 2 e 3: {}'.format(media_matriz_l4))
submatriz_l5 = matriz[4,[1,2]]
media_matriz_l5 = np.average(submatriz_l5)
print('A média da linha 5 considerando coluna 2 e 3: {}'.format(media_matriz_l5))
submatriz_l6 = matriz[5,[1,2]]
media_matriz_l6 = np.average(submatriz_l6)
print('A média da linha 6 considerando coluna 2 e 3: {}'.format(media_matriz_l6))
submatriz_l7 = matriz[6,[1,2]]
media_matriz_l7 = np.average(submatriz_l7)
print('A média da linha 7 considerando coluna 2 e 3: {}'.format(media_matriz_l7))
print('-'*50)
print(' ')

##### Questão 2.e #####
print('e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
print('Resposta:')

col_2 = (matriz[:, 1])
notas_menor5 = np.where(col_2<5)

print('As posições na matriz dos genótipos que possuem notas inferiores a 5 são: {}'.format(notas_menor5[0]))
bol_notas_menor5 = col_2<5

col_1 = (matriz[:, 0])
genotipos_notas_menor5 = col_1[bol_notas_menor5]
print('Os genótipos com notas inferiores a 5 são: {}'.format(genotipos_notas_menor5))
print('-'*50)
print(' ')

##### Questão 2.f #####
print('f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
print('Resposta:')
col_3 = (matriz[:, 2])
peso_maior21 = np.where(col_3>=22)
print('As posições na matriz dos genótipos que possuem peso de 100 grãos superior ou igual a 22: {}'.format(peso_maior21[0]))
bol_peso_maior21 = col_3>=22
col_1 = (matriz[:, 0])
genotipos_peso_maior21 = col_1[bol_peso_maior21]
print('Os genótipos com peso de 100 grãos superior ou igual a 22: {}'.format(genotipos_peso_maior21))
print('-'*50)
print(' ')

##### Questão 2.g #####
print('g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100grãos igual ou superior a 22.')
print('Resposta:')
print('As posições na matriz dos genótipos que possuem nota inferior ou igual a 4 são, {}, e as posições na matriz dos genótipos com peso de 100 grãos superior ou igual a 22: {}'.format(notas_menor5[0], peso_maior21[0]))
genotipos_q2g = col_1[bol_peso_maior21 & bol_notas_menor5]
print('Os genótipos com peso de 100 grãos superior ou igual a 22 e nota de severidade de doença inferior ou igual a 3: {}'.format(genotipos_q2g))
print('-'*50)
print(' ')

##### Questão 2.h #####
print('h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido. Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z". Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
print('Resposta:')
nl, nc = np.shape(matriz)
print(matriz)
print(' ')
print('Número de Linhas: {}'.format(nl))
print('Número de Colunas: {}'.format(nc))
###################################### NAO DEI CONTA #######################################################
print('-'*50)
print(' ')

##### Número do exercício #####
print('EXERCÍCIO 03')

##### Questão 3.a #####
print('a) Crie uma função em um arquivo externo (outro arquivo .py) para calcular a média e a variância amostral um vetor qualquer, baseada em um loop (for).')
print('Resposta:')
def funcao ()





# b) Simule três arrays com a biblioteca numpy de 10, 100, e 1000 valores e com distribuição normal com média 100 e variância 2500. Pesquise na documentação do numpy por funções de simulação.
# c) Utilize a função criada na letra a para obter as médias e variâncias dos vetores simulados na letra b.
# d) Crie histogramas com a biblioteca matplotlib dos vetores simulados com valores de 10, 100, 1000 e 100000.

########################################################################################################################
########################################################################################################################
########################################################################################################################

# EXERCÍCIO 04:
# a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro
# variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, apresente os dados e obtenha as informações
# de dimensão desta matriz.
# b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy
# c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas
# d) Apresente uma matriz contendo somente as colunas 1, 2 e 4
# e) Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.
# f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.
# g) Apresente os seguintes graficos:
#    - Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura
#    - Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.

########################################################################################################################
########################################################################################################################
########################################################################################################################