A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]
C = [[0, 0], [0, 0]]
D = (1, 2, 3)
type(A)
type(D)

for row in range(len(A)):
    print(row)
    for column in range(len(B[0])):
        print(column)
        for cell in range(len(B)):
            print(cell)
            C[row][column] += A[row][cell] * B[cell][column]
            print(C)
print(C)
