import time
start = time.time()

n, k = map(int, input().split())

result = 0

while (n > 1):
    a = (n // k) * k
    result += n-a
    n = a

    if n < k:
        break
    
    n //= k
    result += 1 

result += (n-1)
print(result)
print("time :", time.time() - start)