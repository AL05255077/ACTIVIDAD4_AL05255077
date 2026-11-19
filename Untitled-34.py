print("Ejercicio 2: ¿Quién paga el flete y el seguro?")
print("Nombre: Mauricio Gael de León Salazar")
print("Matrícula: 2239897")
print()

# Pedimos los datos del contrato
incoterm = input("Escribe el Incoterm en MAYÚSCULAS (EXW, FOB, CIF, CIP, DAP): ")
valor = float(input("Valor de la mercancía en dólares: "))
transporte = input("Transporte en MAYÚSCULAS (MARITIMO, AEREO, TERRESTRE): ")
fragil = input("¿La mercancía es frágil? (si/no): ")

# Convertimos la respuesta en True o False
es_fragil = fragil == "si"

print()
print("===== RESUMEN DEL CONTRATO =====")

# not + or: si NO es ninguno de los 5 Incoterms, el dato está mal
if not (incoterm == "EXW" or incoterm == "FOB" or incoterm == "CIF" or incoterm == "CIP" or incoterm == "DAP"):
    print("❌ Incoterm no válido. Revise que esté en MAYÚSCULAS.")
else:
    # or: con EXW o FOB, el Flete internacional lo paga el COMPRADOR
    if incoterm == "EXW" or incoterm == "FOB":
        print("📦 Flete internacional: Lo paga el COMPRADOR.")
    else:
        print("📦 Flete internacional: Lo paga el VENDEDOR.")

    # or: con CIF o CIP, el seguro lo contrata el VENDEDOR
    if incoterm == "CIF" or incoterm == "CIP":
        # or: si es frágil O va por barco, el riesgo es mayor
        if es_fragil or transporte == "MARITIMO":
            porcentaje = 2
        else:
            porcentaje = 1

        seguro = valor * porcentaje / 100
        print("🛡️ Seguro: Lo contrata el VENDEDOR.")
        print("📊 Porcentaje del seguro: ", porcentaje, "%", sep="")
        print("💰 Costo estimado del seguro: $", seguro, sep="")
    else:
        print("🛡️ Seguro: NO lo contrata el vendedor. Lo decide el COMPRADOR.")