def val_cheker(funct):
    def wrapper(x):
        try:
            if x > 0:
                return funct(x)
            else:
                raise ValueError(f'ValueError: wrong val {x}')
        except ValueError:
            print(f'ValueError: wrong val {x}')
    return wrapper


@val_cheker
def calc_cube(x):
    return x ** 3


i = calc_cube(5)
print(i)