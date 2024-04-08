import re

input_str = input("Type the input string: ")
filtered_str = re.sub(r'[^a-zA-Z]', '', input_str)
freq = {}

for char in filtered_str:
    # Initialize the count for the character if not present
    if char not in freq:
        freq[char] = 0
    # Increment the count for the character
    freq[char] += 1

# Iterate over key-value pairs and print them
for char, count in freq.items():
    print(char + " " + str(count))
