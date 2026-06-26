def print_array(a):
    print(*a)


def selection_sort(a, n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
         if a[j] < a[min_index]:
            min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
selection_sort(a, n)
