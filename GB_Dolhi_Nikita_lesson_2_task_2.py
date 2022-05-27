name = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, s  in enumerate(name):
    if s.isdigit():
        name[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        name[i] = f'"{s[0]}{int(s[1:]):02d}"'

print(name[i], end=' ')
print('\n', name)