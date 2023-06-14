import random
from datetime import timedelta, datetime

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

def generate_random_string():
    # Генерируем случайную строку из заданных символов
    chars = 'abcdefghijklmnopqrstuvwxy'
    return ''.join(random.choices(chars, k=len(chars)))

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

for i in range(10):
    song_name = generate_random_string()
    duration = round(random.random() * 10, 2) 
    my_favorite_songs.append((song_name, duration))
    
# Создаем список случайных чисел
random_indexes = sorted(random.sample(range(0, len(my_favorite_songs)), 3))

# Суммируем длительности выбранных песен
total_duration = sum([my_favorite_songs[index][1] for index in random_indexes])
total_duration_rounded = round(total_duration, 2)

current_date_time = datetime.now()
dt = datetime(current_date_time.year, current_date_time.month, current_date_time.day, hour=0, minute=int(total_duration_rounded) , second=int(total_duration_rounded % 1 * 60), microsecond=0)
print("Три песни звучат {} минут =".format(total_duration_rounded), dt.strftime('%H:%M:%S'))

# Пункт B. 
# Есть словарь песен my_favorite_songs_dict, который содержит список названий и длительности каждого трека
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

for i in range(10):
    song_name = generate_random_string()
    duration = round(random.random() * 10, 2) 
    my_favorite_songs_dict[song_name] = duration

total_time = 0
for song in random.sample(my_favorite_songs_dict.keys(), 3):
    total_time += my_favorite_songs_dict[song]

total_time_rounded = round(total_time, 2) 

current_date_time = datetime.now()
dt = datetime(current_date_time.year, current_date_time.month, current_date_time.day, hour=0, minute=int(total_time_rounded) , second=int(total_time_rounded % 1 * 60), microsecond=0)
print("Три песни звучат {} минут =".format(total_time_rounded), dt.strftime('%H:%M:%S'))






