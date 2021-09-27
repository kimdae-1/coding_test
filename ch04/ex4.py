data = input()

sum = 0
result = []

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        sum += int(i)

result.sort()
if sum != 0:
    result.append(str(sum))

print(''.join(result))