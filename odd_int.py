# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    for int in seq:
        if seq.count(int) % 2 == 1:
            return int

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))



