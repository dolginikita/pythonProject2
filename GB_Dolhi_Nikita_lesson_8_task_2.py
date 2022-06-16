import re
import requests


url_text = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

parsed_raw = []

for i in url_text.iter_lines():
    try:
        n = str(i)
        ip_pars = (re.findall(r'\d*[.]\d*[.]\d*[.]\d*(?=\s)', n))[0]
        date_pars = (re.findall(r'\d{2}[/]\w*[/]\d*[:]\d*[:]\d*[:]\d*\s\S\d*', n))[0]
        get_pars = (re.findall(r'GET', n))[0]
        folder_way_pars = (re.findall(r'[/]\w*[/]\w*[_]\d', n))[0]
        numbers_pars = str(re.findall(r'\s\w*\s\w*\s', n))
        number_one_pars = str(numbers_pars.rsplit(' ')[1])
        number_two_pars = str(numbers_pars.rsplit(' ')[2])
        parsed_raw_list = (ip_pars, date_pars, get_pars, folder_way_pars, number_one_pars, number_two_pars)
        parsed_raw.append(parsed_raw_list)
    except IndexError:
        pass

for val in parsed_raw:
    print(val)