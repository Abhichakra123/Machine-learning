def count_pairs_sum_10(arr):
    count = 0
    counts = {}

    for num in arr:
        needed_value = 10 - num
        if needed_value in counts and counts[needed_value] > 0:
            count += 1
            counts[needed_value] -= 1
        else:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

    return count

numbers = [2, 7, 4, 1, 3, 6]
pairs = count_pairs_sum_10(numbers)
print("Pairs with sum 10:", pairs)
