def find_repeated_numbers(B):
    B.sort()
    repeated_numbers = []

    repeated_numbers = [
        B[i]
        for i in range(1, len(B))
        if B[i] == B[i - 1] and B[i] not in repeated_numbers
    ]

    return repeated_numbers
