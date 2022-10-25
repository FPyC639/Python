def dig(a):
    if a // 10 != 0:
        return (a % 10) + dig(a//10)
    else:
        return a
if __name__ == "__main__":
    a = int(input("Input a integer: "))
    print("The sum of the individual digits of ", a, " is ", dig(a))