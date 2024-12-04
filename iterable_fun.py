
colors = ['red', 'purple', 'green']

for color in colors:
    print(color)
print('-' * 60)
print(f"{dir(colors) = }")

icolors = iter(colors)  # fetch iterator obj from list
print(f"{dir(icolors) = }")
print(f"{next(icolors) = }")
print(f"{next(icolors) = }")
print(f"{next(icolors) = }")
# print(f"{next(icolors) = }")

import csv
with open('DATA/knights.csv') as k_in:
    rdr = csv.reader(k_in)
    first_line = next(rdr)  # internally uses next(k_in)
    print(f"{first_line = }")
    
    line = next(k_in)
    print(f"{line = }")
    