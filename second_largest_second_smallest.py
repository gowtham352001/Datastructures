def second_smallest(arr):
    small = float('inf')
    second_small = float('inf')
    for i in range(0,len(arr)):
        if small > arr[i]:
            second_small = small
            small = arr[i]
        elif second_small > arr[i] and arr[i] != small:
            second_small = arr[i]
    return second_small

def second_largest(arr):
    large = float('-inf')
    second_large = float('-inf')
    for i in range(0,len(arr)):
        if large < arr[i]:
            second_large = large
            large = arr[i]
        elif second_large < arr[i] and arr[i] != large:
            second_large = arr[i]
    return second_large

print(second_smallest([1,89,0,34,2]))
print(second_largest([1,89,0,34,2]))
    