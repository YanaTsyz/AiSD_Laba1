# Найти первое число в последовательности Фибоначчи, большее n
# Последовательность Фибоначчи образуется так
# Первый и второй члены последовательности равны 1, а каждый следующий равен сумме двух предыдущих

print('Введите число n')
n = int(input())

i, i1, i2 = 0, 1, 1
while i < n:
    i = i1 + i2
    i1 = i2
    i2 = i

print('Первое число в последовательности Фибоначчи, большее n =',i)