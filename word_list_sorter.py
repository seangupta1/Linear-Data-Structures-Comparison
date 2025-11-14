# Original file
filepath = '1000-most-common-words.txt'

# Empty list
words = []

# Load in words from original file and add to list
with open(filepath, 'r') as file:
    for line in file:
        words.append(line.rstrip())

# Sort list
words.sort()

# Print index and word
for element in words:
    print(f"{words.index(element)} | {element}")
