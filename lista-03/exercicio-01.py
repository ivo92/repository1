a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a > b and a > c:
    print("O maior valor é %1.2f" %a)

if b > a and b > c:
    print("O maior valor é %1.2f" %b)

if c > b and c > a:
    print("O maior valor é %1.2f" %c)