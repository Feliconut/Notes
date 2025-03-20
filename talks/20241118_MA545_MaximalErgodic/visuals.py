# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
# Set the seed
np.random.seed(5)

# plot the heat kernel in 2D using color map with contours
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = (1 / (2 * np.pi)) * np.exp(-(X**2 + Y**2) / 2)

plt.figure(figsize=(8, 8))
contour = plt.contourf(X, Y, Z, cmap='Blues')
# plt.colorbar(contour)
plt.title('Heat Kernel in 2D')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('figures/heat_kernel_2d.png')
plt.show()
# %%
# simulate two-dimension Brownian Motion
def brownian_motion_2d(T=1, N=5000):
    dt = T / N
    t = np.linspace(0, T, N)
    # Brownian motion in 2D
    dB = np.sqrt(dt) * np.random.randn(N, 2)
    B = np.cumsum(dB, axis=0)
    return B
plt.figure(figsize=(8, 8))
B= brownian_motion_2d()
plt.plot(B[:, 0], B[:, 1],alpha=0.8)
# final point
plt.plot(B[-1, 0], B[-1, 1], 'ro')

B= brownian_motion_2d()
plt.plot(B[:, 0], B[:, 1],alpha=0.8)
# final point
plt.plot(B[-1, 0], B[-1, 1], 'ro')

plt.title('2D Brownian Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.savefig('figures/brownian_motion_2d.png')
plt.show()

# %%

# Sample 1000 times from a 2-dimensional Gaussian distribution
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance matrix
samples = np.random.multivariate_normal(mean, cov, 2000)

plt.figure(figsize=(8, 8))
plt.scatter(samples[:, 0], samples[:, 1], alpha=0.3)
plt.title('2000 Samples from 2D Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
# from -5 to 5
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.savefig('figures/gaussian_samples_2d.png')
plt.show()

# %%

# %%
