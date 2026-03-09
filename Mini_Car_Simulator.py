print('''                            WELCOME TO MINI CAR GAME
===========================================================================================================''')
print('Enter help for the menu: ')
state = False
while True:
    user_input = input('> ').lower()

    if user_input == 'help':
        print('1. "Start" - starts the car\n2. "Stop - stops the car/3. "Help" - shows help\n4. "Quit" - quits the program')
    elif user_input == 'start':
        if state:
            print('Car already started')
        else:
            state = True
            print('You have started the car')
    elif user_input == 'stop':
        if state:
            state = False
            print('You have stopped the car')
        else:
            print('car already stopped')
    elif user_input =='menu':
        print('1. "Start" - starts the car\n2. "Stop - stops the car\n3. "Help" - shows help\n4. "Quit" - quits the program')
    elif user_input == 'quit':
        break
    else:
        print('Please enter a valid input')

print('You played well!!!!! BYE')