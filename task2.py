def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations_count = 0

    while low <= high:
        mid = (low + high) // 2
        iterations_count += 1
        mid_value = arr[mid]

        if arr[mid] == target:
            return iterations_count, mid_value
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    upper_bound = arr[low] if low < len(arr) else None
    return iterations_count, upper_bound


if __name__ == "__main__":
    sorted_array = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.5, 3.0]
    target_value = 1.4

    result = binary_search(sorted_array, target_value)

    print(f"Елемент {target_value} знайдено за {result[0]} ітерацій.")
    print(f"Верхня межа: {result[1]}")
