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
    # print bubble_sort([3,2,5,1,8,6,4,9,7])
    print max_element_rec([3,2,5,1,8,6,4,9,7])
