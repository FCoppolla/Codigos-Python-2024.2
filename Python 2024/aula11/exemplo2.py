#função: Calcula o quadrado de um numero

def quadrado(numero):
    return numero **2

numero = float (input("digite um numero:\n >"))
resultado = quadrado(numero) #recebe o retorno da função
print(f"o quadrado de {numero} é {resultado}")


