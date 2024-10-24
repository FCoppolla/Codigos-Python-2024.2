'''apos a aventura da aula passada, o aventureiro resolveu treinar mais seu combate; faça uma simulação onde o aventureiro tem uma lista
[100, 20 ] onde 100 e a vida dele e 20 e o poder de ataque dele e a cada 7 segundos de treino, 
ele aumenta seu poder de ataque em +1 e com o limite maximo de 30 para o seu poder de ataque '''


lista = [100 , 20]

pda = lista[1]
import time
print("começando o treinamento")


while True:
    print(pda)
    time.sleep(1)
    pda += 1
    if pda >30 :
        break

    
print("o treino acabou...")

print(lista)