def myfactorial(n):
    if n>1:
        return n*myfactorial(n-1)
    else:
        return 1

num = int(input('input positive integer: '))
print(f'{num}\'s factorail is {myfactorial(num)}.')
