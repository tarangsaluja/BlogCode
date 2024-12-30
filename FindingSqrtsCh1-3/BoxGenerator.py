import matplotlib.pyplot as plt

#initial
fig, ax = plt.subplots()
for i in range(17):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='brown')
    ax.add_patch(rect)


#post-Fatima
ax.arrow(x = 8.5, y = 3.5, dx = 0, dy = -2, width = 0.1, color='red')
ax.annotate('Fatima', xy=(7.5, 4))

for i in range(9):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='red')
    ax.add_patch(rect)

for i in range(9,17):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='green')
    ax.add_patch(rect)


#post - Kate
ax.arrow(x = 12.5, y = 3.5, dx = 0, dy = -2, width = 0.1, color='red')
ax.annotate('Kate', xy=(11.5, 4))

for i in range(13):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='red')
    ax.add_patch(rect)

for i in range(13,17):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='green')
    ax.add_patch(rect)

#post - Nithin
ax.arrow(x = 14.5, y = 3.5, dx = 0, dy = -2, width = 0.1, color='red')
ax.annotate('Nithin', xy=(13.5, 4))

for i in range(14, 17):
    rect = plt.Rectangle((i, 0), 0.75, 0.75, edgecolor='black', facecolor='red')
    ax.add_patch(rect)

ax.set_xlim(0, 17), 
ax.set_ylim(0, 5)
ax.set_aspect('equal')
plt.axis('off')  # Turn off axes
plt.savefig("17_boxes.png")