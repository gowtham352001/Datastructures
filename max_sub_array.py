def max_sum_of_subarray(arr):
    max = arr[0]
    for i in range(len(arr)):
        sum = 0
        for j in range(i+1,len(arr)):
            sum = sum+arr[j]
            if(max < sum):
                max = sum
    return max
print(max_sum_of_subarray([-2,-3,4,-1,-2,1,5,-3]))
