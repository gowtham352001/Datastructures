def reverse_array(left,right,arr):
    if(left == right or left > right):
          print(arr)
          return
    arr[left], arr[right] = arr[right],arr[left]
    left=left+1
    right=right-1
    reverse_array(left,right,arr)
array = [1,2,3,4,5,6]
left_start = 0
right_start = len(array)-1
reverse_array(left_start,right_start,array)


