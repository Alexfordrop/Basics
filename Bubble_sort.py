def bubble_sort(array):
    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array [j - 1] > array[j]:
                tmp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = tmp

    return array

numbers = [4, 2, 12, 6, 1, 95]
sorted_numbers = bubble_sort(numbers)

print(sorted_numbers)