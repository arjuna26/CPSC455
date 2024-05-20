import matplotlib.pyplot as plt

def tent(x, a):
    if x <= 0.5:
        return a * x
    else:
        return a * (1 - x)

def cobweb(x0, a, n):
    x = x0
    for _ in range(n):
        y = tent(x, a)
        plt.plot([x, x], [x, y], color='b', linewidth=1)  # Vertical line
        plt.plot([x, y], [y, y], color='b', linewidth=1)  # Horizontal line
        x = y
    
    plt.plot([0, 1], [0, 1], color='k', linewidth=2)  # y=x line (diagonal)
    plt.plot([0, 0.5], [0, a/2], color='g', linewidth=3)  # Tent map line segment 1
    plt.plot([0.5, 1], [a/2, 0], color='g', linewidth=3)  # Tent map line segment 2
    plt.xlabel('$x_n$')
    plt.ylabel('$x_{n+1}$')
    plt.title('Cobweb Diagram (a={}) (x0={})'.format(a, x0))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.show()

# Example usage

# a < 1
# cobweb(0.7, 0.6, 100)
# cobweb(0.7, 0.7, 100)
# cobweb(0.3, 0.6, 100)

# a = 1
# cobweb(0.3, 1, 100)
# cobweb(0.8, 1, 100)

# a > 1
# cobweb(0.25, 1.4, 100)
# cobweb(0.7, 1.4, 100)
# cobweb(0.3, 1.6, 100)
# cobweb(0.8, 1.6, 100)

# a = 2
cobweb(0.3, 2, 100)
# cobweb(0.8, 2, 100)



