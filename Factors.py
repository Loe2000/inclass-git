def factors(a):
    for x in range(a//2):
        if a % (x + 1) == 0:
            print(x + 1)
    print(a)

factors(7)
factors(12)