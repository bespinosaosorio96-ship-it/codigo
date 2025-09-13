def numHuevo():
    cantidad=int(input("cuantos huevos pone:"))
    while cantidad<0:
        mensajeError("valor invalido para cantidad")
        cantidad=int(input("cuantos huevos pone:")) 
    return cantidad

def alturaGallina():
    altura=float(input("ingresa la altura de la gallina"))
    while altura<0:
        mensajeError("valor invalido para altura")
        altura=float(input("ingresa la altura de la gallina"))
    return altura

def pesoGallina():
    peso=float(input("ingrese el peso de la gallina"))
    while peso<0:
        mensajeError("valor invalido para peso")
        peso=float(input("ingrese el peso de la gallina"))
    return peso
    
def calidadGallina(calidad):
    sumaCalidad=0
    for i in range(1,calidad+1):
        resultado=pesoGallina()*alturaGallina() / numHuevo()
        return resultado

def calcularPrecio(promedio):
    if promedio<0.5:
        return 1000
    elif promedio>=0.5 and promedio<2:
        return 2000
    elif promedio>=2 and promedio<4:
        return 3000
    else:
        return 4000    

def mensajeError(mensaje):
    print("\n>> Error. Valor inválido:", mensaje)
    input("Presione una tecla para continuar")


def leerCantidadGallinas():
    n=int(input("ingrese cantidad de gallinas:"))
    while n<1:
        mensajeError("valor invalido para n")
        msg=int(input("ingrese cantidad de gallinas:"))
        return msg
        



n = leerCantidadGallinas()
suma = 0
for i in range(n):
    suma = suma + calidadGallina()
promedio = suma / n
precio = calcularPrecio(promedio)
print("el precio del huevo es:", precio)