def GCD(a,b):
    if a % b == 0:
        return b
    else:
        GCD(b, a % b)

if __name__ == "__main__":
    a, b = list(eval(input("Please enter two integers to find their Greatest Common Denominator: ")))
    print("The greatest common denominator between ", a, " and ", b, " the greatest common denomiator ", GCD(a,b))