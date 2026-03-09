print('''                              BASIC CALCULATOR
========================================================================================================================================================================
What you need to know ? : This is a basic calculator only in which you could do the operations with two numbers only.Kindly request you to follow the given instructions.
The calculator has addition, substraction, multiplication, division and exponentiation''')
print('+ for addition')
print('- for substraction')
print('* for multiplication')
print('/ for division')
print('^ for exponentiation')

while True:
    num1 = int(input('Please enter a number: '))
    oper = input('Please enter a operation: ')
    num2 = int(input('Please enter a number: '))

    if oper == '+':
        print(f'= {num1 + num2}')
        break
    elif oper == '-':
        print(f'= {num1 - num2}')
        break
    elif oper == '*':
        print(f'= {num1 * num2}')
        break
    elif oper == '/':
        if num2 == 0:
            print('cant divide by zero')
        else:
            print(f'= {num1 / num2}')
            break
    elif oper == '^':
        print(f'= {num1 ** num2}')
        break
    else:
        print('Please enter a valid input')

