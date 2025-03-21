'''
→ Obtener el resto de una division sin utilizar el operador mod ←
    Franz Joel Quispe Mamani
    Simulación y Modelacion - Ing. Freddy Garnica I-2025
'''

def resto_sin_modulo(a, b):
    if b == 0:
        return "ERROR: NO SE PUEDE REALIZAR LA DIVISION"

    cociente = a // b  # División entera

    print("")
    print("El cociente de la division de ", a, " y ", b, "es: ", cociente)
    resto = a - (cociente * b)
    print("El resto viene dado por la siguiente operacion: ", a, "-(",
        cociente, "*", b, ") = ", resto)
    print("")
    return resto

def resto_con_modulo(a, b):
    if b == 0:
        return "ERROR: NO SE PUEDE REALIZAR LA DIVISION"

    con_resto = a % b
    return con_resto

# Ejecucion
print("*** Obtener el resto de una division sin utilizar el operador mod ***")
print("** Simulacion y Modelacion **")
print("▬▬▬▬ Franz Joel Quispe Mamani ▬▬▬▬")
print(
    '''El modulo devuelve el resto de la división del operando izquierdo 'a' llamado dividendo
por el operando derecho 'b' llamado divisor. 
Se usa para obtener el residuo de un problema de división.
El resto de la división de a entre b SIN USAR MOD se obtiene así:
Usando la division entera que toma los valores enteros y no asi los reales de la division
    cociente = a//b ← Division entera
Para hallar el resto se multiplica el cociente obtenido por el divisor para finalmente restarse con el dividendo
    resto = a - (cociente*b)''')
print('''---Una división es inexacta cuando el resto es diferente de cero 
y el dividendo es igual al divisor por el cociente más el resto.---''')
print("")
a = int(input("→ Ingresa el dividendo (a): "))
b = int(input("→ Ingresa el divisor (b): "))

print("1. El resto SIN el operador modulo es:", resto_sin_modulo(a, b))
print("")
print("2. El resultado CON el operador modulo es: ", resto_con_modulo(a, b))
