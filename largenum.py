def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 4, 45, 99]))