temp = [1,2,3,4,5]
def add_numbers(a):
    if not a:
        return 0
    else:
        b = a.pop()
        return b + add_numbers(a)
assert sum(temp) == add_numbers(temp)
print("Check sums are correct.")