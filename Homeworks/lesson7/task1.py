"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    matrix_count = 0

    def __init__(self, args):
        self.args = args
        Matrix.matrix_count += 1

    def __str__(self):
        matrix = '\n'.join(' '.join('{:^4}'.format(str(i)) for i in el) for el in self.args)
        return f'Матрица №{Matrix.matrix_count}:\n{matrix}'

    def __add__(self, other):
        new_matrix = []
        idx = 0
        while idx < len(self.args):
            new_list = list(map(sum, zip(self.args[idx], other.args[idx])))
            new_matrix.append(new_list)
            idx += 1
        new_matrix = '\n'.join(' '.join('{:^4}'.format(str(i)) for i in el) for el in new_matrix)
        return f'Сумма матриц:\n{new_matrix}'


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)

m2 = Matrix([[7, 8, 9], [1, 2, 3], [4, 5, 6]])
print(m2)

sum1 = m1 + m2
print(sum1)

m3 = Matrix([[20, 45, 60, 3], [90, 111, 6, -7]])
print(m3)

m4 = Matrix([[-10, 6, 7, 1], [-33, 9, 8, 7]])
print(m4)

sum2 = m3 + m4
print(sum2)
