# program that creates a repeating triangular image.
# installing numpy and matplotlib is required.
# the program will plot and display the fractal graph.
# Peter Menchu 2023

import numpy as np
import matplotlib.pyplot as plt

n = 10000

# initialize x and y vectors
# 10000 zeroes in this case
sx = np.zeros(n)
sy = np.zeros(n)

for i in range(1, n):
    # generate random number {1,2,3}
    k = np.random.randint(1, 4)

    # update x and y points
    sx[i] = sx[i - 1] / 2 + k - 1
    sy[i] = sy[i - 1] / 2
    if k == 2:
        sy[i] += 2

# plot x values by y values, 'k.' tells python what
# the points should look like, k. being black dots.
# markersize is the font
plt.plot(sx, sy, 'k.', markersize=1)
plt.title("Sierpinski Triangle (Repeating Fractal Triangles)")
plt.axis('off')
plt.show()

# Peter Menchu 2023
