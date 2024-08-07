# Write a function bar(n) that returns a list of functions. Each function should be created by a nested closure and should multiply its argument by the corresponding index. Verify the closures by inspecting their __closure__ attributes.

def bar(n):
    functions = []
    for i in range(n):
        def multiplier(x, index=i):
            return x * index
        functions.append(multiplier)
    
    return functions

result = bar(6)

for index, func in enumerate(result):
    print(f"Function {index}:")
    print(f"  Result of func(10): {func(10)}")
    print(f"  __closure__: {func.__closure__}")