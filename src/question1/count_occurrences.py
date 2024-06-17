def count_occurrences(arr, target):
    return (
        0
        if len(arr) == 0
        else (1 if arr[0] == target else 0) + count_occurrences(arr[1:], target)
    )
