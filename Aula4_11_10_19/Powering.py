# Potência
def powering(x, n):
    if n == 1:
        return x
    half=0
    if n%2 == 0:
        half = powering(x, n//2)
        return half*half
    else:
        half = powering(x, (n-1)//2)
        return half*half*x

# Teste
a=2
n=5
result = powering(a,n)
print(result)