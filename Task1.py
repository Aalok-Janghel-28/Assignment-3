
n = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
    
result = factorial(n)
    


print('The factorial of 5 is', result)