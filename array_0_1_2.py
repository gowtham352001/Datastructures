def array_of_012(arr):
    left = 0
    mid = 0
    right = len(arr)-1
    while(mid <= right):
        if(arr[mid]==0):
            arr[left],arr[mid]=arr[mid],arr[left]
            mid=mid+1
            left=left+1
        elif arr[mid]==1:
            mid = mid+1
        else:
            arr[mid],arr[right]=arr[right],arr[mid]
            right = right-1
    return arr
print(array_of_012([0,1,2,0,1,2]))
            
        

