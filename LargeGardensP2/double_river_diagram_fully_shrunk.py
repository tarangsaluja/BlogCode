import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make garden with line
plt.plot([0, 7], [-2,-2], color='brown', linewidth=2)
plt.plot([7, 7], [-2, 2], color='brown', linewidth=2)
plt.plot([7, 0], [2, 2], color='brown', linewidth=2)

#make garden
garden = patches.Rectangle((0, -2), 7, 4, linewidth=1, facecolor='green')
ax.add_patch(garden)
ax.text(3.5, 0, 'garden', color='black', ha='center', va='center')

#make second graden with line
plt.plot([0,-7], [-2,-2], color='brown', linewidth=2)
plt.plot([-7, -7], [-2, 2], color='brown', linewidth=2)
plt.plot([-7, 0], [2, 2], color='brown', linewidth=2)

#make garden
garden2 = patches.Rectangle((-7, -2), 7, 4, linewidth=1, facecolor='green')
ax.add_patch(garden2)
ax.text(-3.5, 0, 'garden', color='black', ha='center', va='center')


ax.set_aspect('equal')

plt.savefig("double_river_fully_shrunk.png")