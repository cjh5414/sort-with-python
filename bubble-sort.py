def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp

    
if __name__ == '__main__': 
    arr = [4, 2, 1, 3, 0, -1, 5]
    print('Before: ')
    print(arr)
    bubble_sort(arr)
    print('\nAfter: ')
    print(arr)

