def sum1(a):
    if a == 1:
        return 1
    else:
        return 1/a + sum1(a-1)

if __name__  == "__main__":
    a = int(input("Please enter a number to calucate the summation up to: "))
    print(f"The summation up to the {a}th term is {sum1(a)}")