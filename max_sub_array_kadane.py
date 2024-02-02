def max_sum_of_subarray(arr):
    max = arr[0]
    sum = 0
    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum = sum + arr[i]
        if(sum < 0):
            sum = 0
        if(max < sum):
            max = sum
            start = start
            end = i
    return max,start,end
array = [-2,-3,4,-1,-10,-2,5,1,-3]
a,b,c = max_sum_of_subarray(array)
print("Maximum sum = ",a)
print("Maximum sub array is ", array[b:c+1])

        
