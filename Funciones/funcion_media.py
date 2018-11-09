#Sacar la media de 2 numeros
def fmedia():
    media = (a+b)/2
    print(f"La media de {a} y {b} es: {media}")
    return
a = 3
b = 5
fmedia()
print("---------------------------")

def media(x, y):
    media = (x + y)/2
    print(f"La media de {x} y {y} es: {media}")
    return 

a = 3
b = 4
media(a, b)
print("Programa terminado")
print("---------------------------")

def calcular_media(x, y):
    resultado = (x + y)/2
    return resultado

a = 5
b = 6
media = calcular_media(a, b)
print(f"La media de {a} y {b} es: {media}")
print("Programa terminado")
print("---------------------------")

def calcular_media(*args):
    total = 0
    for i in args:
        total += i
    resultado = total/len(args)
    return resultado

a,b,c = 3,5,10
media = calcular_media(a,b,c)
print(f"La media de {a}, {b}, {c} es: {media}")
print("Programa terminado")
print("---------------------------")

def calcular_media(*args):
    total = 0
    for i in args:
        total += i
    resultado = total/len(args)
    return resultado

media = calcular_media(3, 5, 10)
print(f"La media es de {media}")
print("---------------------------")

def calcular_media_desviacion(*args):
    total = 0
    for i in args:
        total += i
    media = total/len(args)
    total = 0
    for i in args:
        total += (i - media)**2
    desviacion = (total/len(args))**0.5
    return media, desviacion

a,b,c,d = 3,5,10,12
media, desviacion_tipica = calcular_media_desviacion(a,b,c,d)
print(f"Datos {a}, {b}, {c}, {d}")
print(f"Media {media}")
print(f"Desviacion tipica {desviacion_tipica}")
print("Progrma terminado")
    
