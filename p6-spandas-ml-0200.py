import pandas as pd 
import numpy as np

serie_amigos = ["Abril", "Barbara", "Alejandra", "Nicole", "Karla", "Matias", "Eliseo", "Samuel"]
print("<3<3<3 Serie listado de amigos NC 0200 <3<3<3")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billeteras = [20, 50, 100, 200, 500, 1000]
print("<3<3<3 Serie listado valor de billeteras MX NC 0200 <3<3<3")
amigos = pd.Series(serie_billeteras)
print(amigos)

serie_billeteras = [20, 50, 100, 200, 500, 1000]
etiquetas_billeteras = ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
print("<3<3<3 Serie listado valor de billeteras MX NC 0200 <3<3<3")
tablasbilleteras = pd.Series(serie_billeteras, index=etiquetas_billeteras)
print(tablasbilleteras)

# diccionario datafarme 
# diccionario de valor monedas y nombre 
print("<3<3<3 Datos de diccionario a DataFrame en pandas NC 0200 <3<3<3")
dic_monedas = {
    "serie_billeteras": [20, 50, 100, 200, 500, 1000],
    "etiquetas_billeteras": ["veinte", "cincuenta", "cien", "docientos", "quinientos", "mil"]
}

tablabilletes = pd.DataFrame(dic_monedas, index=["A", "B", "c", "D", "E", "F"])
print(tablabilletes)
print("<3<3<3 Casa de cambio de Alejandra Rivera Valenzuela NC = 0200 <3<3<3")