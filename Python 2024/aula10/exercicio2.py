'''faça um programa que gera 4 numeros aleatorios entre 20 e 50 e depois os ordena em forma decrescente'''
import random

numero1 = random.uniform(20,50)
numero2 = random.uniform(20,50)
numero3 = random.uniform(20,50)
numero4 = random.uniform(20,50)

print(f"numeros gerados: {numero1:.2f},{numero2:.2f}, {numero3:.2f}, {numero4:.2f}")

for i in range(5):
    if numero1<numero2:
        numero1, numero2 = numero2,numero1
    if numero1<numero3:
        numero1, numero3 = numero3,numero1
    if numero1< numero4:
        numero1,numero4 = numero4,numero1
    if numero2<numero3:
        numero2,numero3 = numero3 =numero2
    if numero2<numero4:
        numero2,numero4 = numero4,numero2
    if numero3<numero4:
        numero3,numero4 = numero4,numero3


print(f"numeros ordenados decrescentes:{numero1:.2f}, {numero2:.2f},{numero3:.2f}, {numero4:.2f}")