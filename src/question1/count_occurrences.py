def count_occurrences(arr, target):
    return (
        0
        if len(arr) == 0
        else (1 if arr[0] == target else 0) + count_occurrences(arr[1:], target)
    )


test_array = [1, 2, 3, 4, 2, 2, 5, 2, 6]
target_element = 2
print(f"Test Case 1: The element {target_element} appears {count_occurrences(test_array, target_element)} times in the array.")


test_array = [1, 3, 4, 5, 6]
target_element = 3

print(f"Test Case 2: The element {target_element} appears {count_occurrences(test_array, target_element)} times in the array.")


test_array = []
target_element = 4

print(f"Test Case 3: The element {target_element} appears {count_occurrences(test_array, target_element)} times in the array.")
