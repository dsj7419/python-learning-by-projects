# Import necessary libraries/modules
import matplotlib.pyplot as plt

# Data related to planets in our solar system
# Hint: You might need to provide data for each planet like its name, mass, distance from the sun, and number of moons.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# Add other data lists here...

# Creating a Figure and Axes instances
# Hint: Define a figure with multiple subplots for each of your visualizations. Decide on the layout of your dashboard.
fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # Example: creates a 3x1 grid of subplots

# Title for the entire figure/dashboard
# TODO: Add a suptitle to the figure.

# Plot 1: Bar chart showing the mass of the planets relative to Earth
# TODO: Create a bar chart using the appropriate plotting function. Make sure to label axes and add a title.
axs[0].bar(planets, [1] * len(planets))  # Replace the second argument with actual data
# Add labels and title...

# Plot 2: Scatter plot showing distance from the sun vs. number of moons
# TODO: Create a scatter plot visualizing the relationship between distance from the sun and the number of moons.
# Consider encoding another dimension of data using color or size of the scatter points.
# Add labels and title...

# Plot 3: Pie chart showing the share of total number of moons by each planet
# TODO: Create a pie chart representing the proportion of moons that each planet has.
# Make sure to label each section of the pie chart and add a title.
# Add labels and title...

# Adjusting layout
# Hint: Adjust the layout to ensure the plots are organized and non-overlapping.
plt.tight_layout()

# Displaying the plots
# TODO: Display the plots using plt.show() or save the figure using plt.savefig().
