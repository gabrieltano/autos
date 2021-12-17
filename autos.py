#5 clientes van a pedir un auto, debe preguntarsele:
#*Nombre y apellido del comprador.
#*Marca
#*Puertas
#*Color
#marca: Ford $100000
#Chevrolet: $120000
#Fiat: $80000
#puertas: 2: $50000
#4: $65000
#5: $78000

#color: Blanco: $10000 
#Azul: $20000
#Negro: $30000

for i in range (2) :                  
    nombre= input("ingrese nombre y apellido del comprador: ")

    marca= input("ingrese la marca del vehiculo: ")
    if marca == "Ford":
        precio_marca= 100000
    elif marca == "Chevrolet": 
        precio_marca= 120000
    elif marca == "Fiat":
        precio_marca=80000

    puertas= input("ingrese cantidad de puertas: ")
    if puertas == "2":
        precio_puertas= 50000
    elif puertas == "4":
        precio_puertas= 65000
    elif puertas == "5":
        precio_puertas= 78000

    color= input("ingrese color requerido: ")
    if color == "blanco":
        precio_color= 10000
    elif color == "azul":
        precio_color= 20000
    elif color == "rojo":
        precio_color= 30000
    
    precio_final= precio_marca+ precio_puertas+ precio_color
    print("la persona:" + str(precio_final))
    #mejor el ultimo


