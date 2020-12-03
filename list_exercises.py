def main():
    numbers = []
    for i in range(1,6):
        Num = int(input('input number {} :'.format(i)))
        numbers.append(Num)
    print('the first number is {}'.format(numbers[0]))
    print('the last number is {}'.format(numbers[-1]))
    print('the smallest number is {}'.format(min(numbers)))
    print('the largest number is {}'.format(max(numbers)))
    print('the average of the numbers is {}'.format(sum(numbers)/len(numbers)))
if __name__ == '__main__':
    main()