'''utilizando o for, faça i, programa que peça 5 numeros ao usuario e no fim de a sua soma'''
soma = 0 
for i in range(5):
    numero =int(input("digite um numero\n >"))

    soma += numero
print(f"sua soma é:{soma}")