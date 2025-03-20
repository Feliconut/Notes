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
from collections import defaultdict
class SIRW:
    def w(n):
        return 1 + 10 * (n+1) ** -0.5
    walk = [0]
    x = 0
    local_times = defaultdict(int)
    for i in range(30):
        w_left = w(local_times[x-1])
        w_right = w(local_times[x])
        p = w_left/(w_left + w_right)
        # print(p)
        if np.random.rand() < p:
            x -= 1
            local_times[x] += 1
        else:
            local_times[x] += 1
            x += 1
        walk.append(x)

# %%
class sirwplot:
    walk = SIRW.walk
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(range(len(walk)), walk)
    # plt.axis('equal')
    # plt.show()
    plt.ylim(-2, 10)
    # print $X_k$ on bottom right
    plt.text(25, -1, r'$X_k$', fontsize=12)
    plt.title('Self-Interacting Random Walk')
    plt.savefig('figures/sirw.png')

class sirwlocal:
    local_times = SIRW.local_times
    # Fill in missing values

    # plot as step function
    plt.figure(figsize=(4,3), dpi=200)
    # plt.step(list(local_times.values()), range(len(local_times)))
    plt.barh(list(local_times.keys()), list(local_times.values()), height=1, alpha = 0.7)
    plt.ylim(-2, 10)
    # print $L_k$ on bottom right
    plt.text(3, -1, r'$L^X(y, 30)$', fontsize=12)
    plt.title('Local Time of SIRW')
    
    # plt.show()
    plt.savefig('figures/sirwlocal.png')



    


# %%

class SIRWlarge:
    def w(n):
        return 1 + 10 * (n+1) ** -0.5
    walk = [0]
    x = 0
    local_times = defaultdict(int)
    for i in range(300000):
        w_left = w(local_times[x-1])
        w_right = w(local_times[x])
        p = w_left/(w_left + w_right)
        # print(p)
        if np.random.rand() < p:
            x -= 1
            local_times[x] += 1
        else:
            local_times[x] += 1
            x += 1
        walk.append(x)
# %%
class sirwplotrescaled:
    walk = SIRWlarge.walk[:300000]
    plt.figure(figsize=(4,3), dpi=200)
    plt.step(np.linspace(0, 30, 300000), np.array(walk)/np.sqrt(10000))

    plt.text(25, -2, r'$W_t$', fontsize=12)
    # plt.axis('equal')
    # plt.show()
    # plt.ylim(-15, 5)
    plt.title('BM Perturbed at Extrema')
    plt.savefig('figures/sirwrescaled.png')

class sirwlocalrescaled:
    local_times = SIRWlarge.local_times
    # Fill in missing values

    # plot as step function
    plt.figure(figsize=(4,3), dpi=200)

    rescaled_local_times = {k/10000**0.5: v/10000**0.5 for k, v in local_times.items()}

    plt.barh(list(rescaled_local_times.keys()), list(rescaled_local_times.values())
        , height=1/10000**0.5, alpha = 0.7)
    # plt.step(list(local_times.values()), range(len(local_times)))
    # plt.barh(list(map(lambda x:x/10000, local_times.keys())), list(map(lambda x:x/10000,local_times.values())), height=1, alpha = 0.7)
    # plt.ylim(-15, 5)
    plt.text(10, -2, r'$L^W(y, 30)$', fontsize=12)
    plt.title('Squared Bessel Process')
    plt.savefig('figures/sirwlocalrescaled.png')
# %%
