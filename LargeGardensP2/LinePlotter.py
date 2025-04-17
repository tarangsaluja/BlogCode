import matplotlib.pyplot as plt

# Ask for the number of lines
num_lines = int(input("Enter the number of lines to graph: "))

# Initialize a list to store each line's color and coordinates
lines_data = []

# Collect color and coordinates for each line
for i in range(num_lines):
    color = input(f"Enter the color for line {i + 1}: ")
    coordinates = input(f"Enter two coordinate pairs for line {i + 1} (e.g., x1,y1,x2,y2): ").split(',')
    
    # Convert the coordinates to integers
    x1, y1, x2, y2 = map(int, coordinates)
    
    # Store the color and coordinates in the list
    lines_data.append((color, (x1, y1), (x2, y2)))

# Plot the lines
plt.figure()

for color, (x1, y1), (x2, y2) in lines_data:
    plt.plot([x1, x2], [y1, y2], color=color)

plt.title('Graph of Multiple Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.grid(True)
plt.show()