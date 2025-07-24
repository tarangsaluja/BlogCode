import matplotlib.pyplot as plt
import matplotlib.patches as patches

#initial
fig, ax = plt.subplots()

#make square with line
plt.plot([0, 5], [0, 0], color='brown', linewidth=2)
plt.plot([5, 5], [0, 5], color='brown', linewidth=2)
plt.plot([5, 0], [5, 5], color='brown', linewidth=1)
plt.plot([0, 0], [5, 0], color='brown', linewidth=2)

#make triangle
plt.plot([5, 0], [5, 5], color='blue', linewidth=1)
plt.plot([0, 2.5], [5, 9.3], color='blue', linewidth=2)
plt.plot([2.5, 5], [9.3, 5], color='blue', linewidth=2)

#lable vertices
ax.text(-0.5, 0, 'D', color = 'red', size = 'large')
ax.text(5.25, 0, 'C', color = 'red', size = 'large')
ax.text(5.25, 5, 'B', color = 'red', size = 'large')
ax.text(2.5, 9.5, 'A', color = 'red', size = 'large')
ax.text(-0.5, 5, 'E', color = 'red', size = 'large')




ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("pent_construction.png")
