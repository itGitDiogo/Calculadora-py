# Receber o primeiro numero
# Receber um operador (+ - * /)
# Receber o segundo numero
# Mostrar o resultado

print("Digite o primeiro número:")
n1 = int(input())

print("Digite o operador: ")
operador = input()

while operador != '+' and operador != '-' and operador != '*' and operador != '/':
    print("Operador invalido, digite novamente")
    operador = input()

print("Digite o segundo número:")
n2 = int(input())

if operador == '+':
    resultado = n1 + n2
    print(f"{n1} {operador} {n2} = {resultado}")
elif operador == '-':
    resultado = n1 - n2
    print(n1 + operador + n2, resultado)
elif operador == '*':
    resultado = n1 * n2
    print(n1 + operador + n2, resultado)
elif operador == '/':
    resultado = n1 / n2
    print(n1 + operador + n2, resultado)
else:
    print ("Operador incorreto")

    oiee