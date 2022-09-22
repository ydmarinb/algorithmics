def bubble_sort(arr:list) -> list:
    """
    i va decreciendo de uno en uno con el proposito de evitar la comparacion 
    con el ultimo elemento ya que tenemos la certeza de que es el mayor de la lista.
    Ademas se crea una variable que dispara la finalización si en alguna interación
    no se encuentran elementos para intercambiar(significa el el arr ya esta ordenado)
    """
    for i in range(len(arr),-1,-1):
        no_cambiar = True
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                temporal = arr[j] # 5
                arr[j] = arr[j+1] # 1
                arr[j+1] = temporal
                no_cambiar = False
        if no_cambiar:
            return arr
    return arr

    
    

print(bubble_sort([4, 5, 1, 3, 4]))