#дз3
name = ['инженер конструктор Игорь',
        'главный бухгалтер МАРИНА',
        'токарь высшего разряда нИКОЛАЙ',
        'директор аэлита']
for el in name:
    name = el.split()[-1].capitalize()
    print(f'Привет, {name}!')