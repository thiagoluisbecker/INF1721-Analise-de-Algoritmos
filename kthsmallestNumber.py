import random
import timeit
import math
import matplotlib.pyplot as plt


def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sortselection(arr, k):
    bubblesort(arr)
    return arr[k]

def partition(A, low, high, pivot):
    i = low
    for j in range(low, high):
        if A[j] == pivot:
            A[j], A[high] = A[high], A[j]
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    return i

def linearSelection(A, low, high, k):
    if low == high:
        return A[low]

    n = high - low + 1
    num_medians = math.ceil(n / 5)
    medians = []

    for i in range(num_medians):
        sub_low = low + i * 5
        sub_high = min(low + i * 5 + 4, high)

        sub_median = A[sub_low + (sub_high - sub_low) // 2]
        medians.append(sub_median)

    median_of_medians = linearSelection(medians, 0, num_medians - 1, num_medians // 2)
    pivot_index = partition(A, low, high, median_of_medians)

    if k == pivot_index - low:
        return A[pivot_index]
    elif k < pivot_index - low:
        return linearSelection(A, low, pivot_index - 1, k)
    else:
        return linearSelection(A, pivot_index + 1, high, k - (pivot_index - low + 1))



arr = [random.randint(1,10) for i in range(10)]
arr2 = [random.randint(1,10) for i in range(10)]
k = 2
print(f'arr: {arr}\narr2:{arr2}')
print(f"The {k+1}rd smallest element is {sortselection(arr,k)} (by sortSelection)")
print(f"The {k+1}rd smallest element is {linearSelection(arr2, 0, len(arr2) - 1, k)} (by linearSelection)")


print(f'Sorted arrays: \narr: {arr}\narr2: {arr2}\n\n\n')

"""
steps = 1000
start = 1000
end = 5000
sizes = range(start, end, steps)
num_instances = 10
results_linear = []
results_sort = []
print(f'Running both algorithms starting by a {start} sample and ending at {end} size\n\n')

for n in sizes:
    total_time_linear = 0
    total_time_sort = 0
    print(n)
    for _ in range(num_instances):
        A = [random.randint(1, 100000) for x in range(n)]

        sort_time = timeit.timeit(lambda: sortselection(A, n // 2), number=1)
        linear_time = timeit.timeit(lambda: linearSelection(A, 0, len(A)-1, n // 2), number=1)
        total_time_sort += sort_time
        total_time_linear += linear_time

    avg_time_sort = total_time_sort / num_instances
    avg_time_linear = total_time_linear / num_instances

    results_sort.append(avg_time_sort)
    results_linear.append(avg_time_linear)


plt.figure(figsize=(10, 6))
plt.plot(sizes, results_sort, marker='o', label='SortSelection')
plt.plot(sizes, results_linear, marker='o', label='linearSelection')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Tempo Médio de Execução (s)')
plt.title('Comparação de Desempenho: LinearSelection vs. SortSelection')
plt.legend()
plt.grid(True)
plt.show()
"""
