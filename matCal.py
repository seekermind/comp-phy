""" Name: Mamunur Rashid
Reg No: 2017132014 """


import numpy as np          # importing numpy just deal with arrays easily. I did not use any numpy function.

n = int(input("matrix dimension: ")) 

matA = np.ones([n, n])      # two nxn matrices with all elements 1 are declared to perform operation on.
matB = np.ones([n, n])

# These loops are for taking input of the matrix elements
for i in range(n):
    for j in range(n):
        matA[i][j] = float(input("{}, {} 'th element of the first matrix: ".format(j+1, i+1)))

        # This loop is for taking input of the matrix elements
for i in range(n):
    for j in range(n):
        matB[i][j] = float(input("{}, {} 'th element of the second matrix: ".format(j+1, i+1)))
    
def summation(A, B):
    n = len(A)
    m = len(A[0])
    result = np.copy(A)
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][j] + B[i][j]
    return result

def subtraction(A, B):
    n = len(A)
    m = len(A[0])
    result = np.copy(A)
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][j] - B[i][j]
    return result

def multiplication(A, B):
    rowNumber = len(A)
    colNumber = len(A[0])
    result = np.copy(A)
    for i in range(rowNumber):
        for j in range(colNumber):

            # ij 'th element of AB matrix is the dot product of i'th row of A and j'th column of B

            ijElement = 0
            for ArowElement, BcolElement in zip(A[i], B[:, j]):
                ijElement += ArowElement*BcolElement
            result[i][j] = ijElement
    return result

operation = int(input("select operation: \n 1: summation \n 2: subtraction \n 3: multiplication\n"))
if operation not in [1,2,3]:
    print("Please enter a number among 1, 2 and 3.")
    operation = int(input("select operation: \n 1)summation \n 2)subtraction \n 3)multiplication\n"))

if operation == 1:
    print(summation(matA, matB))
elif operation == 2:
    print(subtraction(matA, matB))
else:
    print(multiplication(matA, matB))
