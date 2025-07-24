import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make garden with line
plt.plot([0, 10], [0, 0], color='brown', linewidth=2)
plt.plot([10, 13], [0, 4], color='brown', linewidth=2)
plt.plot([13, 10], [4, 10], color='brown', linewidth=2)
plt.plot([10, -1], [10, 4], color='brown', linewidth=2)
plt.plot([-1, 0], [4, 0], color='brown', linewidth=2)

#Section off the triangle
plt.plot([-1, 10], [4,0], color = 'red', linewidth=3)
plt.plot([10, 0], [0, 0], color='red', linewidth=3)
plt.plot([0, -1], [0, 4], color='red', linewidth=3)

#create second triangle 
plt.plot([-1, 10], [4,0], color = 'purple', linewidth=3, linestyle='dashed')
plt.plot([10, 3.1], [0, -1.3], color='purple', linewidth=3, linestyle='dashed')
plt.plot([3.1, -1], [-1.3, 4], color='purple', linewidth=3, linestyle='dashed')


# Fill the garden area
garden_x = [0, 10, 13, 10, -1, 0]
garden_y = [0, 0, 4, 10, 4, 0]
plt.fill(garden_x, garden_y, color='green', alpha=0.5)  # green fill with some transparency
ax.text(5, 4, 'garden', color='black', ha='center', va='center', size = 'medium')

#Fill in the sliced triangle a little more darkly
triangle_x = [-1, 10, 0, -1]
triangle_y = [4, 0, 0, 4]
plt.fill(triangle_x, triangle_y, color='green', alpha = 0.75)
ax.text(-1.5, 4, 'A', color = 'red', size = 'large')
ax.text(-0.5, -0.5, 'B', color = 'red', size = 'large')
ax.text(10.5, -0.5, 'C', color = 'red', size = 'large')

#Label B'
ax.text(3.1, -2, 'B`', color = 'purple', size = 'large')
iso_triangle_x = [-1, 10, 3.1, -1]
iso_triangle_y = [4, 0, -1.3, 4]
plt.fill(iso_triangle_x, iso_triangle_y, color='blue', alpha = 0.5)



ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("irreg_pentagon_two_triangles.png")