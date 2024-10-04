print("vamos calcular seu IMC? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("qual a sua altura? ")) 
imc = peso/(altura*altura)
print(f"seu imc é:{imc:.2f}")

if(imc<16):
    print("você tem magreza grave!!")
elif(imc>=16 and imc<=16.9):
    print("você tem magreza moderada !!")
elif(imc>=17 and imc<=18.5 ):
    print("você tem magreza leve!!!")
elif(imc>=18.6 and imc<=24.9):
    print("você tem o peso ideal")
elif(imc>=25 and imc<=29.9):
    print("você tem um sobrepeso")
elif (imc>=30 and imc<=34.9):
    print("você tem obesidade grau I")
elif(imc>=35 and imc<=39.9):
    print("você tem obesidade grau II ou severa")
elif(imc>=40):
    print("você tem obesidade grau III ou mórbida.")

