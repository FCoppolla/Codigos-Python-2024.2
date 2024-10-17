jogar = True
while jogar == True:
    contador = 0
print("kahoot iniciado ")
resposta1 = input ("a lingua Python e a lingua mais simples já criada?\n  verdadeiro/falso? \n >  ").lower()
if(resposta1 == "verdadeiro"):
    print("resposta está correta!")
    contador +=1
else: 
    print("Errou !")

resposta2 = input("str é utilizado para numero?\n Verdadeiro/falso \n >").lower()

if(resposta2 == "falso"):
    print("a resposta está correta! ")
    contador +=1
else:
    print("errou !")

resposta3 = input("'if' é utilizado como condição?\n verdadeiro/falso\n >").lower()

if (resposta3 == "verdadeiro"):
    print("a resposta está correta!")
    contador +=1
else: 
    print("Errou!")
    exit()

quantidade_de_pergunta = 3
if contador/2 >= quantidade_de_pergunta/2:
    print("voce venceu!")

else:
    print("Voce mandou mal!")

perguntar = input("deseja jogar novamente? \n  S ou n")

if (perguntar == "n"):
    jogar = False