arr = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()

for i in range(arr[1]):
    a[0] = a[1] = a[0] + a[1]
    a.sort()

print(sum(a))