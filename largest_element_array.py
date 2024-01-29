''' Brute force
def largest_element(arr):
    n = len(arr)
    arr.sort()
    return arr[n-1]
array = [0,32,1,23,90]
large = largest_element(array)
print(large) '''

def largest_element(arr):
    largest = arr[0]
    for i in range(0,len(arr)):
        if largest < arr[i]:
            largest= arr[i]
    return largest
array = [0,32,1,90,23]
large = largest_element(array)
print(large)
