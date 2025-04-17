import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make river
rect = patches.Rectangle((-1, -5), 2, 10, linewidth=1, edgecolor='blue', facecolor='blue')
ax.add_patch(rect)
ax.text(0, 0, 'river', color='white', ha='center', va='center', rotation=90)


#make garden with line
plt.plot([1,4], [5, 1], color='brown', linewidth=2)
plt.plot([4,3], [1, -2], color='gray', linewidth=2)
plt.plot([3,4], [-2, -5], color='gray', linewidth=2)
plt.plot([4,1], [-5, -5], color='brown', linewidth=2)

# Fill the garden area
garden_x = [1, 4, 3, 4, 1]
garden_y = [5, 1, -2, -5, -5]
plt.fill(garden_x, garden_y, color='green', alpha=0.5)  # green fill with some transparency
ax.text(2, 0, 'garden', color='black', ha='center', va='center')

#extension line
plt.plot([4,5], [1, -2], color='red', linewidth=2)
plt.plot([5,4], [-2, -5], color='red', linewidth=2)

gardenext_x = [4, 5, 4, 3]
gardenext_y = [1, -2, -5, -2]
plt.fill(gardenext_x, gardenext_y, color='green')





plt.axis('off')  # Turn off axes
plt.savefig("wonkyshape_extended.png")