for n in range(2, 10):
    for k in range(2, n):
        if n % k == 0:
            print(n, 'equals', k, '*', n//k)
            break
    
    else:
        print(n, 'is prime number')