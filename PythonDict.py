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

# {'Alex': 25, 'Petr': 73}
# {'Alex': 25, 'Petr': 73, 'Kate': 18}
# 73
# {'Alex': 25, 'Petr': 73, 'Kate': 24}
# {'Alex': 25, 'Petr': 73, 'Kate': 24, 10: 20}
# Alex
# 25
# Petr
# 73
# Kate
# 24
# 10
# 20
# КЛЮЧ: Alex ,значения: 25
# КЛЮЧ: Petr ,значения: 73
# КЛЮЧ: Kate ,значения: 24
# КЛЮЧ: 10 ,значения: 20
# {'first': [1, 2, 3], 'second': [10, 20], 'third': [15, 56, 70], 'fourth': [-50]}
