# 1. **Пузырьковая сортировка:**

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = [100, 10, 5, 25, 43, 1, 8]
bubble_sort(numbers)
print("1 узырьковая сортировка:", numbers)

# 2. **Быстрая сортировка:**

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers = [100, 10, 5, 25, 43, 1, 8]
sorted_numbers = quick_sort(numbers)
print("2 Быстрая сортировка:", sorted_numbers)


# 3. **Сортировка выбором:**

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [100, 10, 5, 25, 43, 1, 8]
selection_sort(numbers)
print("3 Сортировка выбором:", numbers)

# 4. **Сортировка вставками:**

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [100, 10, 5, 25, 43, 1, 8]
insertion_sort(numbers)
print("4 Сортировка вставками:", numbers)