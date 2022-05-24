for n in range(1, 101):
    if (10 < n < 20) or (n % 10 in [0, 5, 6, 7, 8, 9]):
        print(n, "процентов")
    elif n % 10 == 1:
        print(n, "процент")
    else:
        print(n, "процента")
