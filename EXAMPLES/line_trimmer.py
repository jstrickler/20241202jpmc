def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object
    yield "YAHOOOOOOO"

mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in: # next(); next(); next()
    print(trimmed_line)
