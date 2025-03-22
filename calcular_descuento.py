# Creación de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamadas a la función desde el programa principal
monto1 = 100.0  # Monto total de la compra
monto2 = 200.0  # Otro monto total de compra
descuento1, monto_final1 = calcular_descuento(monto1)  # Usando el valor predeterminado
descuento2, monto_final2 = calcular_descuento(monto2, 20)  # Usando un porcentaje personalizado

# Mostrando los resultados
print(f"Monto inicial: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")
print(f"Monto inicial: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")
