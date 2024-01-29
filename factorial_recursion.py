def factorial(i,n,fact):
    if i > n:
        print(fact)
        return
    fact = fact*i
    factorial(i+1,n,fact)
initial_fact = 1
number = int(input("Please enter the number for which you want to find the factorial"))
factorial(1,number,initial_fact)