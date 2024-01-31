def sum_of_digits(num):
    while((num//10) > 0):
        sum = 0
        while (num > 0):
            last_digit = num % 10 
            sum += last_digit
            num = num//10
        
        if (sum//10) > 0:
            print("The sum is not a single digit number so repeating the loop and the sum is", sum)
            num = sum     
    return sum
print("final sum is ", sum_of_digits(1997))

'''
def sum_of_digits(num):
    sum = 0
    while(num > 0):
        last_digit = num%10
        sum += last_digit
        num = num//10
    num = sum'''
