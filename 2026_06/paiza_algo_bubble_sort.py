def print_array(a):
    print(*a)


def bubble_sort(a, n):
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
        

        print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
bubble_sort(a, n)