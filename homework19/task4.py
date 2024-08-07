# Write a Python script that manually iterates over a list of numbers using the iter() and next() functions. This task will help you understand how Python handles iteration behind the scenes.
def manual_iter(my_list):
    iterator = iter(my_list)

    print('Start')

    while True:
        try:
            n = next(iterator)
            print(n)
        except StopIteration:
            print("End of iteration")
            break

ls = [1, 2, 3, 4, 5, 6]
manual_iter(ls)

































