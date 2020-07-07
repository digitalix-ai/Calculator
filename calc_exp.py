# Calculator

print('\nThis is a calculator program. Please first select one number. \nThen select your desired arithmetic operator'
      ' between the symbols +, -, *, or /. Then select your second number. \nWhen you press Enter the result'
      ' will appear on the screen.\n')


x = False
while not x:
    try:
        a = int(input('Please select your first number and press enter: '))
        x = True
    except ValueError:
        print('Invalid symbol. Please provide an integer.')


b = input('Please select arithmetic operator and press enter: ')
while b != '+' and b != '-' and b != '*' and b != '/':
    b = input('Invalid symbol. Please select between +, -, *, or / and press enter: ')



x = False
while not x:
    try:
        c = int(input('Please select your second number and press enter: '))
        x = True
    except ValueError:
        print('Invalid symbol. Please provide an integer.')



if b == '+':
    print(f'\nYour result is {a + c}.')
elif b == '-':
    print(f'\nYour result is {a - c}.')
elif b == '*':
    print(f'\nYour result is {a * c}.')
else:
    print(f'\nYour result is {a / c}.')
