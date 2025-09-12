def numHuevo():
    cantidad=int(input("cuantos huevos pone:"))
    return cantidad

def alturaGallina():
    altura=float(input("ingresa la altura de la gallina"))
    return altura

def pesoGallina():
    peso=float(input("ingrese el peso de la gallina"))
    return peso
    
def calidadGallina(calidad):
    sumaCalidad=0
    for i in range(1,calidad+1):
        resultado=pesoGallina()*alturaGallina() / numHuevo()
        return resultado

def calcularPrecio(promedio):
    




def mensajeError(msg):
    print("\n>> Error. Valor inválido")
    input("Presione una tecla para continuar")
    print()


def leerCantidadGallinas():
    n=int(input("ingrese cantidad de gallinas:"))
    while n<1:
        mensajeError("valor invalido para n")
        n=int(input("ingrese cantidad de gallinas:"))
        return n
        



n = leerCantidadGallinas()
suma = 0
for i in range(n):
    suma = suma + calidadGallina()
promedio = suma / n
precio = calcularPrecio(promedio)
print("el precio del huevo es:", precio)