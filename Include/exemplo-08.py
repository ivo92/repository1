serie_ndvi = [0.3, -0.3, 0.2, None, 0.9, 0.8, 0.8, None, 0.2, 0.2]

valores_inválidos = serie_ndvi.count(None)
valores_válidos = len(serie_ndvi) - serie_ndvi.count(None)

print(f"A lista apresenta {valores_inválidos} valores inválidos e {valores_válidos} valores válidos")