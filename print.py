def get_sum(a, b) -> int:
    return a + b


print(get_sum(5, 8))

# Вывод данных, команда print #
print('Мы изучаем язык Python')

# То, что мы пишем в круглых скобках у команды print(), называется аргументами или параметрами команды.
# Команда print() позволяет указывать несколько аргументов, в таком случае их надо отделять запятыми. 
# Если вы не будете писать запятые между аргументами, Python воспримет это как синтаксическую ошибку.
# Например, следующий код:

print('Скоро я', 'буду программировать', 'на языке', 'Python!')

# выведет на экран текст:
# Скоро я⎵буду программировать⎵на языке⎵Python!

# Напишите программу, которая выводит на экран текст «Здравствуй, мир!» (без кавычек).
print("Здравствуй, мир!")

# В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42, 
# которая принесла героям удачу и помогла сорвать джекпот в лотерее. Напишите программу, 
# которая выводит данную последовательность чисел с одним пробелом между ними.

print('4', '8', '15', '16', '23', '42')

# Измените предыдущую программу так, чтобы каждое число последовательности 4 8 15 16 23 42 печаталось на отдельной строке.

print('4')
print('8')
print('15')
print('16')
print('23')
print('42')

# Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).

print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')