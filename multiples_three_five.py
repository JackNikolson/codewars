# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    result = []
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            result.append(num)
    
    return sum(result)

print(solution(10))
