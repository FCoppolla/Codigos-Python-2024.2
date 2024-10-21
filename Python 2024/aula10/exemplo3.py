import random

#gerando 4 numeros aleatorios e armazenando em uma lista
numeros =[random.randint(20,50) for i in range(4)]

#exibindo numeros gerados
print(f"numeros gerados: {numeros}")

#ordenando os numeros com a função sort
numeros.sort()
numeros.reverse()

print(f" numeros ordenados {numeros}")