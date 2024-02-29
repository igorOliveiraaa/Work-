def soma_matrizes(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "As matrizes devem ter as mesmas dimensões para a soma."

    C = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]

    return C

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(soma_matrizes(A, B))  
