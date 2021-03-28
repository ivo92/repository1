x = float(input("Digite o primeiro valor (números reais): "))
o = input("Escreva o tipo de operação (+,-,/ ou *): ")
y = float(input("Digite o segundo valor (números reais): "))

if (o != "+") and (o != "-") and (o != "/") and (o != "*"):
    print("Você não digitou uma operação válida. Rode o programa novamente!")

if o == "-":
    resultado = x - y
    print(resultado)

if o == "/":
    resultado = x / y
    print(resultado)

if o == "+":
    resultado = x + y
    print(resultado)

if o == "*":
    resultado = x * y
    print(resultado)

