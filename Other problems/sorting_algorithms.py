import random


# Search algorithms
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = lst[mid]
        if item == guess:
            return mid
        elif item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Sort algorithms
def bubble_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def selection_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        ind_min = i
        item_min = lst[ind_min]
        for j in range(i+1, length):
            if item_min > lst[j]:
                ind_min = j
        item_min = lst[ind_min]
        lst[ind_min] = lst[i]
        lst[i] = item_min
    return lst


def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i):
            if a[j] > a[i]:
                a[i], a[j] = a[j], a[i]
    return a


def quicksort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    else:
        less = []
        greater = []
        equal = []
        pivot = lst[0]
        for item in lst:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                equal.append(item)
        return quicksort(less) + equal + quicksort(greater)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)/2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# RECURSION
def sum_rec(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[-1] + sum_rec(lst[:-1])


def max_element_rec(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_index = 0 if lst[0] < lst[1] else 1
        lst.pop(min_index)
        return max_element_rec(lst)


if __name__ == '__main__':
    # print binary_search(range(100), 99)
    arr = [3,2,5,1,8,6,8,4,9,0,7]
    merge_sort(arr)
    print(arr)
