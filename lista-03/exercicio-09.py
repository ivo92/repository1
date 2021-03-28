import math

xp1 = int(input("Digite o valor da coordenada x do início da reta 1: ")) #1
yp1 = int(input("Digite o valor da coordenada y do início da reta 1: ")) #1
xp2 = int(input("Digite o valor da coordenada x do final da reta 1: ")) #5
yp2 = int(input("Digite o valor da coordenada y do final da reta 1: ")) #5
xp3 = int(input("Digite o valor da coordenada x do início da reta 2: ")) #5
yp3 = int(input("Digite o valor da coordenada y do início da reta 2: ")) #1
xp4 = int(input("Digite o valor da coordenada x do final da reta 2: ")) #1
yp4 = int(input("Digite o valor da coordenada y do final da reta 2: ")) #5

hp1 = (((yp4) - (yp3)) * ((xp1) - (xp3)) - ((xp4) - (xp3)) * ((yp1) - (yp3))) #/
        #(math.sqrt((xp4 - xp3)^2 + (yp4 - yp3)^2)))

hp2 = (((yp4) - (yp3)) * ((xp1) - (xp3)) - ((xp4) - (xp3)) * ((yp1) - (yp3))) #/
        #(math.sqrt((xp4 - xp3)^2 + (yp4 - yp3)^2)))

hp3 = (((yp2) - (yp1)) * ((xp3) - (xp1)) - ((xp2) - (xp1)) * ((yp3) - (yp1))) #/
        #(math.sqrt((xp2 - xp1)^2 + (yp2 - yp1)^2)))

hp4 = (((yp2) - (yp1)) * ((xp3) - (xp1)) - ((xp2) - (xp1)) * ((yp3) - (yp1))) #/
        #(math.sqrt((xp2 - xp1)^2 + (yp2 - yp1)^2)))

if (hp1 * hp2) < 0:
    print("Os pontos P1 e P2 encontram-se em lados opostos da reta que une os pontos p3 e p4")

if (hp3 * hp4) < 0:
    print("Os pontos P3 e P4 encontram-se em lados opostos da reta que une os pontos p1 e p2")

if hp1 == 0 or hp2 == 0:
    print("Um desses pontos encontra-se sobre a reta que une os pontos p3 e p4")

if hp1 == 0 and hp2 == 0:
    intervalox = xp2 - xp1
    intervaloy = yp2 - yp1

    print("Os dois segmentos de reta são colineares")

    if (intervalox <=0) or (intervaloy <=0):
        print("Há interseção")

    else:
        print("Não há interseção")

elif (xp1 == yp1 or xp1 == xp2 or xp1 == yp2 or xp1 == xp3 or xp1 == yp3 or xp1 == xp4 or xp1 == yp4 or
    yp1 == xp1 or yp1 == xp2 or yp1 == yp2 or yp1 == xp3 or yp1 == yp3 or yp1 == xp4 or yp1 == yp4 or
    xp2 == xp1 or xp2 == yp1 or xp2 == yp2 or xp2 == xp3 or xp2 == yp3 or xp2 == xp4 or xp2 == yp4 or
    yp2 == xp1 or yp2 == yp1 or yp2 == xp2 or yp2 == xp3 or yp2 == yp3 or yp2 == xp4 or yp2 == yp4 or
    xp3 == xp1 or xp3 == yp1 or xp3 == xp2 or xp3 == yp2 or xp3 == yp3 or xp3 == xp4 or xp3 == yp4 or
    yp3 == xp1 or yp3 == yp1 or yp3 == xp2 or yp3 == yp2 or yp3 == xp3 or yp3 == xp4 or yp3 == yp4 or
    xp4 == xp1 or xp4 == yp1 or xp4 == xp2 or xp4 == yp2 or xp4 == xp3 or xp4 == yp3 or xp4 == yp4 or
    yp4 == xp1 or yp4 == yp1 or yp4 == xp2 or yp4 == yp2 or yp4 == xp3 or yp4 == yp3 or yp4 == xp4):

    print("Os dois segmentos de reta possuem interseção")