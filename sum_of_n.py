def sum_of_n(n,i,sum):
    if (i > n):
        print(sum)
        return
    sum = sum+i
    sum_of_n(n,i+1,sum)
initial_sum = 0
number = int(input("Please enter the number of terms"))
sum_of_n(number,1,initial_sum)