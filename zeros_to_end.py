def move_zeros(arr):
    new_array = [0] * len(arr)
    j=0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            new_array[j] = arr[i]
            j=j+1
    for i in range(0,len(arr)):
        if i < j:
            arr[i] = new_array[i]
        else:
            arr[i] = 0
    return arr

print(move_zeros([1,2,3,0,0,1,0,0,9,0]))