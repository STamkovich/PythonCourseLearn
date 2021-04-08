total = 0
for i in range(1, 5):
    total += i
print(total)

total2 = 0
i1 = 0
while i1 < 5:  # while с анг. переводитсья как "До тех пор"
    total2 += i1
    i1 += 1
print(total2)

# когда цикл while полезен (когда мы не знаем заранее сколько раз мы должны будем выполнить цыкл)

my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15]
total3 = 0  # переменная аккумулятр
i2 = 0  # переменная счётчик
while my_list[i2] > 0:
    total3 += my_list[i2]
    i2 += 1
total4 = 0
for element in my_list:
    if element <= 0:
        break  # ключевое стлово которое предназначено для немедленного выхода из тела цыкла
    total4 += element
print(total3)
print(total4)

total5 = 0
i5 = 0
while total5 < 10 and my_list[i5] > 0:  # коньюнкция (выполнение обоих условий)
    total5 += my_list[i5]
    i5 += 1
print(total5)

#  тонкость связанная с цыклом while
my_list = [7, 5, 4, 4, 3, 2, 1]  # (убираем отрицательные числа)
total3 = 0  # переменная аккумулятр
i2 = 0
while i2 < len(my_list) and my_list[i2] > 0:  # в ручную ограничиваем нашу переменную счётчик ( HardCod)
    # стандартная функция len которая определяет размер листа (в данном случае)
    total3 += my_list[i2]
    i2 += 1
print(total3)

# бесконечные цыкл
while 1 < 2:  # так же можем написать просто while True
    print("Hello")
