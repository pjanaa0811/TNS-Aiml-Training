arr = [10,20,10,30,20,10]

count = {}

for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

most = arr[0]

for num in count:
    if count[num] > count[most]:
        most = num

print("Most repeated:", most)