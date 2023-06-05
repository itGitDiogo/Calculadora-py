# Receber o primeiro numero
# Receber um operador (+ - * /)
# Receber o segundo numero
# Mostrar o resultado

import operator

dict_operadores = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

print("Digite o primeiro número:")
n1 = int(input())

print("Digite o operador: ")
operador = input()

while operador not in ['+','-','*','/']:
    print("Operador invalido, digite novamente")
    operador = input()

print("Digite o segundo número:")
n2 = int(input())

print((f"{n1} {operador} {n2} = {dict_operadores[operador](n1,n2)}"))