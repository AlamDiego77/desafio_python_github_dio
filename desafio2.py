num1 = int(input("Digite o primeiro Numero: "))
num2 = int(input("Digite o Segundo Numero: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)

elif operacao == "-":
    print(abs(num1 - num2))

elif operacao == "*":
    print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else:
    print("Informação Invalida!!!\n\n Tente Novamente!!!")