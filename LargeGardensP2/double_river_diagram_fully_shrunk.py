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

#make river
rect = patches.Rectangle((-0.01, -5), 0.02, 10, linewidth=1, edgecolor='blue', facecolor='blue')
ax.add_patch(rect)
ax.text(0, 0, 'river', color='white', ha='center', va='center', rotation=90)


ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("double_river_fully_shrunk.png")