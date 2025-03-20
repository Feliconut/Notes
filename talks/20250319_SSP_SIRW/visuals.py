# %%
import matplotlib.pyplot as plt

# Set up the figure
fig, ax = plt.subplots(figsize=(4,2),dpi=300)
ax.set_ylim(-2, 1)
ax.set_xlim(-3,3.2)

# Hide y-axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Draw the horizontal line (the number line)
ax.axhline(0, color='black', alpha=0.5, linewidth=1)

# line segment from -1 to 0 green
ax.plot([-1, 0], [0, 0], color='green', linewidth=2)

# line segment from 0 to 3 red
ax.plot([0, 3], [0, 0], color='red', linewidth=2)

# Add ticks and labels manually
x=-1
ax.plot([x, x], [0, 0.2], color='green')  # tick
ax.text(x, -0.3, str(x), ha='center', va='center')
x=0
ax.plot([x, x], [0, 0.2], color='black')  # tick
ax.text(x, -0.3, str(x), ha='center', va='center')

ax.text(0,0.4, "AF", ha='center', va='center', fontsize=12) 
ax.text(-0.5,0.4, "WR", ha='center', va='center', fontsize=12, color="green") 
x=-1
ax.plot([x, x], [0, 0.8], color='green', linestyle='--', linewidth=1) 
ax.text(-1,1, "LR", ha='center', va='center', fontsize=12, color="green") 
ax.text(-2,0.4, "degenerate", ha='center', va='center', fontsize=12, color="gray") 
ax.text(2,0.4, "PSR", ha='center', va='center', fontsize=12, color="red") 

ax.text(3.2,0,r"$\alpha$", ha='center', va='center', fontsize=12) 


# LOWER AXIS
y = -1
ax.plot([0, 1.5], [y,y], color='green', linewidth=2)
ax.plot([1.5, 3], [y+0.1,y+0.1], color='blue', linewidth=5, alpha=0.3)
ax.plot([1.5, 3], [y,y], color='green', linewidth=2)
ax.plot([0,0], [y, y+0.2], color='green')
ax.text(0,-1.3, "1", ha='center', va='center')
ax.plot([1.5,1.5], [y, y+0.2], color='green')
ax.text(1.5,-1.3, "1/2", ha='center', va='center')
ax.plot([3,3], [y, y+0.2], color='black')
ax.text(3,-1.3, "0", ha='center', va='center')

ax.text(3.2, y, r"$p$", ha='center', va='center', fontsize=12)

# thin line
ax.plot([0,0], [0,y+0.3], color='gray', linestyle='--', linewidth=1)
ax.plot([0,3], [0,y+0.3], color='gray', linestyle='--', linewidth=1)

# # Add custom text or arrows
# ax.text(2, 0.6, "Some label here", fontsize=12)
# ax.arrow(1, 0.4, 1, 0, head_width=0.1, head_length=0.2, fc='blue', ec='blue')

# Remove box around the plot
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("./figures/cases.png", bbox_inches='tight', dpi=300, transparent=True)

# plt.tight_layout()
plt.show()

# %%
# simulate bmpe
import numpy as np
xs = np.linspace(0,1000,1001)
ys = np.zeros_like(xs)
Bs = np.zeros_like(xs)


running_min = 0
running_max = 0
for i in range(1, len(xs)):
    increment = np.random.normal(0, 1)
    Bs[i] = Bs[i-1] + increment
    running_min = min(running_min, ys[i-1])
    running_max = max(running_max, ys[i-1])
    ys[i] = Bs[i] + (running_max + running_min)*0.8
plt.plot(xs, ys)
plt.plot(xs, Bs)
plt.plot(xs, ys-Bs)

# %%

fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True, dpi=300)

# First subplot for ys (green)
axs[0].plot(xs, ys, color='green')
axs[0].set_ylabel(r'SIRW $X_k$')
axs[0].grid(True)

# Second subplot for Bs (blue)
axs[1].plot(xs, Bs, color='blue')
axs[1].set_ylabel(r'Brownian Motion $B_k$')
axs[1].grid(True)

# Third subplot for ys - Bs (orange)
axs[2].plot(xs, ys - Bs, color='orange')
axs[2].set_ylabel(r'Drift $\Gamma_k$')
axs[2].set_xlabel('Time $k$')
axs[2].grid(True)

# Hide x-labels except for the bottom plot
plt.setp([ax.get_xticklabels() for ax in axs[:-1]], visible=False)

plt.tight_layout(pad=1.0, w_pad=0.1, h_pad=0.5)
plt.savefig("./figures/bmpe.png", bbox_inches='tight', dpi=300, transparent=True)

# %%
plt.figure(figsize=(10,3), dpi=300)
plt.plot(xs, ys, color="green", label=r"SIRW $X_k$")
plt.plot(xs, Bs, color="blue", label=r"Martingale part $M_k$")
plt.plot(xs, ys-Bs, color="orange", label=r"Drift $\Gamma_k$", linewidth=2)
plt.legend()
plt.grid(True)
plt.xlabel("Time $k$")

plt.savefig("./figures/bmpesmall.png", bbox_inches='tight', dpi=300, transparent=True)

# %%

# %%

# %%

# %%

# %%


# %%

