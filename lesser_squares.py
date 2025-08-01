# function for calculation linear approximation with method of least squares

def linear_approximation(x, y):
    if not x or not x:
        return "empty value for x or y"
    
    if len(x) != len(y):
        return "different length of arrays x and y"
    
    sum_x_y = sum(map(lambda x, y: x * y, x, y))
    sum_x = sum(x)
    sum_y = sum(y)
    sum_square_x = sum(map(lambda x: x*x, x))

    a = (len(x)* sum_x_y - sum_x * sum_y)/((len(x) * sum_square_x) - (sum_x * sum_x))
    b = (sum_y - a * sum_x)/len(x)

    predicted_value = a*(len(x)+1) + b
    return predicted_value

print(linear_approximation(
    [1, 2, 3, 4, 5], 
    [3.9, 4.9, 3.4, 1.4, 1.9])
)

