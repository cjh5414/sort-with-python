def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    

if __name__ == '__main__':
    arr = [4, 2, 1, 3, -1, 6, 5, 0]
    print('Before: ' + str(arr))
    insertion_sort(arr)
    print('After: ' + str(arr))
