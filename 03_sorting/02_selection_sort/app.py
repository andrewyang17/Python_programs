def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)


example = [6, 7, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(example)
