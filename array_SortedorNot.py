def SortedorNot(arr):
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True
print(SortedorNot([1,2,2]))
