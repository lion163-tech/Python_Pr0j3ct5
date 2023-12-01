import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure and axis
fig, ax = plt.subplots()

# Draw the head of the fox
head = patches.Circle((0.5, 0.5), 0.2, linewidth=2, edgecolor='black', facecolor='red')
ax.add_patch(head)

# Draw the body of the fox
body = patches.Rectangle((0.3, 0.2), 0.4, 0.3, linewidth=2, edgecolor='black', facecolor='red')
ax.add_patch(body)

# Draw the tail of the fox
tail = patches.FancyArrow(0.2, 0.35, 0.15, 0, width=0.02, color='black')
ax.add_patch(tail)

# Draw the eyes
left_eye = patches.Circle((0.4, 0.6), 0.03, facecolor='white')
right_eye = patches.Circle((0.6, 0.6), 0.03, facecolor='white')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Draw the nose
nose = patches.RegularPolygon((0.5, 0.52), numVertices=6, radius=0.02, facecolor='black')
ax.add_patch(nose)

# Set the aspect ratio to be equal
ax.set_aspect('equal', 'box')

# Remove axes for a cleaner look
ax.axis('off')

# Show the fox
plt.show()
