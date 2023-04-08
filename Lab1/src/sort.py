import time
from multiprocessing import Pool
from src.utils import split

def merge(a):
    left, right = a
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def zipp(a):
    it = iter(a)
    return zip(it, it)

def sort(a):
    start : float = time.time()
    a_sorted = sorted(a)
    end : float = time.time()
    print(f"N={len(a)}, Tempo de ordenação: {end - start}")
    return a_sorted

def mergesort(L, k=2):
    L_splited = split(L, k)
    with Pool(k) as p:
        L_sorted = list(p.map(sort, L_splited))
    last = None
    if len(L_sorted) % 2:
        last = L_sorted.pop()
        if not L_sorted:
            return last

    while len(L_sorted) > 1:
        L_zipp = zipp(L_sorted)
        with Pool(int(k/2)) as p:
            L_sorted = list(p.map(merge, L_zipp))

    L_sorted = L_sorted[0]
    if last:
        L_sorted = merge([L_sorted, last])
    return L_sorted