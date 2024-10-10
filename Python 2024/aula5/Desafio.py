#faça um programa que peça o usuario para inserir 5 numeros. O programa deve calcular a soma acumulada desses numeros e exibir no resultado final
#peça ao usuario para inserir 5 numeros. 
#requisitos: use uma variavel acumuladora para armazenar a soma dos numeros. apos o usuario inserir todos os numeros exiba a soma total

#exibindo a soma acumulada
soma_acumulada = 0

for i in range(5):
    numero = float(input(f"Insira o {i + 1} número: "))
    soma_acumulada += numero 
    
print(f"A soma total dos números inseridos é: {soma_acumulada}")
