a = ["Hey", "Hello", "Goodbye"]
print(a[0])
print(a[1])
print(a[2])
for element in a:  # создаём цыкл
    print(element)
b = [23, 30, 50, 65]
for num in b:
    print(num)
total_sum = 0  # переменная аккумулятор
for e in b:
    total_sum = total_sum + e
print(total_sum)
range(1, 20)
print(list(range(1, 20)))  # range сконвертировал лист(список)
for i in range(1, 20):
    print(i)

total_sum1 = 0
for i in range(1, 20):
    total_sum1 = total_sum1 + i
    total_sum1 += i  # более удобный синтаксис total_sum1 = total_sum1 + i
print(total_sum1)
total_sum2 = 0
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:  # знак % деление без остатка
        total_sum2 += i
print(total_sum2)
