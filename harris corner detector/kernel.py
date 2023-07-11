import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel_size = 13
sigma = 0.5
kernel = cv2.getGaussianKernel(kernel_size, sigma, cv2.CV_64F)
print(kernel)

gaussian_first_deriv_x = np.zeros_like(kernel)
assert(kernel_size % 2 == 1) # I assume you are using an odd kernel_size
half_kernel_size = int(kernel_size / 2)
for i in range(kernel_size):
    x = - half_kernel_size + i
    factor = - x/ (sigma**2)
    gaussian_first_deriv_x[i] = kernel[i] * factor

print(gaussian_first_deriv_x)

plt.plot(kernel[:], 'b')
plt.plot(gaussian_first_deriv_x[:], 'r')
plt.show()