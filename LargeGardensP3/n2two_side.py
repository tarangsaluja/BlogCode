import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make river
# rect = patches.Rectangle((-0.005, -5), 0.01, 10, linewidth=1, edgecolor='blue', facecolor='blue')
# ax.add_patch(rect)


#make garden with line
plt.plot([0,6.5], [5, 0], color='brown', linewidth=2)
plt.plot([6.5, 0], [0, -5], color='brown', linewidth=2)
plt.plot([0,-6.5], [5, 0], color='brown', linewidth=2)
plt.plot([-6.5, 0], [0, -5], color='brown', linewidth=2)
plt.plot([0, 0], [5, -5], color='blue', linewidth=3)


# Fill the garden area
garden_x = [0, 6.5, 0, -6.5]
garden_y = [5, 0, -5, 0]
plt.fill(garden_x, garden_y, color='green', alpha=0.5)  # green fill with some transparency
ax.text(0, 0, 'garden', color='black', ha='center', va='center')



ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("n2two_side.png")