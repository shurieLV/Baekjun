nk = list(map(int, input().split()))
circle = []
p = []

for i in range(1,nk[0] + 1):
    circle.append(i)
print(circle)
n = nk[1] - 1
while 1:
    while n >= len(circle):
        n -= nk[1]
    p.append(circle[n])
    circle.pop(n)
    n += nk[1]

    if len(p) == nk[0]:
        break
    print(p, n)

print(p)