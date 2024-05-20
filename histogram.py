import numpy as np
import matplotlib.pyplot as plt

def tent(x, a):
    if x <= 0.5:
        return a * x
    else:
        return a * (1 - x)

def tent_map_iterations(x0, a, n):
    x_values = [x0]
    for _ in range(n):
        x_values.append(tent(x_values[-1], a))
    return x_values

def tent_frequency_histogram(x0, a, n_iter, num_bins):
    # Generate tent map iterations
    x_values = tent_map_iterations(x0, a, n_iter)
    
    # Create histogram
    plt.hist(x_values, bins=num_bins, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('$x$')
    plt.ylabel('Frequency')
    plt.title('Frequency Histogram of the Tent Map (a={}) (x0={})'.format(a, x0))
    plt.grid(True)
    plt.show()

# Example usage

n_iter = 10000
num_bins = 50

tent_frequency_histogram(0.5, 1.2, n_iter, num_bins)

# tent_frequency_histogram(0.3, 1, n_iter, num_bins)
# tent_frequency_histogram(0.8, 1.6, n_iter, num_bins)







