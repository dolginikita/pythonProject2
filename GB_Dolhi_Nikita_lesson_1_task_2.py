#задача№2
a = []
for i in range(1000):
    if i % 2 != 0:
        a.append(i ** 3)
print(a)

b = []
for num in b:
    sum1 = 0
    i = num
    while num != 0:
        sum1 += num % 10
        num = num // 10
    if sum1 % 7 == 0:
        b.append(i)
print(sum(b))

sum_num_plus = 0

for num in a:
    sum = 0
    i = num
    num += 17
    while num != 10:
        sum += num % 10
        num = num // 10
    if num % 7 == 0:
        sum_num_plus += i + 17

print(sum_num_plus)
