#faça um programa que conte de 0 a 10
#e diga no final "obrigado por esperar estamos redirecionando sua ligação"


import time
print("contagem de espera")
contador = 0

while contador <= 10:
    print(contador)
    time. sleep (1)
    contador = contador +1

print("obrigado por esperar! estaremos redirecionando sua ligação!")
