def summation(n):
    if n>0:
        return n + summation(n-1)
    else:
        return 0
n = int(input('Use a number to test recursion: '))
print('The summation of all the values from 0 to ',n, ' is ', summation(n))