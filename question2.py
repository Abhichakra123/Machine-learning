def find_range(number):
    if len(number) < 3:
        return "Range determination cannot be possible"
    return max(numbers) - min(numbers)

user_input = input("Enter a list of numbers : ")
numbers = list(map(int, user_input.split()))
print("Your array:", numbers)
result = find_range(numbers)
print(f"Range: {result}") 
