N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = set(a)
b = set(b)
c=a|b
d = list(c)
d.sort()

for i in range(len(d)):
    if i == len(d)-1:
        print(d[i])
    else:
        print(d[i], end=" ")