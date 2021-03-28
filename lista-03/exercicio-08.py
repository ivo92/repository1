import math

x = int(input("Digite o valor da coordenada x do ponto: "))
y = int(input("Digite o valor da coordenada y do ponto: "))
xra = int(input("Digite o valor da coordenada x do início da reta: "))
yra = int(input("Digite o valor da coordenada y do início da reta: "))
xrb = int(input("Digite o valor da coordenada x do final da reta: "))
yrb = int(input("Digite o valor da coordenada y do final da reta: "))

dist = ((((yrb) - (yra)) * ((x) - (xra)) - ((xrb) - (xra)) * ((y) - (yra))) /
        (math.sqrt((xrb - xra)^2 + (yrb - yra)^2)))

if dist >= 0:
    print(dist)

else:
    print(dist*(-1))