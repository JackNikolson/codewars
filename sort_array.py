# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odd_numbers = sorted([i for i in source_array if i%2 != 0])
    result = []
    counter = 0

    for x in source_array:
        if x % 2 != 0:
            result.append(odd_numbers[counter])
            counter += 1
        else:  
            result.append(x)
    
    return result

            
print(sort_array([5, 3, 2, 8, 1, 4]))