n = int(input())
a = [int(x) for x in input().split()]
k = int(input())


maximum = 101

for i in range(k):
    next_maximum = -101

    for value in a:
        if value < maximum and next_maximum < value:
            next_maximum = value

    maximum = next_maximum

print(maximum)
