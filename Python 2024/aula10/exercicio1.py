'''faça um programa que gera 3 numeros aleatorios float e voce tem 1 tentativa para descobrir qual '''

import random

numero1 = random.uniform (1, 15)
numero2 = random.uniform(1 , 15)
numero3 = random.uniform(1 , 15)

escolha = float(input("o sistema tem 3 numeros, qual dos e voce acha que é maior?\n > "))

if escolha == numero1 and numero1>numero2 and numero1>numero3:
    print("voce acertou ! ")

elif escolha == numero2 and numero2>numero1 and numero2>numero3:
    print("voce acertou ! o segundo numero era maior ")

elif escolha == numero3 and numero3>numero1 and numero3>numero2:
    print("voce acertou ! o numero 3 era o maior ")
else: 
    print("voce errou !  ")

print("os numeros eram:")
print(f"{numero1:.2f}")
print(f"{numero2:.2f}")
print(f"{numero3:.2f}")