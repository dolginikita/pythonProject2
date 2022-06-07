def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


def odd_nums_without_yield(n):
    return (i for i in range(1, n + 1, 2))


number_one = odd_nums(15)
number_two = odd_nums_without_yield(15)

print('Решение задания №1')

print('number_one_type', type(number_one), number_one)

for el in number_one:
    print(el)

print(f'number_one пустой: {list(number_one)}')

print('Решение задания №2')

print('number_two_type', type(number_two), number_two)

for el in number_two:
    print(el)

print(f'number_two пустой: {list(number_two)}')