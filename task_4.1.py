# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


from sqlite3 import connect, Cursor


def create_table():
    conn = connect('teatchers.db')
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Students (Student_Id INTEGER NOT NULL, Student_Name TEXT NOT NULL, School_Id INTEGER NOT NULL PRIMARY KEY);"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def add_user(id_student, name_student, id_school):
    conn = connect('teatchers.db')
    cursor = conn.cursor()
    sql = "REPLACE INTO Students (Student_Id, Student_Name, School_Id) VALUES (?, ?, ?)"
    cursor.execute(sql, (id_student, name_student, id_school))
    conn.commit()
    cursor.close()
    conn.close()

def show_user(id_student):
    conn = connect('teatchers.db')
    cursor = conn.cursor()
    sql = "SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name FROM Students left join School on School.School_Id = Students.School_Id where Students.Student_Id=?"
    cursor.execute(sql, (id_student,))
    rows = cursor.fetchall()
    for row in rows:
        print('\nID Студента: {}'.format(row[0]))
        print('Имя студента: {}'.format(row[1]))
        print('ID школы: {}'.format(row[2]))
        print('Название школы: {}'.format(row[3]))
    cursor.close()
    conn.close()

create_table()
add_user(201, 'Иван', 1)
add_user(202, 'Петр', 2)
add_user(203, 'Анастасия', 3)
add_user(204, 'Игорь', 4)
show_user(201)
show_user(204)
