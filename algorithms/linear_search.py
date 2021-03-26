num = int(input('Digite um número: '))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(len(lista)):
	if lista[i] == num:
		print(f'O número {num} está na posição de índice {i}')
		break
	elif i == (len(lista) - 1):
		print(f'O número {num} não existe na lista')
