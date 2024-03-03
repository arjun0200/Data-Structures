
#  Question 2 - How to calculcate the power of number using recursion?

def power(base, exp):
    assert int(exp) == exp, 'The exponent must be integer number only'
    if exp == 0:
        return 1
    elif base == 0:
        return 0
    elif exp < 0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)

print(power(0,-1))

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

someRecursive([4,6,8,9], isOdd)