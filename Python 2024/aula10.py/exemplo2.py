
numero1 = 5
numero2 = 8
numero3 = 10
numero4 = 20
if numero2 > numero1:
    #variavel auxiliar recebe o numero 2
    auxiliar = numero1
    #numero2 recebe o numero 1
    numero2 = numero1
    #numero 1 recebe a varivel auxiliar 
    numero1 = auxiliar 

    print(numero1)
    print(numero2)

numero3,numero4 = numero4 , numero3

print(numero3)
print(numero4)
