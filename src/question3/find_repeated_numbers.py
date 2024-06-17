def find_repeated_numbers(B):
    B.sort()
    repeated_numbers = []

    for i in range(1, len(B)):
        if B[i] == B[i - 1]:
            if B[i] not in repeated_numbers:
                repeated_numbers.append(B[i])

    return repeated_numbers


B = [1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7]
print(find_repeated_numbers(B))