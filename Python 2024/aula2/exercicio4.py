#pergunte a idade de uma pesssoa .calcule o descontos dos seguintes produtos 
#calça azul R$120,00 e jaqueta verde R$150,00 sabendo que o valor do desconto é equivalente  a idade 

numero1 = int(input("qual a idade: "))
calça = 120
jaqueta = 150

valor_com_desconto_calça =  calça - numero1
valor_com_desconto_jaqueta = jaqueta - numero1

print(f"Na nossa loja temos os seguintes produtos: calça azul com o valor {calça} e uma jaqueta verde no valor {jaqueta}")
print(f"Graças a sua idade nos daremos um valor de desconto de R${numero1} para voce nos dois produtos")
print (f"a calça azul custará {valor_com_desconto_calça} e a jaqueta custará {valor_com_desconto_jaqueta}")