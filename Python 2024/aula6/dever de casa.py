#Dever de casa:
#Desenvolva um programa que simula um sistema de reciclagem com contagem dos materiais reciclados. O programa deve:

#Exibir uma mensagem de boas-vindas ao usuário: "Bem-vindo ao programa de reciclagem!".
#Solicitar ao usuário que informe o tipo de material que ele deseja reciclar, entre as opções: papel, plástico, vidro, metal, orgânico ou resíduos não recicláveis.
#Com base no material informado, o programa deve informar a cor da lixeira correta para descarte e contabilizar a quantidade de cada material reciclado:

#Papel: lixeira azul.
#Plástico: lixeira vermelha.
#Vidro: lixeira verde.
#Metal: lixeira amarela.
#Orgânico: lixeira marrom.
#Resíduos não recicláveis: lixeira cinza.

#Se não for reconhecido, exibir a mensagem: "Erro tente novamente e não contabilizar na contagem de nenhuma lixeira. 

#Perguntar ao usuário se ele deseja continuar reciclando. Se o usuário digitar 's', o programa deve repetir o processo; caso contrário, o programa deve exibir um resumo da reciclagem com a quantidade de materiais reciclados e a mensagem: "Obrigado por contribuir com a reciclagem!". ''''

print("Bem vindo ao programa de reciclagem!")

material = input("Qual material você deseja reciclar?\n 1 - papel\n 2 - plástico\n 3 - vidro\n 4 - metal\n  5 - orgânico ou resíduos\n 6 - nao reciclaveis \n")

materiais = {'1': 'papel','2': 'plástico','3': 'vidro','4': 'metal','5': 'orgânicos','6': 'nao reciclaveis'}

lixeiras = {'1': 'azul','2': 'vermelha','3': 'verde','4': 'amarela', '5': 'marrom', '6': 'cinza'}


if material in materiais:
    print(f"A lixeira designada é {lixeiras[material]}")
else:
    print("Erro: tente novamente.")
    
continuar = input("Deseja reciclar outro material? (s/n): ")
if continuar.lower() != 's':
    
    if continuar == 'n':
        print ("muito obrigado por reciclar conosco!... O planeta agradece!")
    
    
    
