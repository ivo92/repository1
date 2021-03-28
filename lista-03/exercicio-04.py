n = float(input("Digite um número qualquer maior do que zero: "))

if n <= 0:
    print("Você não digitou um número maior do que zero. Rode o programa novamente.")

elif n > 0 and ((n % 2) == 0) and ((n % 3) != 0):
    print("O número é divisível por 2 mas não por 3.")

elif n > 0 and ((n % 3) == 0) and ((n % 2) != 0):
    print("O número é divisível por 3 mas não por 2.")

elif n > 0 and ((n % 2) == 0) and ((n % 3) != 0):
    print("O número é divisível por 2 mas não por 3.")

elif n > 0 and ((n % 2) == 0) and ((n % 3) == 0):
    print("O número é divisível por 2 e por 3.")

else:
    print("O número não é divisível por 2 nem por 3.")