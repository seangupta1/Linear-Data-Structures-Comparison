filepath = 'HW 3/1000-most-common-words.txt'

words = []

with open(filepath, 'r') as file:
    for line in file:
        words.append(line.rstrip())

words.sort()

for element in words:
    print(f"{words.index(element)} | {element}")