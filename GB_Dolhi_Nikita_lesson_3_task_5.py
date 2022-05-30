from random import choice, randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'позавчера', 'завтра', 'ночью']
abjectives = ['веселый', 'яркий', 'утопичный', 'зеленый', 'мягкий']


def get_jokes(n, repeat=False):
    no, adv, abj = nouns.copy(), adverbs.copy(), abjectives.copy()
    jokes = []
    list_min = min(no, adv, abj)
    while n and len(list_min):
        number = randrange(len(list_min))
        if repeat:
            jokes.append(f'{no.pop(number)} {adv.pop(number)} {abj.pop(number)}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(abjectives)}')
        n -= 1
    return jokes

print(get_jokes(10, True))
print(get_jokes(10, False))