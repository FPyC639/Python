def fibsseq(n):
    if n>1:
        return fibsseq(n-1)+fibsseq(n-2)
    elif n== 1:
        return 1
    else:
        return 0
#n = int(input('Enter your term: '))
#number = fibsseq(n)
#print(number)
numberstack = []
for i in range(0,5):
    numberstack.append(fibsseq(i))
print(numberstack)