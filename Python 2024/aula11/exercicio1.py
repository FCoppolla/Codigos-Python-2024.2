'''voce é um aventureiro carregando uma mochila que comporta 3 itens, uma espada, uma poção e um escudo.
ao longo da aventura encontra um arco no chão e precisa decidir se coloca na mochila ou nao, ou não. se colocar na mochila precisará descartar outro item a sua escolha'''

print("vocé um aventureiro animado por novas aventuras andando sempre para novos lugares. ")
print("voce encontra um arco novo no chão...")

inventario = ["espada", "poção", "escudo"]

print(inventario)
validação = input("gostaria de adicionar o novo arco ? S/N\n >").lower()
if validação == "s" :
    adicionar = input (" voce gostaria de adicionar o novo item ao seu inventario ?\n >").lower()
    remover = input("qual item voce gostaria de remover?:\n >").lower()

    inventario.remove(remover)
    inventario.append(adicionar)
else:
    print(" nada acontece...")


print("inventario após a atualização:" , inventario)