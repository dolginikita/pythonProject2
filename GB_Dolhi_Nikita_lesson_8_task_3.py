def number_type(funct):
    def wrapper(x):
        print(f'{funct.__name__} ({x} : {type(x)})')
        funct(x)

    return wrapper


@number_type
def calc_cube(x):
    return x ** 3


i = calc_cube(5)