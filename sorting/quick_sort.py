#def quick_sort(arr:list) -> list:
def pivote(arr:list, inicio=0, fin=0) -> list:
    """Recibe un array desordenado y una pocisión de inicio de validación.
       Y pone a la derecha todos los elementos que sean menores que el elemento
       en la posición indicada y la izquierda todos los que sean mayores.

    Args:
        arr (list): array desordenado.

    Returns:
        list: Lista con los elemetos menores al indicado unicados a la derecha.
    """
    if fin == 0:
        fin = len(arr)
    pivote = arr[inicio]
    indice_cambio = inicio
    for i in range(1, fin):
        if pivote > arr[i]:
            indice_cambio += 1
            temp = arr[indice_cambio]
            arr[indice_cambio] = arr[i]
            arr[i] = temp
    temp = arr[indice_cambio]
    arr[indice_cambio] = pivote
    arr[inicio] = temp
    return indice_cambio
    
#print(pivote([4, 8, 2, 1, 5, 7, 6, 3]))
 

def quick_sort(arr:list, izquierda=0, derecha=0) -> list:
    """Recibe un array desordenado y la devuelve organizado de manera
    ascendente
    
    Args:
        arr (list): array desordenado.

    Returns:
        list: Lista con los elementos ordenados.
    """ 
    if izquierda < derecha:
        if derecha == 0:
            derecha = len(arr)
        indice_pivote = pivote(arr, inicio=izquierda, fin=derecha)
        quick_sort(arr, izquierda, indice_pivote)
        quick_sort(arr, indice_pivote, derecha)
    return arr

      
      
print(quick_sort([4, 8, 2, 1, 5, 7, 6, 3]))     
        
    