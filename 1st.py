# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

x = int(input('Введи число от 1 до 7: '))
if x > 7 or x < 1:
    print('Такого дня недели не существует!')
elif x > 5:
    print('Выходной день!!1')
else:
    print('Будний день.....(9') 