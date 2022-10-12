import math

def obtener_digitos(numero:int, posicion:int) -> int:
    """Recibe un número y una posición del número y retorna 
       el digito que esta en la posición pasada.

    Args:
        numero (int): Numero a descomponer.
        posicion (int): Posición del digito requerido.

    Returns:
        int: Digito del número.
    """
    return (numero // 10 ** posicion) % 10

#print(obtener_digitos(8, 4))

def contar_digitos(numero:int) -> int:
    """Calculo el número de digitos en un número.

    Args:
        numero (int): Número a calcular el número de digitos.

    Returns:
        int: Número de digitos.
    """
    if numero == 0:
        return 1
    return math.floor(math.log10(abs(numero))) + 1

#print(contar_digitos(1223444))

def mayor_digito(numeros:list) -> int:
    """Al pasar una lista de números, devuelve cual es el mayor numero
       del numero mas grandes.
       
    Args:
        numeros (list): lista con lo números al buscar digitos.

    Returns:
        int: Retorna el número mayor de digitos de toda la lista
        de números.
    """
    maximo_digitos = 0
    for numero in numeros:
        maximo_digitos = max([maximo_digitos, contar_digitos(numero)])
    return maximo_digitos
        
#print(mayor_digito([23, 567, 89, 1223444, 8999]))   
        

def radix_sort(arr:list) -> list:
    """_summary_

    Args:
        arr (list): _description_

    Returns:
        list: _description_
    """
    maximo_digito = mayor_digito(arr)
    for i in range(maximo_digito):
        bucket = {key:[] for key in range(10)}
        for j in arr:
            digito = obtener_digitos(j, i)
            bucket[digito].append(j)
        arr = sum(bucket.values(), [])
    return arr

print(radix_sort([23, 567, 89, 1223444, 8999]))