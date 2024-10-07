#faça um programa que diga se um numero é divisivel por 3 e que diga se um numero é divisivel por 5")

num = int(input("entre com um número para saber se é divisivel por 3 ou 5?"))

if ( num % 3 == 0):
    print(f"o {num} é divisivel por 3!")
else:
     print(f"{num} não é divisível por 3.")
if ( num % 5 == 0 ):
    print(f"o {num} é divisivel por 5 ")

else: 
    print(f"{num} não é divisível por 5.")