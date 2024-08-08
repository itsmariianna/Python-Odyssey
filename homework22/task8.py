# Իրականացնել @memoize դեկորատոր, որը պահում է իր դեկորացրած ֆունկցիայի արդյունքները: Դեկորատորը պետք է պահպանի ֆունկցիայի կանչի արդյունքները իրենց արգումենտներով և վերադարձնի պահված արդյունքը, երբ նույն արգումենտները փոխանցվեն:

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


@memoize
def my_func(a, b):
    print(f'Some of {a} and {b} is:')
    return a + b

print(my_func(7, 8))
print(my_func(5, 6))
print(my_func(7, 8))