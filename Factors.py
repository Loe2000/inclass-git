def factors():
    a = int(input('Input an integer: '))
    print('The factors of ', a, ' are:')
    for x in range(a//2):
        if a % (x + 1) == 0:
            print(x + 1)
    print(a)

factors()