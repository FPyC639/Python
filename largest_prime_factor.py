def largest_prime_factor(n):
    blank_ls = list()
    blank_ls2 = list()
    if n < 2:
        return 0
    else:
        for i in range(2,n-1):
            if n % i == 0:
                print(i)
                blank_ls.append(i)
        
        matching_list = list(map(is_prime,blank_ls))
        print(matching_list)
        indexes = [i for i, x in enumerate(matching_list) if x]
        blank_ls2 = [blank_ls[i] for i in indexes]
        return max(blank_ls2)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Ans 1 -- ", largest_prime_factor(15))  # should print 5
print("Ans 2 -- ", largest_prime_factor(28))  # should print 7
print("Ans 3 -- ", largest_prime_factor(1))   # should print 0
assert largest_prime_factor(15) == 5
assert largest_prime_factor(28) == 7
assert largest_prime_factor(1) == 0