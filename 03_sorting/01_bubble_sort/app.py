def bubble_sort(arr):
    swap = True
    while swap:
        print('Bubble sort status: {}'.format(str(arr)))
        swap = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


example = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(example)

# for loop an iteration through the array inside the while loop
