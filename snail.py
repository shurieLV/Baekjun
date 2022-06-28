arr = list(map(int, input().split()))

day = (arr[2] - arr[1]) / (arr[0] - arr[1])

if (arr[2] - arr[1]) % (arr[0] - arr[1]):
    day += 1

print(int(day))