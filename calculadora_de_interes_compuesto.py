periodos = int(input("Ingresa la cantidad de peridos que quieres calcular: "))
dinero = float(input("Ingresa la cantidad de dinero que quieres calcular: "))
porcentaje = float(input("Ingresa el porcentaje de cada periodo "))
total = 0 
for i in range(periodos):
    calculo = (porcentaje * dinero) / 100
    total += dinero + calculo
    totaldinero = total / 2
    print("Este es el total de todo:  " + str(totaldinero))