print("vocé um aventureiro animado por novas aventuras andando sempre para novos lugares. ")
print("voce encontra um arco novo no chão...")

inventario = ["espada", "poção", "escudo"]

print(inventario)

if "espada" in inventario:
    print(" a espada está no seu inventario.")

else:
    print("a 'espada' não está no inventario.")



validação = input("gostaria de adicionar o novo arco ? S/N\n >").lower()
if validação == "s" :
    adicionar = input (" voce gostaria de adicionar o novo item ao seu inventario ?\n >").lower()
    remover = input("qual item voce gostaria de remover?:\n >").lower()

    inventario.remove(remover)
    inventario.append(adicionar)
else:
    print(" nada acontece...")


print("inventario após a atualização:" , inventario)


print(" você encontrou um ladrão querendo sua poção que costa no seu inventario ")
questão1 = (input("voce gostaria de entregar a poção ao bandido ou voce quer lutar contra o mesmo? S/N\n >")).lower()

if (questão1 == "s" ):
    print("voce entrega a poção e vai emborar...")
    inventario.remove('poção')
    
else: 
    print(" voce se negou então chamou o mesmo para a briga.")



print("como está o seu inventario após sua decisão", inventario)


questão2 = input("voce gostaria de lutar com espada ou sem? S/N \n >").lower()

if questão2 == "s":

    print("voce confrontou o bandido com uma espada e acabou vencendo ... RIP para o bandido e voce segue sua jornada")

else:
    print("voce não sabe lutar sem sua fiel espada e acaba sendo derrotado e é game over .")



