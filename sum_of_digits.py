# https://www.codewars.com/kata/541c8630095125aba6000c00/

def digital_root(n):
    x = sum(int(i) for i in str(n))
    if x > 9:
       return digital_root(x)
    return x

print(digital_root(22233))
