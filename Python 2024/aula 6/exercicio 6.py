# faça um programa que peça dois numeros e faça a operação com base no seguinte menu:
#1 = soma ; 2 = subtração ; 3 multiplicação ; 4 divisão


num1 = int(input("digite um numero:"))
num2 = int (input("digite mais um numero:"))


operação = int(input("escolha uma das operaçoes seguindo o menu\n 1 - soma \n 2 -subitração\n 3 - multiplicação\n 4 - divisão \n >"))

if (operação ==1):
    resposta = num1 + num2

if (operação ==2):
    resposta = num1 - num2

if (operação == 3):
    resposta = num1 * num2

if (operação == 4):
    resposta = num1 / num2


else:
    print(" \erro: divisivel por zero não reconhecido")


print (f"sua resposta é {resposta}")

