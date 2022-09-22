def insertion_sort(arr:list) -> list:
    """
    Toma un array y retorna este ordenado

    Args:
        arr (list): Array desordenado

    Returns:
        list: Array ordenado
    """
    for i in range(1, len(arr)):
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                temp = arr[j]
                arr[j] = current_value
                arr[j+1] = temp
            else:
                pass
    return arr
                
print(insertion_sort([2, 1, 9, 76, 4]))