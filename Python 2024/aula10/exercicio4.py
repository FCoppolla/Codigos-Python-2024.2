'''faça um programa onde: o Pikachu começa com uma lista de 4 poderes:
poderes = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]'''

'''faça um programa que voce ao adicionar um novo poder voce precisa remover outro. ou seja o pikachu precisa ter sempre 4 poderes '''
pokemon = "Pikachu"
poderes = ["choque do trovão", "calda de ferro", "ataque rapido", "esquiva"]

print(poderes)
validação = input("gostaria de adicionar um novo poder ao pikachu? S/N\n >").lower()
if validação == "s" :
    adicionar = input ("qual golpe voce gostaria de adicionar?\n >").lower()
    remover = input("qual golpe voce gostaria de remover?:\n >").lower()

    poderes.remove(remover)
    poderes.append(adicionar)

    print("poderes após a atualização:" , poderes)