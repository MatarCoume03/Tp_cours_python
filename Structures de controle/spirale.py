import math
import matplotlib.pyplot as plt
with open("spirale.dat", "w") as save:
    xa ,ya = 0, 0
    θ = 0
    r = 0.5
    while  θ <= 4*(math.pi):
        xa = math.cos(θ) * r
        ya = math.sin(θ) * r
        θ += 0.1
        r += 0.1
        #print(f"{xa:.5f}    {ya:.5f}")
        save.write(f"{xa:.5f}    {ya:.5f}\n")

x = []
y = []
with open("spirale.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

fig, ax = plt.subplots(figsize=(8,8))
mini = min(x+y) - 2
maxi = max(x+y) + 2
ax.set_xlim(mini, maxi)
ax.set_ylim(mini, maxi)
ax.plot(x, y)
fig.savefig("spirale.png")