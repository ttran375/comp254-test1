def find_repeated_numbers(b):
    b.sort()
    repeated_numbers = []

    repeated_numbers = [
        b[i]
        for i in range(1, len(b))
        if b[i] == b[i - 1] and b[i] not in repeated_numbers
    ]

    return repeated_numbers
