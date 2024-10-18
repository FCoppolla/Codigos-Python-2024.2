'''Dever de casa: Adicione ao jogo da adivinhação a opção de colocar mais 1 ou 2 números para serem advinhados simultaneamente'''

import random

def gerar_numeros(qtd):
    return random.sample(range(1, 201), qtd)

print("Qual o nível de dificuldade você gostaria de jogar?")
print("1 - Fácil (10 tentativas)")
print("2 - Médio (7 tentativas)")
print("3 - Difícil (5 tentativas)")

nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")

if nivel == '1':
    tentativas = 10
elif nivel == '2':
    tentativas = 7
elif nivel == '3':
    tentativas = 5
else:
    print("Nível inválido")
    exit()

quantidade_numeros = int(input("Quantos números você quer adivinhar? (1 ou 2): "))

if quantidade_numeros not in [1, 2]:
    print("Quantidade inválida. Escolha 1 ou 2.")
    exit()

numeros = gerar_numeros(quantidade_numeros)

while tentativas > 0:
    palpite = input(f"Tentativas restantes: {tentativas}. Adivinhe os números (separados por espaço): ")
    palpites = list(map(int, palpite.split()))

    acertos = [num for num in palpites if num in numeros]
    errou = [num for num in palpites if num not in numeros]

    if len(acertos) == quantidade_numeros:
        print("Parabéns! Você acertou todos os números!")
        break
    else:
        if acertos:
            print(f"Você acertou: {acertos}")
        if errou:
            print(f"Números errados: {errou}")
        tentativas -= 1

if tentativas == 0:
    print(f"Você não conseguiu adivinhar os números em {tentativas + 1} tentativas. Os números eram: {numeros}.")