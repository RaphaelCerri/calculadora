#calculadora básica

op1= float(input("Digite o primeiro número: "))
op2= float(input("Digite o segundo número "))
operador= input("Digite a operação desejada (+,-,* ou /): ")

if operador == "+":
    print("O resultado da soma é: ",op1 + op2)
elif opererador == "-":
    print("O resultado da subtração é: ",op1 - op2)
elif operador == "*":
    print("O resultado da multiplicação é: ",op1 * op2)
elif oper == "/":
    print("O resultado da divisão é: ",op1 / op2)
else:
    print("Operação Inválida")
    
