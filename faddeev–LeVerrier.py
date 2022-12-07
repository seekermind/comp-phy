"""
Name: Mamunur Rashid
Reg No: 2017132014
"""

"""Reference: https://en.wikipedia.org/wiki/Faddeev-LeVerrier_algorithm
    """


# a function to return trace of a 3x3 matrix
def trace(A):
    return A[0][0]+A[1][1]+A[2][2]

# a function to multiply two matrix
def matMultiplication(A, B):
    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    return result
 
dim = 3     # dimension of matrix

# uncomment to take manual input. Commented to avoid annoying prompt everytime.

# A = [[float(input("{}, {} 'th matrix element: ".format(j+1,i+1))) for i in range(dim)] for j in range(dim)]

A = [[3, 1, 5], [3, 3, 1], [4, 6, 4]]

c = [0 for i in range(dim+1)]   # coefficients of characteristics equation

c[3] = 1    # c_n is always 1
c[2] = -trace(A)

# M_2 = A*M_1 + c_2*I
M_2 = [[(A[j][i] + c[2]) if i == j else A[j][i] for i in range(dim)] for j in range(dim)]

# c_1 = -1/2 * trace(A*M_2)
AM_2 = matMultiplication(A, M_2)
c[1] = -0.5*(trace(AM_2))

# M_3 = A*M_2 + c_1*I
M_3 = [[(AM_2[j][i] + c[1]) if i == j else AM_2[j][i] for i in range(dim)] for j in range(dim)]

# c_1 = -1/2 * trace(A*M_2)
c[0] = -(1/3)*(trace(matMultiplication(A, M_3)))

# A^-1 = -(1/c_0) * M_3
A_inv = [[(-(1/c[0])*M_3[j][i]) for i in range(dim)] for j in range(dim)]

c.reverse()
print("{}x^3 + {}x^2 + {}x + {}".format(*c))
print(A_inv)
