print("Ejercicio 4: Semáforo de revisión aduanal")
print("Nombre: Mauricio Gael de León Salazar")
print("Matrícula: 2239897")
print()

# Pedimos los datos del embarque y de la empresa
valor = float(input("Valor del embarque en dólares: "))
primera = input("¿Es la primera vez que la empresa importa? (si/no): ")
certificada = input("¿La empresa está certificada como confiable? (si/no): ")
documentos = input("¿Los documentos están completos? (si/no): ")
perecedero = input("¿La mercancía es perecedera (fruta, flores, carne)? (si/no): ")

# Convertimos a True o False
es_primera = primera == "si"
es_certificada = certificada == "si"
documentos_ok = documentos == "si"
es_perecedero = perecedero == "si"

print()
print("===== SEMÁFORO ADUANAL =====")

# ROJO sí: Los documentos NO están completos
# o (es caro O es su primera vez) y además NO está certificada
if not documentos_ok or ((valor > 50000 or es_primera) and not es_certificada):
    print("🔴 Semáforo ROJO: el embarque pasa a revisión física.")
    días = 3
# and: rojo Y perecedero: La mercancía se puede echar a perder
elif es_perecedero:
    print("⚠️ Mercancía perecedera: solicita revisión prioritaria.")
    días = 1
else:
    print("🟢 Semáforo VERDE: el embarque pasa sin revisión.")
    días = 0

# Cada día en la aduana cuesta $500 de almacenaje
almacenaje = días * 500
print("Días estimados en la aduana:", días)
print("Costo de almacenaje: $", almacenaje, sep="")