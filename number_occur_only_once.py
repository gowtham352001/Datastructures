
''' Using XOR 
def number_once(arr):
    number = 0
    for i in range(len(arr)):
        number = number ^ arr[i]
    return number
print(number_once([5,1,2,1,2]))'''

''' using hash map'''
def number_once(arr):
    hash = {}
    for num in arr:
        hash[num] = hash.get(num,0)+1
    for num, count in hash.items():
        if count == 1:
            return num
    return -1
print(number_once([1,2,5,5,1,2,13,1]))