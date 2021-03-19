import math
print("Este programa irá calcular a distância entre duas coordenadas descritas a seguir. O valor final será descrito em km.")
coordenadax1 = float(input("Qual é o valor de x1? "))
coordenaday1 = float(input("Qual é o valor de y1? "))
coordenadax2 = float(input("Qual é o valor de x2? "))
coordenaday2 = float(input("Qual é o valor de y2? "))

coordenadax1rad = math.radians(coordenadax1)
coordenadax2rad = math.radians(coordenadax2)
coordenaday1rad = math.radians(coordenaday1)
coordenaday2rad = math.radians(coordenaday2)

distanciaxrad = math.radians(coordenadax2 - coordenadax1)
distanciayrad = math.radians(coordenaday2 - coordenaday1)

distanciafinal = 2 * 6371 * math.asin(math.sqrt((math.sin((distanciayrad/2))**2 + math.cos(coordenaday1rad) * math.cos(coordenaday2rad) * (math.sin((distanciaxrad/2)**2)))))

print(distanciafinal)