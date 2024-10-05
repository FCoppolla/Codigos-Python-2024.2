#faça um programa que diga se um número é par ou impar
#dica: para pegar o resto de uma divisão utilize "%"
#exemplo: o resto da divisão por 6 por 3 é 0 6%3 = 0 . o resto da divisão de 4 por 3 é 1 4%3 = 1

num = int(input("entre com um número para saber se é par ou impar?"))

if ( num % 2 == 0):
    print(f"o {num} é par!")

else:
    print(f"o {num} é impar")

       

