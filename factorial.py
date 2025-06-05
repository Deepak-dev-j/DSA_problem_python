# a=int(input("Enter a number:"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
#     print(fact)

# factorial

def factorial(n):
    if n==1:
        return 1
    else:
         return factorial(n-1)*n
        
n=int(input("Enter a number:"))
print(factorial(n))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n - 1) * n

# Get user input outside the function
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
