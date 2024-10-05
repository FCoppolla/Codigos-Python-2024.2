print("vamos calcular seu IMC? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("qual a sua altura? ")) 
imc = peso/(altura*altura)





if(imc< 18.5 ):
    classificação = "magreza"
    grau = 0
elif(imc>=18.5 and imc<=24.9):
    classificação = "normal" 
    grau = 0
elif(imc>=25 and imc<=29.9):
    classificação = "sobrepeso" 
    grau = 1
elif (imc>=30 and imc<=39.9):
    classificação = "obesidade I"
    grau = 2
elif(imc> 40):
    classificação = "obsidade severa" 
    grau = 3

#exibir resultado
print(f"seu imc é: {imc:.2f}")
print(f"classificação é: {classificação}")
print(f"grau de obesidade: {grau}")  

