def missing_number(arr):
    for i in range(len(arr)):
        if i == len(arr)-1:
            return -1
        if arr[i]+1 != arr[i+1]:
            return arr[i]+1
print(missing_number([1,2,3,4,5,6,8]))