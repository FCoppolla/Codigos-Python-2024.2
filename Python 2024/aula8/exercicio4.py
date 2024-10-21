'''faça um programa que usando 'for' que peça 4 numeros e some apenas numeros impares '''

soma = 0
for i in range(4):   
    numero =int(input("digite um numero\n >"))
    if numero % 2 != 0:

        soma += numero

print(f"seu resultado é: {soma}")