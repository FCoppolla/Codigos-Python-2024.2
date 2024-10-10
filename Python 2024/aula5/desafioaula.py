#faça um programa que: perguntar o usuario se o usuario quer um COMBO ou um item individual.
#onde o hamburguer custa 10.00, batata frita 10.00 refri custa 10.00 combo 22.00
#cliente pode adicionar 2 itens mas caso faça , ofereça o terceiro item por 2 reais, incentivando e vendendo o combo .

EscolhaLanche = int(input("-------------------Bem Vindo ao Maquimeleca, qual opção você gostaria?---------------------\n Digite 1 para Hamburguer - R$10,00 \n Digite 2 para Batata Frita  - R$10,00 \n Digite 3 para refrigerente - R$10,00 \n Digite 4 para combo (os 4 itens) - R$22,00 \n"))
item1 = "Hamburguer"
item2 = "Batata Frita"
item3 = "Refrigerante"
item4 = "Combo"

soma = 0
valortotal = {soma}

if(EscolhaLanche == 1):
    print(f"Você escolheu {item1}")
    soma +=10
    adicional = int(input("Gostaria de adicionar outro item? Digite 2 para Batata Frita e Digite 3 para refrigerente\n >"))
    if (adicional == 2):
        print(f"Você escolheu {item1} e {item2}")
        soma +=10
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            soma +=2
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")

        else:
            print(f"Seu pedido é {item1} + {item2},  totalizando R$20,00")

    elif (adicional == 3):
        soma +=10
        print(f"Você escolheu {item1} e {item3}")
        oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            soma +=2
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")

        else:
            print(f"Seu pedido é {item1} + {item3},  totalizando R$20,00")

    else:
        print(f"Seu pedido é {item1},  totalizando R$10,00") 
        
elif(EscolhaLanche ==2):
    print(f"Você escolheu {item2}")
    soma +=10
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para hamburguer e Digite 3 para refrigerente"))
    if (adicional == 1):
            print(f"Você escolheu {item2} e {item1}")
            soma +=10
            oferecercombo = input("Gostaria de adicionar o refrigerente por mais R$2,00?\n sim ou não\n >").lower()
            if(oferecercombo == "sim"):
                soma +=2
                print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")

            else:
                print(f"Seu pedido é {item2} + {item1},  totalizando R$20,00")
    if (adicional == 3):
        soma +=10
        print(f"Você escolheu {item2} e {item3}")
        oferecercombo = input("Gostaria de adicionar o Hamburguer por mais R$2,00?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            soma +=2
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")

        else:
         print(f"Seu pedido é {item2} + {item3},  totalizando R$20,00")

    else:
        print(f"Seu pedido é {item1},  totalizando R$10,00") 
            
elif(EscolhaLanche ==3):
    print(f"Você escolheu {item3}")
    soma += 10
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para Hamburguer e Digite 2 para Batata- frita\n >"))
    if (adicional == 1):
        print(f"Você escolheu {item3} e {item1}")
        soma +=10
        oferecercombo = input("Gostaria de adicionar o batata - frita por mais R$2,00?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
                soma+=2
                print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")

        else:
            print(f"Seu pedido é {item3} + {item1},  totalizando R$20,00")
    if (adicional == 2):
        print(f"Você escolheu {item3} e {item2}")
        soma +=10
        oferecercombo = input("Gostaria de adicionar o Hamburguer por mais R$2,00?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            soma += 2
            print(f"Seu pedido é {item1} + {item2} + {item3}, totalizando R$22,00")
        else:
            print(f"Seu pedido é {item3} + {item2},  totalizando R$20,00")

    else:
        print(f"Seu pedido é {item3},  totalizando R$10,00") 

        print("seu pedido teve um custo de {valortotal}")