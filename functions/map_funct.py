# Функция мар принимает на вход два аргумента; 1 - сама функция; 2- объект
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.
# Есть набор данных. Функция map позволяет увеличить каждый объект на 10.


list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))

print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
print(data)

# data = data.split
# print(data)

data = list(map(int, data. split()))
print(data)