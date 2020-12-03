def main():
    # part 1:
    numbers = []
    for i in range(1,6):
        Num = int(input('input number {} :'.format(i)))
        numbers.append(Num)
    print('the first number is {}'.format(numbers[0]))
    print('the last number is {}'.format(numbers[-1]))
    print('the smallest number is {}'.format(min(numbers)))
    print('the largest number is {}'.format(max(numbers)))
    print('the average of the numbers is {}'.format(sum(numbers)/len(numbers)))

    # part 2:
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input('enter your name ')
    if name in usernames:
        print('Access granted')
    else:
        print('Access denied')
if __name__ == '__main__':
    main()