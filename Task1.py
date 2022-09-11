print('Введите день недели');
day = int(input('Enter day number: '))
if day > 7 or day < 1:
     print('Это не день недели. Повторите ввод.')
elif day == 6 or day == 7:
     print("Да, это выходной!")
else:
     print("Нет, это не выходной.")