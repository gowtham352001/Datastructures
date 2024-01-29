def print_numbers(n):
    if (n < 1):
        return
    print(n)
    print_numbers(n-1)
number = int(input("Enter the number of terms"))
print_numbers(number)
