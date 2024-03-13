def add(a, b):
    c = a + b
    return c


# calculate the product of n numbers from 1 to n
def multiply(n):
    if n < 0:
        raise ValueError('No factorial for negative number')
    p = 1
    for i in range(1, n + 1):
        p *= i
    
    return p