#Datos
nombre= input("ingrese nombre")
apellido = input ("ingrese apellido")
nota_mate = int( input( "ingrese nota matematica"))
nota_literatura = int( input(" ingrese nota literatura"))
nota_fisica = int( input ("ingrese nota fisica") )


promedio = ((nota_mate+nota_fisica+nota_literatura) /3) 
print("el alumno"+nombre+ apellido +"tiene como promedio"+ str(promedio))
print(promedio)

if promedio>6:
    print("Aprobado")
    if promedio>= 9:
        print("alumno destacado")
elif 6<= promedio<= 4:
    print( "a recuperatorio")
else:
    print("insuficiente")
    
autos = ("esto es para ver solamente")
print(autos)



