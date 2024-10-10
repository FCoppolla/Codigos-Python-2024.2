#programa oficina grande monte!
print("Bem-vindo à Oficina Grande Monte!")

Escolhaproduto = int(input("-------------------Bem Vindo a Oficina Grande Monte, qual opção você gostaria?---------------------\n""Digite 1 para troca de óleo - R$100.00\n""Digite 2 para troca de filtro de ar - R$130.00\n""Digite 3 para garrafa de óleo - R$40.00\n""Digite 4 para fluido de freio - R$130.00\n""Digite 5 para combo total - R$320.00 \n>"))
item1 = "troca de óleo"
item2 = "troca de filtro de ar"
item3 = "garrafa de óleo"
item4 = "fluido de freio"
item5 = "combo total"

if Escolhaproduto == 1:
    print(f"Você escolheu {item1}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 2 para filtro de ar, 3 para garrafa de óleo ou 4 para fluido de freio\n> "))
    
    if adicional == 2:
        print(f"Você escolheu {item1} e {item2}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e fluido de freio por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Você escolheu {item1}, {item2}, {item3} e {item4} por R$ 320.00")
        else:
            print(f"Seu pedido é {item1} + {item2}, totalizando R$ 230.00")
    
    elif adicional == 3:
        print(f"Você escolheu {item1} e {item3}")
        oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1}, {item2}, {item3} e {item4}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item1} + {item3}, totalizando R$ 140.00")
    
    elif adicional == 4:
        print(f"Você escolheu {item1} e {item4}")
        oferecercombo = input("Gostaria de adicionar filtro de ar e garrafa de óleo por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item1}, {item2}, {item3} e {item4}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item1} + {item4}, totalizando R$ 230.00")

elif Escolhaproduto == 2:
    print(f"Você escolheu {item2}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para troca de óleo, 3 para garrafa de óleo ou 4 para fluido de freio\n> "))
    
    if adicional == 1:
        print(f"Você escolheu {item2} e {item1}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e fluido de freio por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Você escolheu {item2}, {item1}, {item3} e {item4} por R$ 320.00")
        else:
            print(f"Seu pedido é {item2} + {item1}, totalizando R$ 230.00")

    elif adicional == 3:
        print(f"Você escolheu {item2} e {item3}")
        oferecercombo = input("Gostaria de adicionar filtro de ar e fluido de freio por R$ 140.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item2}, {item3}, {item1} e {item4}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item2} + {item3}, totalizando R$ 140.00")
    
    elif adicional == 4:
        print(f"Você escolheu {item2} e {item4}")
        oferecercombo = input("Gostaria de adicionar filtro de ar e garrafa de óleo por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item2}, {item4}, {item1} e {item3}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item2} + {item4}, totalizando R$ 230.00")

elif Escolhaproduto == 3:
    print(f"Você escolheu {item3}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para troca de óleo ou 2 para filtro de ar\n> "))
    
    if adicional == 1:
        print(f"Você escolheu {item3} e {item1}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e fluido de freio por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Você escolheu {item3}, {item1}, {item2} e {item4} por R$ 320.00")
        else:
            print(f"Seu pedido é {item3} + {item1}, totalizando R$ 230.00")
    
    elif adicional == 2:
        print(f"Você escolheu {item3} e {item2}")
        oferecercombo = input("Gostaria de adicionar troca de óleo e fluido de freio por R$ 140.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item3}, {item2}, {item1} e {item4}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item3} + {item2}, totalizando R$ 140.00")
    elif adicional == 4: 
            print(f"Você escolheu {item3} e {item4}")
            oferecercombo = input("Gostaria de adicionar troca de óleo e fluido de freio por R$ 140.00? (sim ou não)\n> ").lower()
            if oferecercombo == "sim":
                print(f"Seu pedido é {item3}, {item4}, {item2} e {item1}, totalizando R$ 320.00")
            else:
                print(f"Seu pedido é {item3} + {item4}, totalizando R$ 140.00")       

elif Escolhaproduto == 4:
    print(f"Você escolheu {item4}")
    adicional = int(input("Gostaria de adicionar outro item? Digite 1 para troca de óleo ou 2 para filtro de ar digite 3 para garrafa de óleo\n> "))
    
    if adicional == 1:
        print(f"Você escolheu {item4} e {item1}")
        oferecercombo = input("Gostaria de adicionar garrafa de óleo e fiutro de ar por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Você escolheu {item4}, {item1}, {item2} e {item3} por R$ 320.00")
        else:
            print(f"Seu pedido é {item4} + {item1}, totalizando R$ 230.00")
    
    elif adicional == 2:
        print(f"Você escolheu {item4} e {item2}")
        oferecercombo = input("Gostaria de adicionar troca de óleo e garrafa de óleo por R$ 140.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item4}, {item2}, {item3} e {item1}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item4} + {item2}, totalizando R$ 140.00")
    
    elif adicional == 3:
        print(f"Você escolheu {item4} e {item3}")
        oferecercombo = input("Gostaria de adicionar filtro de óleo e filtro de ar por R$ 90.00? (sim ou não)\n> ").lower()
        if oferecercombo == "sim":
            print(f"Seu pedido é {item4}, {item3}, {item2} e {item1}, totalizando R$ 320.00")
        else:
            print(f"Seu pedido é {item4} + {item3}, totalizando R$ 230.00")
