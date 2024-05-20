import matplotlib.pyplot as plt

def tent(x, a):
    if x <= 0.5:
        return a * x
    else:
        return a * (1 - x)

def tent_time_series(x0, a, n):
    x_values = [x0]
    for _ in range(1, n+1):
        x_values.append(tent(x_values[-1], a))
    
    plt.plot(range(n+1), x_values, linestyle='-')
    plt.xlabel('Iteration')
    plt.ylabel('$x_n$')
    plt.title('Time Series Plot of the Tent Map (a={}) (x0={})'.format(a, x0))
    plt.grid(True)
    plt.show()

# Example usage

# a < 1
# tent_time_series(0.7, 0.6, 100)
# tent_time_series(0.7, 0.7, 100)
# tent_time_series(0.3, 0.6, 100)

# a = 1
# tent_time_series(0.3, 1, 100)
# tent_time_series(0.8, 1, 100)

# a > 1
tent_time_series(0.25, 1.4, 100)
tent_time_series(0.7, 1.4, 100)
tent_time_series(0.3, 1.6, 100)
tent_time_series(0.8, 1.6, 100)

# a = 2
# tent_time_series(0.3, 2, 100)
# tent_time_series(0.8, 2, 100)
