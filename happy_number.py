def is_lucky(number):
    if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
        print('You got a lucky ticket!')
    else:
        print('Oops. Not today')


num = input()
is_lucky(num)