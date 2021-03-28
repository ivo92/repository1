l1 = int(input("Digite o valor do primeiro lado do triângulo: "))
l2 = int(input("Digite o valor do segundo lado do triângulo: "))
l3 = int(input("Digite o valor do terceiro lado do triângulo:"))

#Matematicamente, a soma das medidas de dois lados é sempre maior que a medida do terceiro. Então:
if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
	print("Com base nos valores digitados a figura geométrica não pode ser um triângulo.")

#Para um triângulo ser isósceles dois de seus lados devem apresentar os mesmos valores.
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
	print("Com base nos valores digitados a figura geométrica é um triângulo isósceles.")

#Para um triângulo ser equilátero seus lados devem apresentar os mesmos valores.
elif l1 == l2 == l3:
	print("Com base nos valores digitados a figura geométrica é um triângulo equilátero.")

#Para um triângulo ser escaleno seus lados devem apresentar valores diferentes.
#Porém, para fechar o programa, um else já será suficiente.
else:
	print("Com base nos valores digitados a figura geométrica é um triângulo escaleno.")