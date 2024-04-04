import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a Basemap instance centered on Bangladesh
m = Basemap(projection='merc', llcrnrlat=20, urcrnrlat=27, llcrnrlon=88, urcrnrlon=93, resolution='i')

# Draw coastlines, countries, and states
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Fill the land area with a color (yu can  pick any color)
m.fillcontinents(color='lightgray', lake_color='aqua')

# Draw the boundary of Bangladesh
m.drawcountries(linewidth=2)

# give a title
plt.title('Bangladesh')

#map displaying
plt.show()
