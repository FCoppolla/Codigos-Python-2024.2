'''jogo do palpite.  sistema gera 1 numero aleatorio entre 1 e 200.  usuario tem 10 palpites para tentar acertar . sistema sempre da um feedback dizendo se o 'numero secreto'
é maior ou menor que o palpite do usuario '''

import random

numero_secreto = random.randint(1, 200)
tentativas = 0 

print("Bem-vindo ao jogo do palpite!")
escolher = input("Escolha o nível de dificuldade:\n1 - Fácil (10 tentativas)\n2 - Médio (7 tentativas)\n3 - Difícil (5 tentativas)\n> ")

if escolher == '1':
    tentativas = 10
    print("Você escolheu a opção: Fácil.")

elif escolher == '2':
    tentativas = 7
    print("Você escolheu a opção: Médio.")

elif escolher == '3':
    tentativas = 5
    print("Você escolheu a opção: Difícil.")

else:
    print("Você não escolheu nenhuma opção... Tente novamente.")
    exit()  # Encerra o programa se a escolha for inválida

print(f"Adivinhe um número entre 1 e 200. Você tem {tentativas} tentativas!")

while tentativas > 0:
    palpite = int(input("Insira um palpite: "))

    if palpite < 1 or palpite > 200:
        print("Por favor, escolha um número entre 1 e 200.")
        continue  # Pede um novo palpite se o número estiver fora do intervalo

    if palpite < numero_secreto:
        print("O número secreto é maior que o seu palpite.")

    elif palpite > numero_secreto:
        print("O número secreto é menor que o seu palpite.")

    else:
        print(f"Parabéns! Você acertou o número secreto: {numero_secreto}!")
        break

    tentativas -= 1
    print(f"Você ainda tem {tentativas} tentativas.")

if tentativas == 0:
    print(f"Você esgotou suas tentativas. O número secreto era: {numero_secreto}.")