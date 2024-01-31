def leaders(arr):
    temp = []
    max = arr[len(arr)-1]
    temp.append(max)
    for i in range(len(arr)-1,-1,-1):
        if(max < arr[i]):
            max = arr[i]
            temp.append(max)
    return temp
print(leaders([10,22,12,3,0,6]))
        

