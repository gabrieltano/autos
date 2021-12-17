for i in range (2) :
    nombre= input("ingrese nombre y apellido del comprador: ")
    precio=0

    marca= input("ingrese la marca del vehiculo: ")
    if marca == "Ford":
        precio= precio+ 100000
    elif marca == "Chevrolet": 
        precio= precio+ 120000
    elif marca == "Fiat":
        precio= precio+ 80000

    puertas= input("ingrese cantidad de puertas: ")
    if puertas == "2":
        precio= precio+ 50000
    elif puertas == "4":
        precio= precio+ 60000
    elif puertas == "5":
        precio= precio+ 78000

    color= input("ingrese color requerido: ")
    if color == "blanco":
        precio= precio+ 10000
    elif color == "azul":
        precio= precio+ 20000
    elif color == "rojo":
        precio= precio+ 30000
    

    print("la persona:" + str(precio))