import sys

read_interval = list(map(int, sys.argv[1:]))
with open('data/bakery.csv', 'r', encoding='utf-8') as sale:
    text = sale.readlines()
    if len(read_interval) == 2:
        for line in text[read_interval[0] - 1:read_interval[1]]:
            print(line.strip())
    elif len(read_interval) == 1:
        for line in text[read_interval[0] - 1:]:
            print(line.strip())
    else:
        for line in text:
            print(line.strip())
exit()