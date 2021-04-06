serie = input(str("Dadas as seguintes séries:\n"
" \n"
"Lucas\n"
"Pell\n"
"Triangular\n"
"Square\n"
"Pentagonal\n"
" \n"
"Digite a série escolhida para que possamos retornar a sequência atribuída: "))

if serie == "Lucas":
    a = 2
    print(a)

    b = 1
    print(b)

    n = 3

    while n <=11:
        proximo = b + a
        print(proximo)
        a = b
        b = proximo
        n = n + 1

elif serie == "Pell":
    a = 0
    print(a)

    b = 1
    print(b)

    n = 3

    while n <=11:
        proximo = 2*b + a
        print(proximo)
        a = b
        b = proximo
        n = n + 1

elif serie == "Triangular":

    n = 0

    while n <= 11:
        proximo = (n*(n+1))/2
        print(proximo)
        n = n + 1

elif serie == "Square":

    n = 0

    while n <= 11:
        proximo = n**2
        print(proximo)
        n = n + 1

elif serie == "Pentagonal":

    n = 0

    while n <= 11:
        proximo = (3*(n**2) - n)/2
        print(proximo)
        n = n + 1

else:
    print("Você não digitou um valor válido. Obs.: Diferencia minúsculas de maiúsculas.")

