# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите день недели');
day = int(input('Enter day number: '))
if day > 7 or day < 1:
     print('Это не день недели. Повторите ввод.')
elif day == 6 or day == 7:
     print("Да, это выходной!")
else:
     print("Нет, это не выходной.")