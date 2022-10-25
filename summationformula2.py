def summationformula2(n):
    if n>0:
        return n**2 + summationformula2(n-1)
    else:
        return 0
n = int(input('Test second summation formula: '))
print('The indicated number for the second summation formula ', summationformula2(n))