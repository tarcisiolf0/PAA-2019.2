# Fibonacci Naive - O(2^n)
"""
def fib_naive(n):
    if n<= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

n=10
result = fib_naive(n)
print(result)
"""
# Fibonacci Bottom-Up - O(n)
"""
def fib_n(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib_n(n-1, memo) + fib_n(n-2, memo)
    return memo[n]

memo = list()
for i in range(1000):
    memo.append(-1)
    
result = fib_n(10, memo)
print(memo)
print(result)
"""
# Fibonacci O(log(n))
"""
def mult_matrix(a, b, c):
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return

def assign(a, b):
    a[0][0] = b[0][0]
    a[0][1] = b[0][1]
    a[1][0] = b[1][0]
    a[1][1] = b[1][1]
    return

def powering(a, result, n):
    if n==1:
        assign(result, a)
        return

    half = [[1,1], [1,0]]

    if n%2 == 0:
        powering(a, half, n//2)
        mult_matrix(half, half, result)
        return
    else:
        temp = [[1,1], [1,0]]
        powering(a, half, (n-1)//2)
        mult_matrix(half, half, temp)
        mult_matrix(temp, a, result)
        return

def fib(n):
    result = [[1,1], [1,0]]
    m = [[1,1], [1,0]]
    powering(m, result,n)
    return result[0][1]

n=10
print(fib(10))
"""
