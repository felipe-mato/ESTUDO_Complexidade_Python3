#1-)
def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result
#print(multiply_array([2, 4, 6])) #48

#Espaço: O(1) = O numero de saídas é sempre 1 numero só
#Tempo: O(n) = O numero de operações é proporcional ao numbero de entradas 
################################################################################

#2-)
# Os arrays têm sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            print(result)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return print('Result: ', result)


meu_array1 = [1, 2, 3, 4, 5]
meu_array2 = [5, 4, 3, 2, 1]
# multiply_arrays(meu_array1, meu_array2)

#Complexidade: O(n²) = entradas n operações  n²
################################################################
#3-)
def binary_search(numbers, target):
    # definir os índices
    start = numbers[0]
    end = len(numbers) - 1

    while start <= end: # os índices podem ser no máximo iguais, o início não pode ultrapassar o fim
        mid = (start + end) // 2 # encontro o meio
        print('mid: ',mid)

        if numbers[mid] == target: # se o elemento do meio for o alvo, devolve a posição do meio
            return mid
        
        if target < numbers[mid]: # se o elemento for menor, atualiza o índice do fim
            end = mid - 1
            print('end agora é :', end)
        if target > numbers[mid]: # caso contrário, atualiza o índice do inicio
            start = mid + 1
            print('start agora é: ', start)
    
    return -1 # Não encontrou? Retorna -1

numbers = [0,1,2,3,4,5,6,7,8,9]
target = 8

result = binary_search(numbers, target)
# print(f"Elemento encontrado na posição: {result}")

# #Complexidade: O(log n) = n entradas n/2 operações 
################################################################
#4-)
def search_in_arrays(array1, array2):
    for i in array1:
        print('i agora é: ', i)
        start = 0 
        end = len(array2) - 1
        while start <= end:
            mid = (start + end) // 2
            print('mid é: ', mid)

            if array2[mid] == i:
                print('encontrou ',array2[mid],' na posição: ',mid,' do array2')
                break

            if i < array2[mid]:
                end = mid - 1
                print('end agora é: ', end)
            else:
                start = mid + 1
                print('start agora é: ', start)
        else:
            print('Não encontrado em array2')
    return 'DONE'

array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'x', 'u', 'v', 'w']
array2 = ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'x', 'u', 'v', 'w']

result = search_in_arrays(array1, array2)
# print(result)

#Complexidade: O(n * log m) = n entradas * m entradas/2

#A complexidade desse código é O(n * log m), onde "n" é o tamanho do array1 e
# "m" é o tamanho do array2. Para cada elemento do array1, o algoritmo realiza 
# uma busca binária em array2, que tem um tamanho de "m".

#A busca binária tem complexidade logarítmica (O(log m)) porque a cada iteração do loop
# ela reduz o intervalo de busca pela metade. Como está fazendo isso para cada elemento 
# em array1, a complexidade total é O(n * log m).
##############################################################################################
#4-)
def search_in_arrays2(array1, array2):
    for i in array1:
        print('i agora é: ', i)
        found = False
        for index, element in enumerate(array2):
            if element == i:
                print('encontrou na posição: ', index)
                found = True
                break
        if not found:
            print('Não encontrado em array2')
    return 'DONE'

array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'x', 'u', 'v', 'w']
array2 = ['z', 'x', 'u', 'v', 'w', 'a', 'b', 'c', 'd', 'e', 'f']

result = search_in_arrays(array1, array2)
print(result)

#Complexidade Tempo: O(n * m) = n tamanho do array1 m tamanho do array2. 
#Para cada elemento em array1 ela percorre todo o array2 em busca do elemento correspondente
#Portanto, o tempo de execução será proporcional ao produto dos tamanhos dos dois arrays.