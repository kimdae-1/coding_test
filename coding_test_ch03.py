#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Greedy 알고리즘의 거스름돈 예제
n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)


# In[6]:


#Greedy 알고리즘의 큰 수의 법칙 예제1
import time
start_time = time.time()

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print (result)

end_time = time.time()
print("time : ", end_time - start_time)


# In[7]:


#Greedy 알고리즘의 큰 수의 법칙 예제2
import time
start_time = time.time()
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)*k) 
count += m%(k+1)

result = 0
result += (count) * first
result += (m-count)*second

print(result)
end_time = time.time()
print("time : ", end_time - start_time)


# In[14]:


#Greedy 알고리즘의 숫자 카드 게임 예제1
import time
start_time = time.time()

n, k = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)

end_time = time.time()
print("time : ", end_time - start_time)


# In[16]:


#Greedy 알고리즘의 숫자 카드 게임 예제2
import time
start_time = time.time()

n, k = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
    
print(result)

end_time = time.time()
print("time : ", end_time - start_time)


# In[17]:


#Greedy 알고리즘의 1이 될 때까지 예제1
import time
start_time = time.time()

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
        
    n //= k
    result += 1
    
while n > 1:
    n -= 1
    result += 1
    
print(result)

end_time = time.time()
print("time :", end_time - start_time)


# In[9]:


#Greedy 알고리즘의 1이 될 때까지 예제2
import time
start_time = time.time()

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
        
    result += 1
    n //= k

result += (n - 1)
print(result)

end_time = time.time()
print("time :", end_time - start_time)


# In[ ]:




