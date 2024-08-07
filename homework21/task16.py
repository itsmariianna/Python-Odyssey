# Create a dictionary with functions to calculate the area of different geometric shapes (circle, square, rectangle, triangle). Write a function calculate_area(shape, **kwargs) that uses this dictionary to calculate the area based on the provided shape and parameters.

areas = {'circle' : lambda x: 3.14 * (x ** 2),
         'square' : lambda x: x ** 2,
         'rectangle' : lambda x, y: x * y,
         'triangle' : lambda x, y: x * y * 0.5}


def calculate_area(shape, **kwargs):
    if shape in areas:
        try:
            return areas[shape](**kwargs)
        except TypeError:
            return 'Missing argument'
    else:
        return 'There is no such shape'
    
print(calculate_area('circle', x = 7))
print(calculate_area('square', x = 5))
print(calculate_area('rectangle', x = 7, y = 9))
print(calculate_area('triangle', x = 3, y = 6))
print(calculate_area('pentagon', x = 7))
print(calculate_area('rectangle', x = 7))
