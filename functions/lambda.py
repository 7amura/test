# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число, квадрат числа).
# Пример; [1, 2, 3, 5, 8, 15, 23, 38]
# Получить; [(2, 4), (8, 64), (38, 1444)]

# 1

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i%2 == 0:
#         res.append((i, i**2))

# print(res)     

# 2 lambda
# Ниже: возвращает список, в котором мы к каждому элементу применили функцию f
def select(f, col):
    return[f(x) for x in col]

# возвращает только те значения, которые прошли проверку условия f(x)
def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)

# возводим в квадрат
res = list(select(lambda x: (x, x**2), res))
print(res)