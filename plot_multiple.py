import pandas as pd
import numpy as np
import numpy.random
import pandas as pd
from astropy.convolution import convolve
import matplotlib.pyplot as plt
from astropy.convolution.kernels import Gaussian2DKernel
import scipy.ndimage as spnd
from matplotlib.colors import LogNorm



ldv_x = []
ldv_y = []
ldv_z = []
ldv = pd.read_csv('./differenced_ldv.csv')
for index, row in ldv.iterrows():
    ldv_x.append(row['x_bucket'])
    ldv_y.append(row['y_bucket'])
    ldv_z.append(row['difference_PM2.5'])

heatmap_ldv, xedges_ldv, yedges_ldv = np.histogram2d(ldv_x, ldv_y, bins=500, weights=[w*100+40 for w in ldv_z])
extent_ldv = [yedges_ldv[0], yedges_ldv[-1], xedges_ldv[0], xedges_ldv[-1]]

im = plt.imshow(convolve(heatmap_ldv, Gaussian2DKernel(stddev=2)), extent=extent_ldv, cmap='inferno', vmin=0, vmax=100)

plt.colorbar()

plt.show()

bus_x = []
bus_y = []
bus_z = []
bus = pd.read_csv('./differenced_bus.csv')
for index, row in bus.iterrows():
    bus_x.append(row['x_bucket'])
    bus_y.append(row['y_bucket'])
    bus_z.append(row['difference_PM2.5'])
heatmap_bus, xedges_bus, yedges_bus = np.histogram2d(bus_x, bus_y, bins=500, weights=[w*100+40 for w in bus_z])
extent_bus = [yedges_bus[0], yedges_bus[-1], xedges_bus[0], xedges_bus[-1]]

taxi_x = []
taxi_y = []
taxi_z = []
taxi = pd.read_csv('./differenced_taxi.csv')
for index, row in taxi.iterrows():
    taxi_x.append(row['x_bucket'])
    taxi_y.append(row['y_bucket'])
    taxi_z.append(row['difference_PM2.5'])
heatmap_taxi, xedges_taxi, yedges_taxi = np.histogram2d(taxi_x, taxi_y, bins=500, weights=[w*100+40 for w in taxi_z])
extent_taxi = [yedges_taxi[0], yedges_taxi[-1], xedges_taxi[0], xedges_taxi[-1]]

heatmaps=[heatmap_taxi, heatmap_taxi, heatmap_bus, heatmap_ldv]

im = plt.imshow(convolve(heatmap_taxi, Gaussian2DKernel(stddev=2)), extent=extent_ldv, cmap='inferno', vmin=0, vmax=100)

plt.colorbar()

plt.show()

im = plt.imshow(convolve(heatmap_bus, Gaussian2DKernel(stddev=2)), extent=extent_ldv, cmap='inferno', vmin=0, vmax=100)

plt.colorbar()

plt.show()



'''fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolor(x, y, z,
                   norm=colors.LogNorm(vmin=min(z), vmax=max(z)),
                   cmap='Greys')
fig.colorbar(pcm, ax=ax[0], extend='max')

pcm = ax[1].pcolor(x, y, z, cmap='Greys')
fig.colorbar(pcm, ax=ax[1], extend='max')
fig.show()'''

'''from astropy.convolution.kernels import Gaussian2DKernel
plt.pcolor(convolve(heatmap, Gaussian2DKernel(stddev=2)), cmap='inferno')
plt.colorbar()

plt.show()'''
