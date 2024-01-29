def print_numbers(i,n):
    if i>n:
        return
    print(i)
    print_numbers(i+1,n)
number = int(input("Please enter the number of terms"))
print_numbers(1,number)

 