from Interfaces import List
import random

def linear_search(a: List, x):
    """
    Implements the linear search algorithm to find the index of element x in the ArrayList object a.
    Returns -100 if x is not found.
    """
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -100

def binary_search(a: List, x):
    """
    Implements the binary search algorithm to find the index of element x in the sorted ArrayList object a.
    Returns -100 if x is not found.
    """
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -100

def _merge(a0: List, a1: List, a: List) -> None:
    """
    Helper function for merge_sort. Merges two sorted ArrayLists a0 and a1 into a sorted ArrayList a.
    """
    i0 = 0
    i1 = 0
    for i in range(len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1

def merge_sort(a: List) -> None:
    """
    Implements the merge-sort algorithm to sort the ArrayList object a.
    """
    if len(a) <= 1:
        return

    m = len(a) // 2

    a0 = a[0:m]
    a1 = a[m:len(a)]
    merge_sort(a0)
    merge_sort(a1)
    _merge(a0, a1, a)

def _quick_sort_f(a: List, start, end):
    """
    Helper function for quick_sort. Implements the quick-sort algorithm with the first element as pivot.
    """
    if start >= end:
        return

    pivot = a[start]
    i = start + 1
    j = end

    while i <= j:
        if a[i] <= pivot:
            i += 1
        elif a[j] > pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    a[start], a[j] = a[j], a[start]
    _quick_sort_f(a, start, j - 1)
    _quick_sort_f(a, j + 1, end)

def _quick_sort_r(a: List, start, end):
    """
    Helper function for quick_sort. Implements the quick-sort algorithm with a random element as pivot.
    """
    if start >= end:
        return

    # Randomly select pivot element
    pivot_idx = random.randint(start, end)

    # Move pivot element to start of the array
    a[start], a[pivot_idx] = a[pivot_idx], a[start]

    # Partition the array around the pivot
    i = start + 1
    for j in range(start + 1, end + 1):
        if a[j] < a[start]:
            a[i], a[j] = a[j], a[i]
            i += 1

    # Move the pivot element to its correct position
    a[start], a[i - 1] = a[i - 1], a[start]

    # Recursively sort the left and right subarrays
    _quick_sort_r(a, start, i - 2)
    _quick_sort_r(a, i, end)

def quick_sort(a: List, p=True):
    """
    Sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as a pivot.
    Otherwise, the quick sort algorithm uses the first element as a pivot.
    """
    if p:
        _quick_sort_r(a, 0, len(a) - 1)
    else:
        _quick_sort_f(a, 0, len(a) - 1)
