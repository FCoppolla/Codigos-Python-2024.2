#faça um programa que pergunte quantas rodas tem um veiculo
#se tiver 4 diga carro ou van, caso contrario avise o usuario que o veiculo nao foi encontrado correspondente ao numero de rodas

print("vamos procurar o seu veiculo??")

rodas = int(input("quantas rodas tem o veiculo em questão?"))
if(rodas==4):
    print("o veiculo é um carro ou uma van ")
elif(rodas ==2):
    print("o veiculo é uma moto ou bicicleta")
elif(rodas==1):
    print("o veiculo é um monociclo")
elif(rodas==6):
    print("esse veiculo é um onibus")
elif(rodas>=8 and rodas<=20):
    print("o veiculo procurado é um caminhão ")

else:
    print("Não foi encontrado um veiculo correspondente ao número de rodas!!")

    #se colocar rodas e RoDAS dentro de uma mesma condição, ele não reconhecerá a segunda variavel pelo fato dela não ter sido usada para nada
