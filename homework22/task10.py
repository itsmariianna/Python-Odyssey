# Python-ը չի ապահովում ֆունկցիաների գերբեռնում, որպես ներկառուցված գործիք, չենք կարող ունենալ նույն անունով ֆունկցիաներ, բայց տարբեր պարամետրերով։ Սակայն պետք է ընդօրինակել նման պահելաձև՝ օգտագործելով *args փոփոխական երկարության positional արգումենտների համար և **kwargs keyword արգումենտների համար: Իրականացնել process_data ֆունկցիա, որն իրեն այլ կերպ է պահում ՝ կախված իրեն փոխանցվող փաստարկների քանակից և տեսակից:

def process_data(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], int):
        return args[0] ** 2
    elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
        return args[0] * args[1]
    elif len(kwargs) > 0:
        result = {key:value for key, value in kwargs.items()}
        return result
    else:
        return "Something went wrong"
    
print(process_data(5))
print(process_data(5, 10))
print(process_data(name="Alice", age=30))
print(process_data(2, 4, 5, 6))