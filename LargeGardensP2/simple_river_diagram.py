import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make river
rect = patches.Rectangle((-1, -5), 2, 10, linewidth=1, edgecolor='blue', facecolor='blue')
ax.add_patch(rect)
ax.text(0, 0, 'river', color='white', ha='center', va='center', rotation=90)

#make garden with line
plt.plot([1,8], [-2,-2], color='brown', linewidth=2)
plt.plot([8, 8], [-2, 2], color='brown', linewidth=2)
plt.plot([8, 1], [2, 2], color='brown', linewidth=2)

#make garden
garden = patches.Rectangle((1, -2), 7, 4, linewidth=1, facecolor='green')
ax.add_patch(garden)
ax.text(5.5, 0, 'garden', color='black', ha='center', va='center')

ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("simple_river.png")