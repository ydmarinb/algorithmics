def selection_sort(arr:list) -> list:
    """
    Es importante tener en cuenta que el funcionamiento es similar el metodo
    de burbuja. Ademas en cada iteración se recorta el numero de elementos
    a comparar ya que el arr va quedando organizado en las primera posiciones.
    """
    for i in range(len(arr)):
        minimo = i
        for j in range(i, len(arr)):
            if arr[minimo] > arr[j]:
                minimo = j
        temporal = arr[i]
        arr[i] = arr[minimo]
        arr[minimo] = temporal
    return arr
             
print(selection_sort([4, 5, 1, 3, 4]))