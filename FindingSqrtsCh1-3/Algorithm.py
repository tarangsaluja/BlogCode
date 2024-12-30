import matplotlib.pyplot as plt
#initial
fig, ax = plt.subplots()

#box dictionary
boxes = {
    "Input": (1, 0, 6, 3), 
    "Algorithm": (11, 0, 6, 3),
    "Output": (21, 0, 6, 3)
}

#create the boxes
for label, (x, y, width, height) in boxes.items():
    if label == "Algorithm":
        ax.add_patch(plt.Rectangle((x, y), width, height, fill = True, color = "skyblue", edgecolor="black"))
    else:
        ax.add_patch(plt.Rectangle((x, y), width, height, fill = True, color = "pink", edgecolor="black"))

    ax.text(x + width / 2, y + height / 2, label, ha="center", va="center", fontsize=12)

#create the narrows
ax.annotate("", xy=(10.5, 1.5), xytext=(7.5, 1.5), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(20.5, 1.5), xytext=(17.5, 1.5), arrowprops=dict(arrowstyle="->", lw=1.5))

ax.set_xlim(0, 30), 
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.axis('off') 
plt.savefig("flow_chart.png")