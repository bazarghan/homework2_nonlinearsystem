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

# Create a meshgrid of x1 and x2 values
x1 = np.linspace(-10, 10, 100)
x2 = np.linspace(-10, 10, 100)
X1, X2 = np.meshgrid(x1, x2)


# Initial values
Z = expression(X1, X2, a_init, b_init, c_init)
epsilon = 1e-5
d_low, d_high = 0, 100
while d_high - d_low > epsilon:
    d_mid = (d_low + d_high) / 2
    circle_values = circle_equation(X1, X2, a_init, b_init, c_init, d_mid)

    X1_negative = X1[circle_values <= 0]
    X2_negative = X2[circle_values <= 0]

    if np.all(expression(X1_negative, X2_negative, a_init, b_init, c_init)<=0):
        d_low = d_mid
    else:
        d_high = d_mid
  
    d_init = d_low 
circle_values = circle_equation(X1, X2, a_init, b_init, c_init,d_init)

# Create the plot
fig, ax = plt.subplots()
contour_expr = ax.contour(X1, X2, Z, levels=[0], colors='r', linestyles='dashed')
contour_circle = ax.contour(X1, X2, circle_values, levels=[0], colors='blue', linestyles='dashed')

# Add sliders for a, b, and c
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.2, 0.06, 0.65, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.2, 0.11, 0.65, 0.03], facecolor=axcolor)

s_a = Slider(ax_a, 'a', 0.1, 5.0, valinit=a_init)
s_b = Slider(ax_b, 'b', -2, 2, valinit=b_init)
s_c = Slider(ax_c, 'c', 0.1, 5.0, valinit=c_init)

# Update function for sliders
# Update function for sliders
if np.all(circle_equation(X1, X2, 1, 1, 1, 1) <= 0):
    print("yes")

def update(val):
    global contour_expr, contour_circle  # Declare global variables
    a = s_a.val
    b = s_b.val
    c = s_c.val
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
  
    d = d_low 
    

    Z = expression(X1, X2, a, b, c)
    circle_values = circle_equation(X1, X2, a, b, c, d)
    
    for coll in contour_expr.collections:
        coll.remove()
    for coll in contour_circle.collections:
        coll.remove()
    contour_expr = ax.contour(X1, X2, Z, levels=[0], colors='r', linestyles='dashed')
    contour_circle = ax.contour(X1, X2, circle_values, levels=[0], colors='blue', linestyles='dashed')

    fig.canvas.draw_idle()
    plt.title(r'${:.2f}={:.1f}x_1^2 + {:.1f}x_1x_2 + {:.1f}x_2^2$'.format(d,a, b, c), y=1.05)
    ax.set_aspect('equal', adjustable='datalim')

   

# Attach the update function to sliders
s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)

plt.show()
