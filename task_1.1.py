# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Разбиваем строку на список слов
words = my_favorite_songs.split(', ')

# Выводим первый трек
print(words[0])

# Получаем длину списка и вычитаем 1, чтобы получить индекс последнего элемента
last_index = len(words) - 1

# Выводим последний трек
print(words[-1])

# Выбираем второй трек
second_index = 1
print(words[second_index])

# Выбираем последний второй трек
last_second_index = last_index - 1
last_song = words[last_second_index]
print(last_song)
