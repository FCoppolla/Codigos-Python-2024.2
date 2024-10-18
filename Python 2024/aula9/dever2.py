import random

def jogar(nivel):
    # Define o número de tentativas com base no nível
    if nivel == '1':
        tentativas = 10
    elif nivel == '2':
        tentativas = 7
    elif nivel == '3':
        tentativas = 5
    else:
        print("Nível inválido")
        return

    # Gera dois números aleatórios
    numero1 = random.randint(1, 200)
    numero2 = random.randint(1, 200)

    for tentativa in range(1, tentativas + 1):
        palpite1 = int(input(f"Tentativa {tentativa} (número 1): Adivinhe o primeiro número (entre 1 e 200): "))
        if palpite1 == numero1:
            print("Parabéns! Você acertou o primeiro número!")
            break
        elif palpite1 < numero1:
            print("O número é maior.")
        else:
            print("O número é menor.")
    else:
        print(f"Você não conseguiu adivinhar o primeiro número em {tentativas} tentativas. O número era {numero1}.")

    for tentativa in range(1, tentativas + 1):
        palpite2 = int(input(f"Tentativa {tentativa} (número 2): Adivinhe o segundo número (entre 1 e 200): "))
        if palpite2 == numero2:
            print("Parabéns! Você acertou o segundo número!")
            break
        elif palpite2 < numero2:
            print("O número é maior.")
        else:
            print("O número é menor.")
    else:
        print(f"Você não conseguiu adivinhar o segundo número em {tentativas} tentativas. O número era {numero2}.")

# Menu de dificuldade
print("Qual o nível de dificuldade você gostaria de jogar?")
print("1 - Fácil (10 tentativas)")
print("2 - Médio (7 tentativas)")
print("3 - Difícil (5 tentativas)")

nivel = input("Escolha o nível de dificuldade (1, 2 ou 3): ")
jogar(nivel)
