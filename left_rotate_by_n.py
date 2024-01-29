
def left_rotate(arr,n):
    size = len(arr)
    n = n % size
    temp = [0] * n
    for i in range(0,n):
        temp[i] = arr[i]
    for i in range(0,size-n):
        arr[i] = arr[n+i]
    for i in range(0,n):
        arr[size-i-1] = temp[n-i-1]
    return arr
print(left_rotate([1,2,3,4,5,6,7,8],20))