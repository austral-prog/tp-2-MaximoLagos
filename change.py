# Solicitar datos al usuario
print("Ingresar gasto:")
gasto = float(input())

print("Dinero recibido")
pagado = float(input())

# Calcular el vuelto
vuelto = pagado - gasto
pesos = int(vuelto)
centavos = round((vuelto - pesos) * 100)

# Mostrar el informe
print("\nVuelto\n")
print("Pesos:")
print(pesos)
print("Centavos:")
print(centavos)
