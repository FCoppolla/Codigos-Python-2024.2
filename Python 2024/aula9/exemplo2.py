import random

#simula o lançamento de uma moeda 
resultado = "cara" if random.randint(0,1) == 0 else "coroa"
print (f"o resultado do lançamento da moeda é : {resultado}")