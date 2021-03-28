print("Dadas as seguintes séries:")
print("0 Lucas")
print("1 Pell")
print("2 Triangular")
print("3 Square")
print("4 Pentagonal")

s = int(input("Qual série você deseja computar? Obs.: Digite um número válido de 0 a 4: "))

if s < 0 or s > 4:
    print("Você não digitou um número válido. Rode o programa novamente!")

if s == 0:
    print("Você escolheu computar a série 'Lucas'!")

if s == 1:
    print("Você escolheu computar a série 'Pell'!")

if s == 2:
    print("Você escolheu computar a série 'Triangular'!")

if s == 3:
    print("Você escolheu computar a série 'Square'!")

if s == 4:
    print("Você escolheu computar a série 'Pentagonal'!")
