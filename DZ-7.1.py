class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for row in self.matrix_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for i_2 in range(len(other.matrix_list[i])):
                self.matrix_list[i][i_2] = self.matrix_list[i][i_2] + other.matrix_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]])
new_m = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(m.__add__(new_m))
