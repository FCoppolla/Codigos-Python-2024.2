'''faça um programa que receba 1 numero e diga se ele é primo ou não'''
#peça um numuero ao usuario
numero = int(input("entre com um numero\n >"))
#uso de uma variavel de apoio que definira se um numero é primo ou não
primo = True
#faço um loop que vai do numero 2 até o numero antecessor a ele 
for i in range (2,numero):
#se um numero fpr divisivel por qualquer numero sem ser o 1 ou ele mesmo, primo será falso  
    if(numero%i == 0):
        primo = False
#se o mumero for falso é porque ele e divisivel por mais algum numero sem ser 1 e ele mesmo 
if (primo == False):
    print("esse numero não é primo")

else:
    print("esse numero é um  primo")