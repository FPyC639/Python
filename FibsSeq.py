def Fibs(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return Fibs(a-2) + Fibs(a-1)

if __name__ == "__main__":
    ls_vals = range(0,10)
    for i in ls_vals:
        print("For the index ", i, " the Fibs Seqeunce is ", Fibs(i))