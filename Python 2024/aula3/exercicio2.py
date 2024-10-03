#peça para o usuario colocar o seu peso em quilos e sua altura em metros, com base nisso retorne para ele o seu IMC
#IMC = peso/(alturaxaltura)
print("vamos calcular seu IMC? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("qual a sua altura? ")) 
imc = peso/(altura*altura)
print(f"seu imc é:{imc:.2f}")
