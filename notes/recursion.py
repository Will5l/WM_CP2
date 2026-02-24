for num in range(1,11):
    if num % 2 == 0:
        print(num)

even = []

num = 7
sum = 1

for x in range(1,num+1):
    sum *= x
print(f"Loop: {sum}")

def factorial(n):
    if n == 1: return 1 #Base case
    return n * factorial(n-1)

print(f"Recursion: {factorial(num)}")

fib = [1,1]

for i in range(1,11):
    fib.append(fib[i-1] + fib[i])

print(f"Loop: {fib}")

numbers = []
def fibonacci_seq(n):
    #numbers.append(n)
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)
    
print(f"Recursion: {fibonacci_seq(12)}")