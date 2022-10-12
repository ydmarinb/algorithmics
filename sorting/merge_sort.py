def merge(arr1:list, arr2:list) -> list:
    """Tomas dos array ordernados y los concatena en un array ordenado

    Args:
        arr1 (list): array ordenado 1
        arr2 (list): array ordenado 2

    Returns:
        arr (list): Array ordenado
    """
    arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1     

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1  
        
    return arr + arr2[j:] 
        

#print(merge([1, 10, 50], [2, 14, 99, 100]))    
#print(merge([73], [72]))

def merge_sort(arr:list) -> list:
    """Recibe un array desordenado y lo devuelve ordenado

    Args:
        arr (list): array desordenado

    Returns:
        list: array ordenado
    """
    if len(arr) <= 1:
        return arr
    punto_medio = len(arr) // 2
    arr1 = merge_sort(arr[:punto_medio])
    arr2 = merge_sort(arr[punto_medio:])
    return merge(arr1, arr2)
    
print(merge_sort([10, 24, 76, 73, 72, 1, 9]))

        
        
            