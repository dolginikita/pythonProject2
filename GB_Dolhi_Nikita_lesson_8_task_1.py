import re


def email_parse(text):
    try:
        if text.rsplit('.')[-1] == text:
            raise ValueError
    except ValueError:
        print(f'wrong email: {text}')
    else:
        re_mail = re.compile(r'(?P<username>\w*)@(?P<domain>\w*[.]\w*)')
        print(*map(lambda x: x.groupdict(), re_mail.finditer(text)), sep=', ')


email_parse(input('Введите e-mail:\n'))