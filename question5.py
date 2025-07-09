import random

# Step 1: Generate 25 random numbers between 1 and 10
numbers = [random.randint(1, 10) for _ in range(25)]
print("Numbers:", numbers)

# Step 2: Calculate Mean
total = 0
for num in numbers:
    total += num
mean = total / len(numbers)
print("Mean:", mean)

# Step 3: Calculate Median
# First, sort the list
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
sorted_numbers = numbers
print("Sorted Numbers:", sorted_numbers)

# Find median
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
print("Median:", median)

# Step 4: Calculate Mode
frequency = {}
for num in sorted_numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find the number(s) with the highest frequency
max_freq = 0
mode = []
for num, freq in frequency.items():
    if freq > max_freq:
        max_freq = freq
        mode = [num]
    elif freq == max_freq:
        mode.append(num)

print("Mode:", mode)
