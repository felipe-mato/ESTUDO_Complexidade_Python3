"""
PROBLEMA:
> Dada uma lista de números de tamanho 'n', substitua cada número 
pelo maior valor ṕossível que estiver à sua direita
> Caso não exista número maior à direita, mantenha o valor original
"""

entrada = [2, 1, 2, 3, 0, 5, 1, 2, 3]
#saída:   [5, 5, 5, 5, 5, 5, 3, 3, 3]

# Primeira abordagem
def number_substitution1(numbers):
    saida = []
    for i, original_number in enumerate(numbers): # Enumerate é uma função do python que vai fornecer o index e o elemento
        # print(i, original_number) #Para visualização
        right_max = original_number

        for j, candidate in enumerate(numbers):
            if j > i and candidate > right_max:
                right_max = candidate

        numbers[i] = right_max

        saida.append(numbers[i])
    return saida
#print(number_substitution1(entrada))

"""
Descrição:

Complexidade de tempo: O(n²) ou O(n^2) => n * n => n interações no ofr externo, para cada uma
fazemos n interações no for interno

Complexidade de espaço: 0(1) => Usamos um numero constante de variaveis/memóriaind
independente da entrada

Observação: estamos percorrendo todos os elementos do array, independente de qual
numero esta sendo analisado. Isso desperdiça tempo e memória pois os numeros à esquerda
do elemento em analise não nos interessa, apenas os numeros à direita
"""
########################################################################################################

# Segunda abordagem
def number_substitution2(numbers):
    saida = []
    for i, original_number in enumerate(numbers):
        right_max = original_number

        for candidate in (numbers[i:]): # [i:] = indica que o array vai ser percorrido a partir de i até o final
            if candidate > right_max: # Assim podemos descartar o j e o enumerate
                right_max = candidate

        numbers[i] = right_max

        saida.append(numbers[i])
    return saida
# print(number_substitution2(entrada))

"""
Descrição: Dois loops com slice

Complexidade de tempo: O(n²) ou O(n^2) => Para cada iteração do for externo, temos um número diferente de interações no for interno
= n + (n-1) + (n-2) + (n-3) + ... + 1
Soma de PA (formula)
= (n + 1) * n / 2
= (n^2 + n) / 2
= 0(n^2)

Complexidade de espaço: O(n) => O slicing está criando uma nova lista, que no pior caso tem n(valor da entrada) elementos

Observação: A complexidade de tempo ficou igual, enquanto a complexidade de espalo aumentou, pois o slicing que usamos gera um novo array
Assim, um nova constante(array gerado pelo sliging) será criado para cada valor do array recebido na entrada
"""
##############################################################################################################

# Terceira abordagem
def number_substitution3(numbers):
    saida = []
    for i, original_number in enumerate(numbers):
        right_max = original_number

        for j in range(i, len(numbers)): # Com range(i, len(numbers)) percorremos o array apenas da posição i até o final
            candidate = numbers[j] # candidate vai ser o numbers na posição j (primeiro index do array que esta sendo analisado no range)
            if candidate > right_max:
                right_max = candidate

        numbers[i] = right_max

        saida.append(numbers[i])
    return saida
# print(number_substitution3(entrada))

"""
Descrição: Dois loops com range

Complexidade de tempo: O(n²) => A complexidade de tempo se mantem igual a da solução anterior

Complexidade de espaço: 0(1) => Usamos um numero constante de variaveis/espaço/memória extra

Observação: Mantemos a complexidade de tempo, mas reduzimos a complexidade de espaço substituindo
o splice pelo range
"""
###########################################################################################################

# Quarta abordagem
def number_substitution4(numbers):
    if len(numbers) == 0:
        return
    saida = []
    last_pos = len(numbers) - 1
    right_max = numbers[last_pos]
    for i in range(last_pos, -1, -1): #Com essa sintaxe range anda de trás pra frente
        if right_max > numbers[i]: #Se maximo_adireita for maior que numbers na posição analisada
            numbers[i] = right_max #numbers[i] recbe o valor de right_max
            saida.append(numbers[i])
        else:
            right_max = numbers[i] #Caso contrário, right_max recebe o valor de numbers[i]
            saida.append(right_max)
    return print(saida)
# number_substitution4(entrada)

"""
Descrição: Range de trás pra frente (Loop reverso)

Complexidade de tempo: O(n) => Andamos a lista de trás pra frente, passando por n elementos
para cada elemento fazemos um numero constante de operações

Complexidade de espaço: O(1) => A quantidade de variaveis é sempre a mesma, independente do tamanho
da entrada

Observação:
"""


#TESTES
def test_number_substitution1():
    entrada = [2, 1, 2, 3, 0, 5, 1, 2, 3]
    number_substitution1(entrada)
    assert  entrada == [5, 5, 5, 5, 5, 5, 3, 3, 3]

def test_number_substitution2():
    entrada = [2, 1, 2, 3, 0, 5, 1, 2, 3]
    number_substitution2(entrada)
    assert  entrada == [5, 5, 5, 5, 5, 5, 3, 3, 3]

def test_number_substitution3():
    entrada = [2, 1, 2, 3, 0, 5, 1, 2, 3]
    number_substitution3(entrada)
    assert  entrada == [5, 5, 5, 5, 5, 5, 3, 3, 3]

def test_number_substitution4():
    entrada = [2, 1, 2, 3, 0, 5, 1, 2, 3]
    number_substitution4(entrada)
    assert  entrada == [5, 5, 5, 5, 5, 5, 3, 3, 3]










