def find_max_index(arr: list) -> int | None:
    max_value = arr[0]
    max_index = 0

    for index in range(1, len(arr)):
        if arr[index] > max_value:
            max_value = arr[index]
            max_index = index

    return max_index


def selection_sort(arr: list) -> None:
    sorted_list = []
    for _ in range(0, len(arr)):
        max_index = find_max_index(arr)
        sorted_list.append(arr.pop(max_index))

    return sorted_list


list_to_sort = [5, 15, 10, 25, 45, 0, 2]

sorted_list = selection_sort(list_to_sort)
print("sorted_list:", sorted_list)
