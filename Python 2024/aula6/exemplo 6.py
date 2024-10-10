#faça um programa que some infinitamente numeros que o usuario colocar e so parar de somar caso ele escreva parar

#booleano só pode ser True ou False 
x = True
soma = 0 
while (x==True):
    numero =float(input("digite um numero"))
    continuar = input("continuar ou parar?").lower()
    if(continuar == "parar"):
        soma += numero
        print (f"a soma deu {soma}")
        x=False
else:        
    soma += numero
