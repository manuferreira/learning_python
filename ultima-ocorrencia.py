# Retornar a última ocorrência do número solicitado, senão estiver na lista, retornar - 1
# count = -1
# for i in range... if... count +=1 (-1 +1 = 0)
# if count == -1: there's no occurence of the number
# else: the number is in the indice {count}

num = int(input('Digite um número: '))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]

count = 0

for i in range(len(lista)):
    if lista[i] == num:
        count+=1
    elif i == len(lista) - 1 and count == 0:
        print(-1)

if count > 0:
    print(f'A última ocorrência se encontra no índice {i}')
    
