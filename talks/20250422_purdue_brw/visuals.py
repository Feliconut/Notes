# graph of one path of simple random walk
# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
# Set the seed
np.random.seed(5)

# Simulate a random walk
random_walk = np.random.randint(0,2,30000)
random_walk = np.where(random_walk > 0, 1, -1)
random_walk = np.cumsum(random_walk)

class srw1:
    # Plot random_walk as step function
    rw = random_walk[:30]
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(range(len(rw)), rw)
    # x and y same scale
    plt.axis('equal')
    plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    plt.text(25, -10, r'$X_{\left\lfloor t \right \rfloor }$', fontsize=12)
    # add caption on top
    plt.title('Simple random walk')

    # create figures/srw_x1.png
    plt.savefig('figures/srw_x1.png')

class srw2:
   # Plot random_walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(np.linspace(0, 30, 60), random_walk[:60]/np.sqrt(2))
    # x and y same scale
    plt.axis('equal')
    plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    plt.text(20, -10, r'$X_{\left\lfloor 2 t \right \rfloor }/ \sqrt{2}$', fontsize=12)
    # add caption on top
    plt.title('Simple random walk')

    # create figures/srw_x1.png
    plt.savefig('figures/srw_x2.png') 

class srw4:
    # Plot random_walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(np.linspace(0, 30, 120), random_walk[:120]/np.sqrt(4))
    # x and y same scale
    plt.axis('equal')
    plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    plt.text(20, -10, r'$X_{\left\lfloor 4 t \right \rfloor }/ \sqrt{4}$', fontsize=12)
    # add caption on top
    plt.title('Simple random walk')

    # create figures/srw_x1.png
    plt.savefig('figures/srw_x3.png')


class srw100:
    # Plot random_walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(np.linspace(0, 30, 3000), random_walk[:3000]/np.sqrt(100))
    # x and y same scale
    plt.axis('equal')
    plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    plt.text(20, -10, r'$X_{\left\lfloor 100 t \right \rfloor }/ \sqrt{100}$', fontsize=12)
    # add caption on top
    plt.title('Simple random walk')

    # create figures/srw_x1.png
    plt.savefig('figures/srw_x4.png')

class srw1000:
    # Plot random_walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(np.linspace(0, 30, 3000), random_walk[6000:9000]/np.sqrt(100))
    # x and y same scale
    plt.axis('equal')
    plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    plt.text(25, -10, r'$B_t$', fontsize=12)
    # add caption on top
    plt.title('Brownian Motion')

    # create figures/srw_x1.png
    plt.savefig('figures/srw_x5.png')
# %%


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

# %% Many brownian motions in 1D
# Simulate 10 paths of a 1D Brownian motion
class BM1D:
    def brownian_motion_1d(T=1, N=5000):
        dt = T / N
        t = np.linspace(0, T, N)
        # Brownian motion in 1D
        dB = np.sqrt(dt) * np.random.randn(N)
        B = np.cumsum(dB)
        return B
    plt.figure(figsize=(8, 6), dpi=200)
    Ts = np.linspace(0, 1, 5000)
    for i in range(20):
        B = brownian_motion_1d()
        plt.plot(Ts, B, alpha=0.5)

    # plot x = +- sqrt(t)
    plt.plot(Ts, 2*np.sqrt(Ts), 'r--', alpha=1)
    plt.plot(Ts, -2*np.sqrt(Ts), 'r--', alpha=1)
    plt.text(0.5, 1.5, r'$\pm 2 \sqrt{t}$', fontsize=12, color='red')

    # final point
    # plt.plot(B[-1], 'ro')
    plt.title('20 Paths of 1D Brownian Motion')
    plt.xlabel('Time')
    plt.ylabel('X')
    plt.grid(True)
    plt.xlim(0, 1)
    plt.ylim(-2, 2)
    plt.savefig('figures/bm_1d_many.png')
    plt.show()

# %% Cramer Theorem Rate Function
# plot the rate function of the Cramer theorem

# Define the rate function
#\[
#\log 2+z \log z+(1-z) \log (1-z)
#\]
class Cramer:

    def rate_function(z):
        return np.log(2) + z * np.log(z) + (1 - z) * np.log(1 - z)
    z = np.linspace(0, 1, 100)
    plt.figure(figsize=(8, 6),dpi=200)
    plt.plot(z, rate_function(z), label='Rate Function')
    plt.title(r'$\mathbf{I(z)}$ for simple random walk')
    plt.xlabel('z')
    plt.ylabel('Rate Function')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.savefig('figures/cramer_rate_function.png')
    plt.show()

# %% Branching Random Walk
class BRW:
    eps = 0.1
    plt.figure()
    nodes = {(0,0):1}
    edges = dict()
    for i in range(8):
        kk = list(nodes.keys())
        for _i, x in kk:
            if _i == i:
                for _ in range(2 * nodes[(i, x)]):
                    x1 = x+1 if np.random.rand()>0.5 else x-1
                    nodes.setdefault((i+1, x1), 0)
                    nodes[(i+1, x1)] += 1
                    edges.setdefault((i, x, i+1, x1), 0)
                    edges[(i, x, i+1, x1)] += 1
    print(nodes)
    print(edges)
    # plt.xlim(-10,10)
    for edge, count in edges.items():
        i,x,i1,x1 = edge
        for j in range(count):
            plt.plot([x,x1+j*eps],[i,i1], alpha=0.2, color='grey')
    for (i,x) in set(nodes.keys()):
        plt.scatter([x],[i], s=nodes[(i,x)]*10, color='blue', alpha=0.5)

    plt.title('Branching Random Walk')
    plt.xlabel('x')
    plt.ylabel('t')
    plt.xlim(-10, 10)
    plt.ylim(0, 10)

    plt.savefig('figures/brw.png')





# %%
class SimpleRWDef:
    # Improved version of the visualization with cleaner design and closer match to the original sketch

    fig, ax = plt.subplots(figsize=(9, 4), dpi=200)

    # Setup limits
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-0.6, 1.2)
    ax.axis('off')

    # Draw number line with arrowheads at both ends
    arrowprops = dict(arrowstyle='-|>', color='black', linewidth=2)
    ax.annotate('', xy=(2.1, 0), xytext=(-2.1, 0),
                arrowprops=dict(arrowstyle='<|-|>', linewidth=2, color='black'))

    # Draw tip lines at -1, 0, 1
    for x in [-1, 0, 1]:
        ax.plot([x, x], [0.05, -0.05], 'k', linewidth=2)
        ax.text(x, -0.1, str(x), ha='center', va='top', fontsize=14)
        ax.text(x, -0.3, r'$\omega_{' + str(x) + '}$', ha='center', va='top', fontsize=14)
    
    def draw_stickfigure(ax, pos, scale):
        x, y = pos
        # Stick figure with hollow head
        head_radius = 0.04 * scale
        head = plt.Circle((x, y + 0.3 * scale), head_radius, fill=False, color='black', linewidth=2)
        ax.add_patch(head)
        ax.plot([x, x], [y + 0.15 * scale, y + 0.26 * scale], 'k-', linewidth=2)  # body
        ax.plot([x - 0.05 * scale, x + 0.05 * scale], [y + 0.22 * scale, y + 0.22 * scale], 'k-', linewidth=2)  # arms
        ax.plot([x - 0.03 * scale, x], [y, y + 0.15 * scale], 'k-', linewidth=2)  # left leg
        ax.plot([x + 0.03 * scale, x], [y, y + 0.15 * scale], 'k-', linewidth=2)  # right leg

    draw_stickfigure(ax, (0,0.1), 2)

    # Transition arrows
    ax.annotate('', xy=(-1, 0.6), xytext=(0, 0.6),
                arrowprops=dict(arrowstyle='-|>', color='red', linewidth=2))
    ax.annotate('', xy=(1, 0.6), xytext=(0, 0.6),
                arrowprops=dict(arrowstyle='-|>', color='blue', linewidth=2))

    # Transition probabilities
    ax.text(-0.5, 0.63, r'$1 - \omega_x$', fontsize=16, color='red', ha='center')
    ax.text(0.5, 0.63, r'$\omega_x$', fontsize=16, color='blue', ha='center')

    # Title and Z label
    ax.text(0, 1.0, "Transition Probabilities", fontsize=20, color='blue', ha='center')
    ax.text(2.15, -0.1, r"$\mathbb{Z}$", fontsize=20)

    plt.savefig('figures/rwre-def.png', bbox_inches='tight')
    plt.show()




# %%
import random
from collections import defaultdict

kappa = 0.1
class RWRE:
    # Passive random map: each integer maps to a random number in [0,1] when first queried
    environment = defaultdict(lambda: random.uniform(0.15, 1 - kappa))

    # Simulate a random walk with random environment
    random_walk = []
    x = 0
    for i in range(10000):
        # Randomly choose the next step
        if random.uniform(0, 1) < environment[x]:
            x += 1
        else:
            x -= 1
        random_walk.append(x)
    random_walk = np.array(random_walk)


    # Plot random_walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.plot(random_walk)
    # x and y same scale
    # plt.axis('equal')
    # plt.ylim(-10, 10)
    # equation $S_n$ on bottom right
    # plt.text(25, -10, r'$B_t$', fontsize=12)
    # add caption on top
    plt.title('RWRE')

    # create figures/srw_x1.png
    plt.savefig('figures/rwre-10000.png') 

# %%
class SBM:
    pass

X = {0:1}
for t in range(1,40):
    X1 = defaultdict(int)
    for x, m in X.items():
        new_m = np.random.binomial(2 * m, 0.5)
        # new_m = m * 2
        right=np.random.binomial(new_m, 0.5)
        X1[x+1] += right
        X1[x-1] += (new_m - right)
    X = X1
    # n = 5
    if True:#t % 10 == 0:
        R = 10
        xs = np.linspace(-R, R, 2*R+1)
        ys = np.array([X[x] for x in xs])
        # plt.plot(xs, ys,  alpha=0.5, label='t={}'.format(t))
        plt.scatter(xs, [t]*len(xs),s=ys * 10, alpha=0.5)
    # plt.legend()
# %%

# %%
