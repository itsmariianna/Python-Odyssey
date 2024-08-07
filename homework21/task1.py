# Create a lambda function that returns another lambda function which multiplies its argument by a given factor.
func = lambda x: lambda y : x * y 
result = func(4)
triple = result(3)
print(triple)