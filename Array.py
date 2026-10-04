arr = [10,0,20,0,30,]
result = []

for num in arr:
    if num != 0:
        result.append(num)

for num in arr:
    if num == 0:
        result.append(num)

print(result)