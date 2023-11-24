import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial values of a, b, and c
a_init = 1
b_init = 0
c_init = 1


# Define the expression
def expression(x1, x2, a, b, c):
    term1 = (2*a*x1 + b*x2) * (-np.sin(x1) - 0.5*np.sin(x1 - x2) + 0.01)
    term2 = (2*c*x2 + b*x1) * (-0.5*np.sin(x2) - 0.5*np.sin(x2 - x1) + 0.05)
    return term1 + term2

# Define the circle equation
def circle_equation(x1, x2, a, b, c, d):
    return a*x1**2 + b*x1*x2 + c*x2**2 - d



def area(a, b, c, d):

    matrix = np.array([[a/d,b/(d*2)],[b/(2*d),c/d]])
    eigenvalues = np.linalg.eigvals(matrix)
    if all(np.isreal(eigenvalue) and eigenvalue > 0 for eigenvalue in eigenvalues):
        a_semi=1/np.sqrt(eigenvalues[0])
        b_semi=1/np.sqrt(eigenvalues[1])
        return np.pi*a_semi*b_semi
    else:
        return False
   


# Create a meshgrid of x1 and x2 values
x1 = np.linspace(-10, 10, 100)
x2 = np.linspace(-10, 10, 100)
X1, X2 = np.meshgrid(x1, x2)


# Initial values

def calmaxd(a,b,c):
    epsilon = 1e-5
    d_low, d_high = 0, 100
    while d_high - d_low > epsilon:
        d_mid = (d_low + d_high) / 2
        circle_values = circle_equation(X1, X2, a, b, c, d_mid)

        X1_negative = X1[circle_values <= 0]
        X2_negative = X2[circle_values <= 0]

        if np.all(expression(X1_negative, X2_negative, a, b, c)<=0):
            d_low = d_mid
        else:
            d_high = d_mid
    
    return d_low 



d=calmaxd(1,-1,1)
print(d)
print(area(1,-1,1,d))
# ans=0
# a_max=0
# b_max=0
# c_max=0
# d_max=0
# for a in range(30):
#     for b in range(20):
#         for c in range(30):
#             d=calmaxd(a/10+0.1,b/10-1,c/10+0.1)
#             if d==0:
#                 continue
#             myarea=area(a/10+0.1,b/10-1,c/10+0.1,d)
#             if(myarea and myarea<1000):
#                 if(myarea>ans):
#                     ans=myarea
#                     print(ans)
#                     a_max=a/10+0.1
#                     b_max=b/10-1
#                     c_max=c/10+0.1
#                     d_max=d

# print(a_max,b_max,c_max,d_max,ans)