def f1(x, dx, S, xi, yi):
    
    if x <= xi[0]:
        i = 0
    elif x >= xi[-1]:
        i = len(xi) - 2
    else:
        i = 0
        while x > xi[i]:
            i += 1
        i -=1
    xdx1, xdx2 = x+dx, x-dx
    fdx1 = (S[i*4][0]*(xdx1**3))+(S[(i*4)+1][0]*(xdx1**2))+(S[(i*4)+2][0]*xdx1)+S[(i*4)+3][0]
    fdx2 = (S[i*4][0]*(xdx2**3))+(S[(i*4)+1][0]*(xdx2**2))+(S[(i*4)+2][0]*xdx2)+S[(i*4)+3][0]
    return (fdx1-fdx2)/(2*dx)

