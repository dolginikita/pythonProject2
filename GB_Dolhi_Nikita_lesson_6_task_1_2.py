with open('nginx_logs.txt', 'r', encoding='utf-8') as file_exist:
    ready_tuple = []
    all_ip = []
    for line in file_exist:
        replaced_file = line.replace('"', '')
        reformat_file = replaced_file.split(' ')
        line_tuple = (reformat_file[0], reformat_file[5], reformat_file[6])
        ready_tuple.append(line_tuple)
        all_ip.append(reformat_file[0])

print(f'Имеем список {type(ready_tuple)}, кортежей {type(ready_tuple[0])}, формата \n{ready_tuple}')


def spam_ip(ips):
    """
    :param ips: list with IP address
    :return: return one ip, with highest count of requests and how many count of request this ip did
    """
    ip_spam = max(set(ips), key=ips.count)
    ip_count = ips.count(ip_spam)
    print(f'Самое больше кол-во запросов: {ip_count}, было с IP: {ip_spam}')