def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome_index(n):
    i = 0
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n = abs(n - reversed_n)
        i += 1
        if i >= 1000:
            return -1
    return i

input_file_path = 'palindrome.inp'
output_file_path = 'palindrome.out'

results = []

try:
    with open(input_file_path, 'r') as file:
        test_cases = int(file.readline().strip())
        for _ in range(test_cases):
            n = int(file.readline().strip())
            index = find_palindrome_index(n)
            results.append(index)
except Exception as e:
    print("Error reading input file:", str(e))

try:
    with open(output_file_path, 'w') as output_file:
        for result in results:
            output_file.write("%d\n" % result)
except Exception as e:
    print("Error writing to output file:", str(e))
