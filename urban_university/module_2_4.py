def IsPrime(num):
    res=True
    i=2
    for i in range(2,num):
        if num % i==0:
            res=False
            break

    return res

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]

for i in numbers:
    if(i==1):
        continue
    if (IsPrime(i)):
        primes.append(i)
    else:
        not_primes.append(i)

print(f"primes:{primes}\nnot_primes:{not_primes}")
