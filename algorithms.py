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


if __name__ == '__main__':
    # print binary_search(range(100), 99)
    print bubble_sort([3,2,5,1,8,6,4,9,7])
