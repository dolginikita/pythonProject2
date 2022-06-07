tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']


klasses = ['9А', '7В', '9Б', '9В', '8Б']


def tut_klass():
    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None) for i, tut in enumerate(tutors))


tut_zip = tut_klass()

print(type(tut_zip), tut_zip)

for n in tut_zip:
    print(n)

print(f'tut_zip пустой: {list(tut_zip)}')