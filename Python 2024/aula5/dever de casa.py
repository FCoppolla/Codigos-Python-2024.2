#faça um programa que peça o usuario para inserir 5 numeros. O programa deve calcular a soma acumulada desses numeros e exibir no resultado final
#peça ao usuario para inserir 5 numeros. 
#requisitos: use uma variavel acumuladora para armazenar a soma dos numeros. apos o usuario inserir todos os numeros exiba a soma total

print("Bem vindo a oficina grande Monte!")

Escolhaproduto = int(input("-------------------Bem Vindo a Oficina Grande Monte, qual opção você gostaria?---------------------\n Digite 1 para troca de óleo - R$100.00 \n Digite 2 para troca de filtro de Ar  - R$130.00 \n Digite 3 para garrafa de óleo - R$40.00 \n Digite 4 para fluido de freio 130.00  \n 5 - Combo Total R$320.00"))

item1 = ("troca de óleo")
item2 = ("troca de filtro de ar")
item3 = ("garrafa de óleo ")
item4 = ("Fluido de Freio")
item5 = ("combo total ")

if(Escolhaproduto == 1):
    print(f"Você escolheu {item1}")
    
    adicional = int(input("Gostaria de adicionar outro item? Digite 3 para garrafa de óleo e Digite 2 para filtro de ar digite 4 para fluido de freio  \n >"))
    if (adicional == 2):
        print(f"Você escolheu {item1} e {item2}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e Fluido de freio por R$ 90.00 ?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
           print(f"você escolheu {item1} + {item2}+ {item3} +{item4} por R$ 320.00 ")
    else:
        print(f"Seu pedido é {item1} + {item2},  totalizando R$230.00")
           
    elif (adicional == 3 ):
    print(f"Você escolheu {item1} e {item3}")
    oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00  ?\n sim ou não\n >").lower()
    if(oferecercombo == "sim"):
            print(f"Seu pedido é {item1} + {item2} + {item3} +{item4}, totalizando R$320.00")
    else:
        print(f"Seu pedido é {item1} + {item3},  totalizando R$140.00")
    
    elif (adicional == 4):
        print(f"Você escolheu {item1} e {item4}")
        oferecercombo = input("gostaria de adicionar os itens filtro de ar e a garrafa de óleo por R$ 90.00 a mais totalizando \n > ").lower()
        if(oferecercombo == sim):
            print(f"Seu pedido é {item1} + {item2} + {item3} +{item4}, totalizando R$320.00")
else:
   print(f"Seu pedido é {item1} + {item4},  totalizando R$ 230.00")
  
    elif (Escolhaproduto == 2):
            print(f"Você escolheu {item2}")
        adicional = int(input("Gostaria de adicionar outro item? Digite 3 para garrafa de óleo e Digite 1 para troca de óleo digite 4 fluido de freio  \n >"))
        if (adicional == 1):
            print(f"Você escolheu {item2} e {item1}")
            oferecercombo = input("Gostaria de adicionar garrafa de óleo e Fluido de freio por R$ 90.00 ?\n sim ou não\n >").lower()
            if(oferecercombo == "sim"):
                print(f"você escolheu {item2} + {item1}+ {item3} +{item4} por R$ 320.00 ")
            else:
                    print(f"Seu pedido é {item2} + {item1},  totalizando R$230.00")

    elif (adicional == 3 ):
        print(f"Você escolheu {item2} e {item3}")
        oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00  ?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            print(f"Seu pedido é {item2} + {item3} + {item1} +{item4}, totalizando R$320.00")
        else:
            print(f"Seu pedido é {item2} + {item3},  totalizando R$140.00")
    
        elif (adicional == 4):
    print(f"Você escolheu {item2} e {item4}")
oferecercombo = input("gostaria de adicionar os itens filtro de ar e a garrafa de óleo por R$ 90.00 \n > ").lower()
if(oferecercombo == sim):
         print(f"Seu pedido é {item2} + {item4} + {item1} +{item3}, totalizando R$320.00")
else:
   print(f"Seu pedido é {item2} + {item4},  totalizando R$ 230.00")

if (Escolhaproduto == 3):
        print(f"Você escolheu {item3}")
        adicional = int(input("Gostaria de adicionar outro item? Digite 3 para garrafa de óleo e Digite 2 para filtro de ar  \n >"))
        
        if (adicional == 1):
            print(f"Você escolheu {item3} e {item1}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e Fluido de freio por R$ 90.00 ?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
            print(f"você escolheu {item3} + {item1}+ {item2} +{item4} por R$ 320.00 ")
        else:
                print(f"Seu pedido é {item3} + {item1},  totalizando R$230.00")
           
elif (adicional == 2 ):
            print(f"Você escolheu {item3} e {item2}")
            oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00  ?\n sim ou não\n >").lower()
            if(oferecercombo == "sim"):
                print(f"Seu pedido é {item3} + {item2} + {item1} +{item4}, totalizando R$320.00")
            else:
                print(f"Seu pedido é {item2} + {item3},  totalizando R$140.00")
    
elif (adicional == 4):
            print(f"Você escolheu {item3} e {item4}")
            oferecercombo = input("gostaria de adicionar os itens filtro de ar e a garrafa de óleo por R$ 90.00 \n > ").lower()
            if(oferecercombo == sim):
                print(f"Seu pedido é {item2} + {item4} + {item1} +{item3}, totalizando R$320.00")
            else:
                print(f"Seu pedido é {item3} + {item4},  totalizando R$ 230.00")
            
if (Escolhaproduto == 4):
    print(f"Você escolheu {item4}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 3 para garrafa de óleo e Digite 2 para filtro de ar  \n >"))
    if (adicional == 1):
        print(f"Você escolheu {item4} e {item1}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e Fluido de freio por R$ 90.00 ?\n sim ou não\n >").lower()
        if(oferecercombo == "sim"):
                print(f"você escolheu {item4} + {item1}+ {item2} +{item3} por R$ 320.00 ")
        else:
                print(f"Seu pedido é {item4} + {item1},  totalizando R$230.00")
           
    elif (adicional == 2 ):
            print(f"Você escolheu {item4} e {item2}")
            oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00  ?\n sim ou não\n >").lower()
            if(oferecercombo == "sim"):
                print(f"Seu pedido é {item4} + {item2} + {item3} +{item1}, totalizando R$320.00")
            else:
                print(f"Seu pedido é {item4} + {item2},  totalizando R$140.00")
    elif (adicional == 3):
            print(f"Você escolheu {item4} e {item3}")
            oferecercombo = input("gostaria de adicionar os itens filtro de ar e a garrafa de óleo por R$ 90.00 \n > ").lower()
            if(oferecercombo == sim):
                print(f"Seu pedido é {item4} + {item3} + {item2} +{item1}, totalizando R$320.00")
            else:
                    print(f"Seu pedido é {item4} + {item3},  totalizando R$ 230.00")






