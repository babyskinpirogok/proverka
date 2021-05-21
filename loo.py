# Добавить аргумены в функцию input
i = int(input())
s = int(input())
y = int(input())
def loo(i, s ,y):
    while y != 0:
        s = i / 100 * s + s
        y = y - 1
    return s
print(loo(i, s, y))
