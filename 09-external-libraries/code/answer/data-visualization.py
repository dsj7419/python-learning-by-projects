import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Data related to planets in our solar system
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
mass = [0.055, 0.815, 1, 0.107, 318, 95, 14.5, 17.1]  # relative to Earth
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.5, 1433.5, 2872.5, 4495.1]  # in million km
num_of_moons = [0, 0, 1, 2, 79, 82, 27, 14]

# Creating a Figure and Axes instances
fig, axs = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle("Planetary Dashboard", fontsize=16, fontweight='bold')

# Plot 1: Bar chart showing the mass of the planets relative to Earth
axs[0].bar(planets, mass, color='skyblue')
axs[0].set_ylabel("Mass (relative to Earth)")
axs[0].set_title("Mass of Planets in our Solar System")

# Plot 2: Scatter plot showing distance from the sun vs. number of moons
scatter = axs[1].scatter(distance_from_sun, num_of_moons, s=[200]*8, c=mass, cmap='viridis', alpha=0.7)
axs[1].set_xlabel("Distance from Sun (million km)")
axs[1].set_ylabel("Number of Moons")
axs[1].set_title("Distance from Sun vs. Number of Moons")

# Creating a colorbar for the scatter plot
cbar = plt.colorbar(scatter, ax=axs[1], orientation='vertical')
cbar.set_label('Mass (relative to Earth)', rotation=90)

# Annotating the scatter plot with planet names
for i, txt in enumerate(planets):
    axs[1].annotate(txt, (distance_from_sun[i], num_of_moons[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Plot 3: Pie chart showing the share of total number of moons by each planet
axs[2].pie(num_of_moons, labels=planets, autopct='%1.1f%%', shadow=True, startangle=140, colors=plt.cm.Paired.colors)
axs[2].set_title("Share of Total Number of Moons")

# Adjusting layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Displaying the plots
plt.show()
