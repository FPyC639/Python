import time
b = dict()
def Fibs(a):
    b[0] = 0
    b[1] = 1
    b[2] = 1
    for i in range(3,a+1):
        b[i]= b.get(i,b[i-2]) +b[i-1]
    return b[a]
def Fibs2(a):
    if a==0: return 0
    elif a == 1: return 1
    elif a == 2: return 1
    else: return Fibs2(a-2) + Fibs2(a-1)
begin = time.perf_counter()
print(Fibs(5))
print("The execution of the command is ", time.perf_counter()-begin)
begin1 = time.perf_counter()
print(Fibs2(5))
print("The execution of the command is ", time.perf_counter()-begin1)