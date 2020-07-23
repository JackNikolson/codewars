# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic(value):
    sum = 0
    exponentiation_value = len(str(value))
    for i in str(value):
        sum += int(i)**exponentiation_value
    if sum == int(value):
        return True
    else:
        return False
    
    

narcissistic(7)