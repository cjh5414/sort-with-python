def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                 min_index = j

        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp

    
if __name__ == '__main__': 
    arr = [4, 2, 1, 3]
    print('Before: ')
    print(arr)
    selection_sort(arr)
    print('\nAfter: ')
    print(arr)

