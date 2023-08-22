1-) Conceito

O(n) = 1 entrada operação 1 saída
       10 entradas 10 saídas

0(1) = 1 entrada 1 saída
       10 entradas 1 saída
       100 entradas 1 saída

O(log n) = 2 entradas 1 operação 
           10 entradas 5 operações
           20 entradas 10 operações

O(n * m) = n 2_entradas * m 2_entradas : 4 operações
           n 4_entradas * m 4_entradas : 8 operações
           n 10_entradas * m 10_entradas : 100 operações
           n 100_entradas * m 100_entradas : 1000 operações

O(n * log m) = n 2_entradas * m 2_entradas/2 : 2 operações
               n 10_entradas * m 10_entradas/2 : 50 operações
               n 100_entradas * m 100_entradas/2 : 500 operações

Se falamos em ordem de complexidade sem especificar se é de tempo ou de memória, assuma que é de tempo!

Quando se trata de esoaço, analisamos o espaço EXTRA que utilizamos.
Computamos o espaço que a função ou algoritmo vai usar, ALÉM da entrada

Exemplos -)
1-) O(1) & O(n)
def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result

#Espaço: saída = O(1) = O numero de saídas é sempre 1 numero só
#Tempo: opreações = O(n) = O numero de operações é proporcional ao numbero de entradas 

2-) O(n²)
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result

meu_array1 = [1, 2, 3, 4, 5] #Os arrays têm sempre o mesmo tamanho
meu_array2 = [5, 4, 3, 2, 1]
multiply_arrays(meu_array1, meu_array2)

Para o exemplo acima, no qual as duas entradas continham 5 elementos, foram necessárias 25 operações para obtermos o resultado final!

#O(n²) = entradas n operações  n²

3-) O(log n)
def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2 # encontro o meio
        if numbers[mid] == target:
            return mid
        if target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 'NOT_FOUND'
numbers = [2, 3, 4, 10, 40]
target = 40
result = binary_search(numbers, target)
print(f"Elemento encontrado na posição: {result}")


Foco -)
* A Ordem de Complexidade diz respeito à taxa de crescimento do tempo de execução (ou espaço de memória ocupado) de um algoritmo, na medida em que aumentamos o tamanho da sua entrada;

O(1) -) 
(constante), quando o tempo de execução do algoritmo independe do tamanho da entrada;

O(n) -)
(linear) quando a taxa de crescimento em seu tempo de execução é linear: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 2 vezes;

O(n²) -)
(quadrática) quando a taxa de crescimento do tempo de execução do algoritmo é quadrática: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 4 (ou 2²) vezes;

O(n³) -)
(cúbica) quando a taxa de crescimento do tempo de execução do algoritmo é cúbica: se aumentamos a entrada em 2 vezes, aumentamos o tempo de execução em 8 (2³) vezes.

O(log n) -) 
quando a taxa de crescimento do tempo de execução do
algorimto é reduzida pela metade: Se temos 50 entradas, faremos 25 operações

O(n * m) -)
(polinomial) quando a taxa de crescimento do tempo de execução do algoritmo é proporcional ao produto dos tamanhos das entradas: se aumentamos uma entrada em 2 vezes e a outra entrada em 3 vezes, o tempo de execução aumenta em 6 vezes (2 * 3).

O(n * log m) -)
(quasilinear) quando a taxa de crescimento do tempo de execução do algoritmo é proporcional a 
n * m/2 : se aumentamos a entrada em 2 vezes e a outra entrada permanece igual, o tempo de execução aumenta em um valor aproximado a "2 * log 2" vezes.