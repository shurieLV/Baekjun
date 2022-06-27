L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

count = 0
for i in range(len(S) - 1):
    if n in S :
        break
    elif  S[i] < n and n < S[i + 1]:
        count = (n - S[i]) * (S[i + 1] - n) - 1
        break
print(count)

ni = int(input())
i1 = list(map(int, input().split()))
i1.sort()
n = int(input())
count = 0
def check(a, b, c) :
    global count
    for k in range(a, b + 1) :
        for j in range(k + 1, b + 1) :
            if k <= c and j >= c :
                count += 1
for i in range(ni) :
    if i == 0 :
        check(1, i1[i] - 1, n)
    else :
        check(i1[i - 1] + 1, i1[i] - 1, n)
print(count)