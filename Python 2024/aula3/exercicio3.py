#faça um programa que calcule o tamanho do sapato de um cachorro sabendo que será o dobro do tamanho da coleira.
#calcular tambem o tamanhando da funcinheira que é o triplo da coleira 
#programa deve pedir o tamanho da coleira do cachorro do usuario e retornar o tamanho do sapato e da fucinheira.

print("vamos calcular o tamanho da coleira do seu cão! ")
coleira = float(input("qual o tamanho da coleira?"))
sapatinho = coleira*2
fucinheira = sapatinho*3 
print("os tamanhos do sapatinho e da fucinheira:")
print(f"o tamanho do sapato é :{sapatinho:.2f} ")
print(f"o tamanho da fucinheira é:{fucinheira:.2f} ")
