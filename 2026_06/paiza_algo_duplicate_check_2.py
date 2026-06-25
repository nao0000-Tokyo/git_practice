N = int(input())
a = list(map(int, input().split()))
seen = set()

for x in a:
    if x in seen:
        print("Yes")
    else:
        print("No")
    seen.add(x)