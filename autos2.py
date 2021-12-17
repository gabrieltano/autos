#Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

#1-Ya no sabemos cuantos clientes tendremos,
#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
def calcular_precio (marca,puertas,color,ventas):
    marcas= {"FORD": 100000, "CHEVROLET": 120000, "FIAT":80000}
    puertas= {2:50000,4:65000,5:78000}
    colores= {"blanco":10000,"azul":20000,"negro":30000}
    precio= marcas[marca]+puertas[puerta]+colores[color]
    if ventas>5 and ventas<11:
        precio= precio*0.9
    elif ventas>10 and ventas<51:
        precio= precio*0.85
    elif ventas>50:
        precio= precio*0.83
    return precio
       
mas_clientes="si"
ventas=[]
marcas=[ "FORD","CHEVROLET","FIAT"]
puertas=[2,4,5]
colores=["blanco","azul","negro"]

while mas_clientes == "si":
    nombre= input("Ingrese nombre: ")
    apellido= input("Ingrese apellido: ")
    marca=""
    puerta=()
    color=""

    while marca not in marcas:
        marca=input("ingrese marcas: ")
        marca=marca.upper()
    
    while puerta not in puertas:
        puerta= int(input("Ingrese cantidad de puertas: "))
    
    while color not in colores:
        color= input("Ingrese color del vehiculo: ")
    #Precio=calcular_precio(marca,puerta,color,ventas)
    ventas.append({"nombre":nombre, "apellido":apellido,"marca":marca,"puertas":puerta,"color":color})
    mas_clientes= input("Hay mas clientes?: ")
largo= len(ventas)
for i in ventas:
    Precio=calcular_precio(marca,puertas,color,largo)
    print("la persona "+ i["nombre"]+i["apellido"]+ " compro un auto marca "+ i["marca"]+ " de "
    + str(i["puertas"])+ " puertas y color "+ i["color"]+" con un precio de $ "+ i[str(Precio)])

   