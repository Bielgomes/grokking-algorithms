def binary_search(ordered_list: list, number: int) -> int | None:
    start = 0
    end = len(ordered_list) - 1

    while start <= end:
        mid = (start + end) // 2
        peak_number = ordered_list[mid]

        if peak_number == number:
            return mid

        if peak_number > number:
            end = mid - 1
        else:
            start = mid + 1

    return None


ordered_list = [1, 5, 10, 18, 21, 45, 56, 78, 128]

print(binary_search(ordered_list, 1))
print(binary_search(ordered_list, 21))
print(binary_search(ordered_list, 78))
print(binary_search(ordered_list, 100))
