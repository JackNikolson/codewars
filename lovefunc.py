# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc(flower1, flower2):
    return True if (flower1 % 2 == 0 and flower2 % 2 == 1 ) or (flower1 % 2 == 1 and flower2 % 2 == 0 ) else False

print(lovefunc(2, 2))