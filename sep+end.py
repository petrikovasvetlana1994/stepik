'''По умолчанию команда print() принимает несколько аргументов (параметров), выводит их через один пробел, 
после чего ставит перевод строки. Это поведение можно изменить, используя необязательные именованные параметры sep 
(separator, разделитель) и end (окончание).'''

'''print('a', 'b', 'c', sep='*') # a*b*c
print('d', 'e', 'f', sep='**') # d**e**f

print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@') # a b c@d e f@@

sep=' '   # пробел
end='\n'  # перевод строки'''

'''qwerty'''

# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).

#print('I', 'like', 'Python', sep='***')

# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.

'''separator=input()
name1 = input()
name2 = input()
name3 = input()
print(name1, name2, name3, sep= separator)'''

# Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), 
# после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.

'''name = input()
print('Привет', name, sep=', ', end='!')

#       Переменные
# <имя переменной> = <значение переменной>
name1 = 'Тимур'

#       Множественное присваивание
# В языке Python можно за одну инструкцию присваивания изменять значение сразу нескольких переменных. Делается это так:

name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)
# Этот код можно записать и так:

name = 'Timur'
surname = 'Guev'
print('Имя:', name, 'Фамилия:', surname)
# Отличие двух способов состоит в том, что множественное присваивание в первом способе присваивает значение двум переменным одновременно.

# Если требуется считать текст с клавиатуры и присвоить его в качестве значения переменным, то можно написать так: 

name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)

# Множественное присваивание удобно использовать, когда нужно обменять значения двух переменных. В Python это делается так:

name1 = 'Timur'
name2 = 'Gvido'
name1, name2 = name2, name1

language = 'Python'
language = 'Pascal'
print(language)'''

print('Python', end='+')  # print('C++')
# print('GO')
print('C#', end='=')  # print('C')
print('awesome')