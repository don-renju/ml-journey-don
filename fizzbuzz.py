print("Welcome to FizzBuzz")
print("This program will show you 'fizz' for multiples of 3 & 'buzz' for multiples of 5 ")
number_upto = 50
for digit in range(number_upto + 1):
    if digit % 3 == 0:
        print("fizz")
    elif digit % 5 == 0:
        print("buzz")
    else:
        print(digit)