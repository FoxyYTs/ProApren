def counting_sort(arr):
    # Encontrar el valor máximo en el arreglo
    max_val = max(arr)
    
    # Inicializar un arreglo de conteo con el tamaño suficiente para almacenar
    # el conteo de ocurrencias de cada elemento
    count_arr = [0] * (max_val + 1)
    
    # Contar las ocurrencias de cada elemento en el arreglo original
    for num in arr:
        count_arr[num] += 1
    
    # Reconstruir el arreglo ordenado utilizando las ocurrencias contadas
    sorted_arr = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sorted_arr.append(i)
    
    return sorted_arr

# Ejemplo de uso
arr = [5, 2, 2, 9, 3, 3, 1]
print("Arreglo original:", arr)
print()
sorted_arr = counting_sort(arr)
print("Arreglo ordenado:", sorted_arr)