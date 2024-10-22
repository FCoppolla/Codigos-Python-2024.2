'''programa que tenha uma função chamada converter essa função deve receber uma températura em celsius e retorne fahreinheit'''


def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("digite um numero:\n >"))
temperatura_fahrenheit = converter(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")