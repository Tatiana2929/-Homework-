# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

def get_days_in_month(month):
    try:
        return calendar.monthrange(1, month)[1]
    except ValueError:
        return -1

month = int(input('Введите номер месяца: '))
days = get_days_in_month(month)
if days == -1:
    print('Такого месяца нет!')
else :
    print('Вы ввели {}. {} дней.'.format(calendar.month_name[month],days))


