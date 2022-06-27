def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1,n):
            n *= i
        return n

def combination(n,r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def bridge():
    num = int(input())
    n = []
    m = []
    for i in range(num):
        a = input()
        n.append(int(a.split(' ')[0]))
        m.append(int(a.split(' ')[1]))

    for i in range(num):
        print(combination(m[i], n[i]))

bridge()