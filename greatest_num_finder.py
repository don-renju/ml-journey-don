from gratestnumfinder_logic import find_max
user_input = input("enter a list: ")
numbers = []
for num in user_input.split(","):
    if num.strip() != "":
        numbers.append(int(num))
find_max(numbers)