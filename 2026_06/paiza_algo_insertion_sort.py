def print_array(a):
    print(*a)


def insertion_sort(a, n):
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
insertion_sort(a, n)
