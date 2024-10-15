'''faça um programa que diga quais dos 20 primeiros multiplos de 5 sao pares'''
soma =0
for i in range(5, 101, 5):
    if  i % 2 == 0:  
        print(i)

    elif i%2 != 0:
        soma += i
        
print(f"a soma dos numeros impares é :{soma}")
