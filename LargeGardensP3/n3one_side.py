import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make river
rect = patches.Rectangle((-1, -5), 2, 10, linewidth=1, edgecolor='blue', facecolor='blue')
ax.add_patch(rect)
ax.text(0, 0, 'river', color='white', ha='center', va='center', rotation=90)


#make garden with line
plt.plot([1, 5.4], [5, 2.5], color='brown', linewidth=2)
plt.plot([5.4, 5.4], [2.5, -2.5], color='brown', linewidth=2)
plt.plot([5.4, 1], [-2.5, -5], color='brown', linewidth=2)


# Fill the garden area
garden_x = [1, 5.4, 5.4, 1]
garden_y = [5, 2.5, -2.5, -5]
plt.fill(garden_x, garden_y, color='green', alpha=0.5)  # green fill with some transparency
ax.text(4, 0, 'garden', color='black', ha='center', va='center')


ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("n3one_side.png")