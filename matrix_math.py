class ShapeException():
    pass


def dot(vector1, vector2):
    dot_product = 0
    for x in range(len(vector1)):
        dot_product = dot_product + vector1[x] * vector2[x]
    return dot_product


def magnitude(vector1):
    magnitude = dot(vector1, vector1) ** .5
    return magnitude


def shape_vectors(c):
    row_length = len(c)
    for column in c:
        if type(column) == type(1):
            return (row_length, )
        else:
            column_length = len(column)
            return (row_length, column_length)


def vector_add(vector1, vector2):
    if len(vector1) != (len(vector2)):
        raise ShapeException
    vector_plus = []
    for a in range(len(vector1)):
        vector_plus.append(vector1[a] + vector2[a])
    return vector_plus


def vector_sub(vector1, vector2):
    if len(vector1) != (len(vector2)):
        raise ShapeException()
    vector_sub = []
    for a in range(len(vector1)):
        vector_sub.append(vector1[a] - vector2[a])
    return vector_sub


def vector_sum(*vector):
    vector_sum = []
    for a in range(len(*vector)):
        vector_sum.append(sum(*vector[a]))
    return vector_sum


def vector_multiply(vector1, scalar):
    vector_scalar_product = []
    for a in range(len(vector1)):
        vector_scalar_product.append(vector1[a]*scalar)
    return vector_scalar_product


"""To get vector_mean of an unknown number of vectors, combine them into a list:
def vector_mean(n):
    #n is a list of all vectors to average
    num_of_vectors = len(n)
    vector_mean = vector_multiply( vector_sum(n), 1/num_of_vectors)
    return vector_mean"""

def vector_mean(a,b):
    vector_plus = vector_add(a,b)
    vector_mean = vector_multiply(vector_plus, 0.5)
    return vector_mean

def matrix_row(matrix, row):
    matrix_row = matrix[row]
    return matrix_row


def matrix_col(matrix, column):
    matrix_column = []
    for x in matrix:
        matrix_column.append(x[column])
    return matrix_column
    pass


def matrix_scalar_multiply(matrix1, scalar):
    matrix_product = []
    for row in matrix1:
        matrix_product.append(vector_multiply(row, scalar))
    return matrix_product


def matrix_vector_multiply(matrix, vector):
    if len(matrix_col(matrix,0)) != (len(vector)):
        raise ShapeException()
    vector_key = []
    matrix_column = matrix_col(matrix,0)
    for b in range(len(vector)):
        mini_vector = vector_multiply(matrix_col(matrix,b), vector[b])
        vector_key = vector_add(vector_key, mini_vector)
    return vector_key


def matrix_matrix_multiply(matrix1, matrix2):
    if len(matrix_col(matrix1,0)) != (len(matrix2)):
        raise ShapeException()
    matrix_product = []
    for a in range(len(matrix1)):
        item = 0
        matrix1_column = matrix_col(matrix1,a)
        item += dot(matrix1_column, matrix2[a])
        matrix_product.append(item)
    for b in range(len(matrix2)):
        item = 0
        matrix2_column = matrix_col(matrix2,b)
        item += dot(matrix1_column, matrix2[b])
        matrix_product.append(item)
    return matrix_product
