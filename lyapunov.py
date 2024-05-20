import numpy as np
import matplotlib.pyplot as plt

def tent(x, a):
    if x <= 0.5:
        return a * x
    else:
        return a * (1 - x)

def calculate_lyapunov_exponents(x0, a, n_iter, n_steps):
    # Initialize tangent vector
    v = np.random.rand()
    sum_lyapunov = 0
    
    # Iterate to get trajectory and perturbed trajectory
    for _ in range(n_iter):
        x = x0
        v /= np.linalg.norm(v)
        for _ in range(n_steps):
            # Compute tangent vector
            v = a * (1 - 2 * abs(x - 0.5)) * v
            # Update trajectory
            x = tent(x, a)
        # Update Lyapunov sum
        sum_lyapunov += np.log(np.linalg.norm(v))
    
    # Calculate average Lyapunov exponent
    return sum_lyapunov / n_iter

def lyapunov_exponent_diagram(a_values, x0, n_iter, n_steps):
    lyapunov_exponents = []
    for a in a_values:
        lyapunov_exponents.append(calculate_lyapunov_exponents(x0, a, n_iter, n_steps))
    
    plt.plot(a_values, lyapunov_exponents, marker='.', linestyle='', color='blue')
    plt.xlabel('Parameter $a$')
    plt.ylabel('Lyapunov Exponent')
    plt.title('Lyapunov Exponent Diagram of the Tent Map')
    plt.grid(True)
    plt.show()

# Example usage
a_values = np.linspace(1.0, 2.0, 500)
x0 = 0.2
n_iter = 1000
n_steps = 100
lyapunov_exponent_diagram(a_values, x0, n_iter, n_steps)
