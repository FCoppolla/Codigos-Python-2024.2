'''a escola adicionou um novo armario 3x3 perto das salas e o chamou de armario vip, caso o aluno adiquira uma gaveta nor armario custaria 50 reais.
adicione ao sistema  essa seleção e retorne para o usuario o custo'''



matriz2 =[
    ["   ", "     ", "      "],
    ["   ", "     ", "      "],
    ["   ","      ", "      "],
]


print(matriz2)

nome = input("qual o seu nome?")
linha =int(input("em qual inha do armario será a sua gaveta [0 a 2]" ))
coluna = int(input("em qual coluna do armario voce utilizará? [0 a 2]"))


matriz2 [linha][coluna] = nome

for linha in matriz2:
    print(linha)

print(matriz2)
    
print(" o valor por esse espaço vip é de: 50 reais ")
