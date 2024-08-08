# Իրականացնել դեկորատոր @measure_time, որը կչափի ֆունկցիայի կատարման և տպագրման ժամանակը: Դեկորատորը պետք է կիրառելի լինի ցանկացած ֆունկցիայի համար։

import time

def mesure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end =  time.time()
        diff = end - start
        print(f'It took {diff}')
        return result
    return wrapper

@mesure_time
def my_func(a, b):
    return a + b

print(my_func(6, 7))