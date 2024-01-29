'''def remove_duplicates(arr):
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j=0
    for x in st:
        arr[j] = x
        j=j+1
    print(arr)
    return k
print(remove_duplicates([1,1,2,2,2]))'''

'''optimal solution in one loop'''
def remove_duplicates(arr):
    i=0
    j=1
    while(j<len(arr)):
            if arr[i] != arr[j]:
                arr[i+1] = arr[j]
                i=i+1
            j=j+1
    print(arr)
    return i+1
        
print(remove_duplicates([1,1,2,2,2,3,3,5,6,6]))   
                
