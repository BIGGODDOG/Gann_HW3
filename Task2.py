# Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму
# элементов главной диагонали.
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Diagonals : 1 + 5 + 9 = 15

def create_matrix():
    # Создаем вложенный список размером 3x3 через ввод
    matrix = []
    print("Введите элементы матрицы 3x3:")
    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Элемент [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def sum_main_diagonal(matrix):
    # Считаем сумму элементов главной диагонали
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

matrix = create_matrix()
diagonal_sum = sum_main_diagonal(matrix)
print(f"Сумма элементов главной диагонали ({matrix[0][0]} + {matrix[1][1]} + {matrix[2][2]}):", diagonal_sum)