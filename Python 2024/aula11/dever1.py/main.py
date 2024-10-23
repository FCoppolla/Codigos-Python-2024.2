from funcoes import calculadora, soma, subtracao, multiplicacao, divisao

if __name__ == "__main__":
    calculadora()
    

    
num1 = float(input("Digite o primeiro número:\n > "))
num2 = float(input("Digite o segundo número:\n > "))

operacao = input("Digite o número da operação (1 = soma, 2= subtração, 3 = multiplicação,4 = divisao):\n > ")


if operacao == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
elif operacao == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
elif operacao == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
elif operacao == '4':
        resultado = divisao(num1, num2)
        print(f"{num1} / {num2} = {resultado}")
   
    
if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")



