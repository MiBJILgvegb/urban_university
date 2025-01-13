def is_prime(func):
    def wrapper(*args):
        n=func(*args)
        if n % 2 == 0:
            print('Составное')
            return n
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        if(d * d > n):
            print('Простое')
        else:
            print('Составное')
        return n
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)