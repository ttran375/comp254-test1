def count_occurrences(arr, target):
    if len(arr) == 0:
        return 0
    else:
        if arr[0] == target:
            return 1 + count_occurrences(arr[1:], target)
        else:
            return count_occurrences(arr[1:], target)


test_array = [1, 2, 3, 4, 2, 2, 5, 2, 6]
target_element = 2
count = count_occurrences(test_array, target_element)
print(f"Test Case 1: The element {target_element} appears {count} times in the array.")


test_array = [1, 3, 4, 5, 6]
target_element = 2
count = count_occurrences(test_array, target_element)
print(f"Test Case 2: The element {target_element} appears {count} times in the array.")


test_array = []
target_element = 2
count = count_occurrences(test_array, target_element)
print(f"Test Case 3: The element {target_element} appears {count} times in the array.")
