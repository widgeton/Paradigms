def binary_search(lst: list[int], val: int) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        middle = start + (end - start) // 2
        if val == lst[middle]:
            return middle
        if val < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


print(binary_search([i for i in range(1, 40)], 25))
