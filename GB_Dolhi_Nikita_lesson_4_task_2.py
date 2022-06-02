import requests
from datetime import datetime


def currency_rates(value):
    """
    :param value: function taken currency in str type (eur, usd and etc.)
    :return: The current exchange rate on the date of the Central Bank
    """
    value = value.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    url_info = str(response.content)
    my_split = url_info.split('<Valute ID=')

    date_url = url_info[(url_info.index('Date=') + 6):(url_info.index('Date="') + 16)]
    datetime_url = datetime.strptime(date_url, '%d.%m.%Y').date()
    cost_value = 0

    tracker = 0

    for i in my_split:
        if value in i:
            cost_value = float(i[(i.find('<Value>') + 7):(i.find('</Value>'))].replace(',', '.'))
            tracker += 1
        else:
            continue

    if tracker == 0:
        print(f"Введенная валюта на {datetime_url} число, в базе не найдена")
    else:
        print(f'Запрашиваемая валюта {value} стоит {cost_value:.02f} руб. на {datetime_url}')


if __name__ == '__main__':

    currency_rates(input('Введите валюту: '))