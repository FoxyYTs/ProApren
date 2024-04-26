def bucket_sort(arr):
    # Encuentra el valor máximo y mínimo en el arreglo
    max_val = max(arr)
    min_val = min(arr)
    n = len(arr)
    
    # Número de cubetas, se puede ajustar según la necesidad
    num_buckets = 10
    bucket_range = (max_val - min_val) / num_buckets

    # Inicializa las cubetas
    buckets = [[] for _ in range(num_buckets)]

    # Coloca cada elemento en la cubeta correspondiente
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index != num_buckets:
            buckets[index].append(num)
        else:
            buckets[num_buckets - 1].append(num)

    # Ordena cada cubeta individualmente (puede usar otro algoritmo de ordenamiento)
    for i in range(num_buckets):
        buckets[i].sort()

    # Concatena las cubetas ordenadas para obtener el arreglo ordenado
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Ejemplo de uso
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Arreglo original:", arr)
print("Arreglo ordenado:", bucket_sort(arr))
