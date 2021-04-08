d = {"Alex": 25, "Petr": 73}
print(d)
d["Kate"] = 18  # добавление ключа
print(d)
print(d["Petr"])  # вызов по ключу
d["Kate"] = 24  # изменения значения
print(d)
d[10] = 20  # смешивания разных типов ключей
print(d)
for key, value in d.items():
    print(key)
    print(value)

for key, value in d.items():
    print("КЛЮЧ: " + str(key) + " ,значения: " + str(value))
