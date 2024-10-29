'''faça um programa que simule o armario de uma escola e permita colocar o nome do aluno responsavel/ pagante da gaveta 6 armarios  tem a dimensão 5x5'''


matriz = [
    ["maria", "joão", "vitor", "amanda", "victoria"],
    ["jonas", "beatriz", "Felipe", "       ", "arthur"],
    ["      ", "      ", "  ", "  ", "    "],
    ["joana", "Diego", "       ", "Laura", "Carla "],
    ["     ", "     ", " Jefferson","     ", "      "]
]


print(matriz)

nome = input("qual o seu nome?")
linha =int(input("em qual inha do armario será a sua gaveta [0 a 4]" ))
coluna = int(input("em qual coluna do armario voce utilizará? [0 a 4]"))

matriz[linha][coluna] = nome

for linha in matriz:
    print(linha)




print("o valor por esse espaço é de: 30 reais")