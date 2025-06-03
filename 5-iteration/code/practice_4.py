def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

print('Smallest:', min([6, 1, 12, 34, 12, 15]))