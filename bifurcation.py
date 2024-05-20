import matplotlib.pyplot as plt

def tent(x, a):
    if x <= 0.5:
        return a * x
    else:
        return a * (1 - x)

def tent_bifurcation(a_values, x0, n_skip, n_iter):
    bifurcation_x = []
    bifurcation_a = []

    for a in a_values:
        x = x0
        for _ in range(n_skip):
            x = tent(x, a)
        
        for _ in range(n_iter):
            x = tent(x, a)
            bifurcation_x.append(x)
            bifurcation_a.append(a)

    plt.scatter(bifurcation_a, bifurcation_x, s=1, c='black', marker='o')
    plt.xlabel('Parameter $a$')
    plt.ylabel('$x$')
    plt.grid(True)
    plt.show()

a_values = [a/100 for a in range(100, 200)]
tent_bifurcation(a_values, .2, 1000, 200)
