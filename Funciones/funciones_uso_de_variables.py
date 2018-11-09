# Variables localesn Sólo existen en la propia función
def v_local():
    a = 2
    print(a)
    return

a = 5
v_local()
print(5)
print("--------------------")

# Las variables locales sólo existen en la propia función y no son accesibles desde niveles superiores
def funcion():
    a = 2
    print(a)
    return

funcion()
print(a)
print("--------------------")

#Variables libres globales o no locales
def funcion1():
    print(a)
    return

a = 5
funcion1()
print(a)
print("--------------------")

def subrutina():
    def sub_rutina():
        print(a)
        return

    a = 3
    sub_rutina()
    print(a)
    return

a = 5
subrutina()
print(a)
