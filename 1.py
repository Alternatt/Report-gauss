 

def gauss(A, B):
    # Прямой ход метода Гаусса
    n = len(B)
    for i in range(n):
        # Поиск максимального элемента в столбце i
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                max_ryad = k
        # Обмен строками
        for k in range(i, n):
            T = A[max_ryad][k]
            A[max_ryad][k] = A[i][k]
            A[i][k] = T
        T = B[max_ryad]
        B[max_ryad] = B[i]
        B[i] = T
        # Приведение к верхнетреугольному виду
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            B[k] += c * B[i]
    # Проверка совместности системы
    for i in range(n):
        if A[i][i] == 0 and B[i] != 0:
            return 0 # Система несовместна

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
            
        x[i] /= A[i][i]

    return x


# Определяем матрицу системы уравнений (ЗДЕСЬ НУЖНО ВЫБРАТЬ МАТРИЦУ)

#Пример совместной. --------------------------------
'''
A = [[1, 1, 1], [1, -1, 2], [2, -1, -1]]
'''
#Пример несовместной. ------------------------------
'''
A = [[2, 3, -1], [4, 6, -2], [1, 2, -1]]
'''
# Определяем столбец свободных членов

B = [6, 5, -3]

x = gauss(A, B)

# Вывод результата

if x == 0:
    print("Система уравнений несовместна.")
else:
    print("Результат:")
    print(x)
