# contador += 1    =  > contador = contador +1     ( )
#contador -= 1     = >  contador = contador -1

import time
print("inciando contagem regressiva")
contador = 5

while contador > 0:
    print(contador)
    time.sleep(1)
    contador -= 1

print("Fim da contagem regressiva! Bom")