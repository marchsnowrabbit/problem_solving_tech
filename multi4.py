import math
from itertools import combinations


def find_min_max_product(arr):
    arr_sorted = sorted(arr)
    smallest = arr_sorted[:4]
    largest = arr_sorted[-4:]

    possible_products = []

    for combination in combinations(smallest + largest, 4):
        product = combination[0] * combination[1] * combination[2] * combination[3]
        possible_products.append(product)

    max_product = max(possible_products)
    min_product = min(possible_products)

    return min_product, max_product


input_file_path = 'multi4.inp'
output_file_path = 'multi4.out'

with open(input_file_path, 'r') as file:
    test_cases = int(file.readline().strip())
    results = []

    for _ in range(test_cases):
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

        min_product, max_product = find_min_max_product(arr)
        results.append((min_product, max_product))

with open(output_file_path, 'w') as output_file:
    for min_product, max_product in results:
        output_file.write("%d %d\n" % (min_product, max_product))
