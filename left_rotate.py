def left_rotate(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr
print(left_rotate([1,2,3,4,5]))