
my_list = []
inp_data = 0
count = 1


class OwnError(ValueError):
    def __init__(self, val):
        self.val = val


while inp_data != 'stop':
    inp_data = input(f'Введите {count}-е число или для отсановки "stop": ')
    try:
        if inp_data.isdigit() or inp_data.replace('.', '').isdigit():
            my_list.append(inp_data)
            count += 1
        elif inp_data.lower() == 'stop':
            continue
        else:
            raise OwnError('Вы ввели не число!')
    except OwnError as err:
        print(err)

print(f'Ваши числа: {my_list}')