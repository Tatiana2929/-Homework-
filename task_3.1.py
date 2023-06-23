# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:

    def __init__(self, n, m):
        # Инициализируем пустую матрицу
        self.n = n # строки
        self.m = m # столбцы

        self.matrix = [list() for _ in range(n)]
        for i in range(self.n):
            row = list()
            for j in range(self.m):
                row.append(None)
            self.matrix[i] = row

    def generate(self, s):
        # Заполняем матрицу
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j]=s*(i+1)*(j+1)

    def get_row_count(self):
        # Возвращаем количество строк
        return self.n

    def get_col_count(self):
        # Возвращаем количество столбцов
        return self.m

    def get(self, i, j):
        # Получаем значение
        if (i<=self.n) and (j<=self.m) and (i>0) and (j>0) : 
           return self.matrix[i-1][j-1]
        else :
            return None

    def set(self, s, i, j):
        # Устанавливаем значение
        if (i<=self.n) and (j<=self.m) and (i>0) and (j>0) : 
            self.matrix[i-1][j-1]=s

    def print(self):
        # Печатаем матрицу таблицей
        print("Матрица:")
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end='\t')
            print(end='\n')

    def show(self):
        # Печатаем матрицу массивом
        print("Матрица:", self.matrix)

# Использование класса
m = Matrix(3,5)
m.generate(3)
m.set(0,1,5)
m.set(0,2,5)
m.set(0,3,5)
m.get(3,5)
print('Значение по координатам 2,3: {}.'.format(m.get(2,3)))
m.print()
m.show()
print('Количество строк: {}.'.format(m.get_row_count()))
print('Количество столбцов: {}.'.format(m.get_col_count()))
