#faça um programa para um lava rápido onde:
# 1 lavagem completa a R$ 50.00 e 2 lavagem basica a R$ 35.00
#caso o usuario queira, o pretinho custa mais R$ 5.00
#retorne  serviço + o valor dele
 
print("bem vindo ao Lava Rapido - Bem-lavado!!")
lavagem = int(input("selecione o tipo de lavagem\n 1- lavagem completa a 50.00\n 2 - lavagem basica a 35.00\n >"))
if (lavagem == 1):
    print ("voce escolheu a lavagem completa")
    valortotal = 50
    categorialavagem = "completa"
elif (lavagem == 2):
    print("voce escolheu a lavagem basica")
    valortotal = 35
    categorialavagem = "basica"
else:
    print("número invalido, tente novamente")
    
pretinho = input("gostaria de adicionar o pretinho na roda por mais R$ 5.00, (sim ou não)?\n >")
if (pretinho == "sim"):
    valortotal += 5
    print(f"o serviço de {categorialavagem} será no total de R$ {valortotal} com o pretinho")
else:
    print(f"o serviço de {categorialavagem} será no total de R$ {valortotal}")