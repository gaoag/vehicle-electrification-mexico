import pandas as pd
import numpy as np
import numpy.random
import pandas as pd
from astropy.convolution import convolve
import matplotlib.pyplot as plt
from astropy.convolution.kernels import Gaussian2DKernel
import scipy.ndimage as spnd
from matplotlib.colors import LogNorm



x = []
y = []
z = []
df_to_edit = pd.read_csv('./differenced_bus.csv')
for index, row in df_to_edit.iterrows():
    x.append(row['x_bucket'])
    y.append(row['y_bucket'])
    z.append(row['difference_PM2.5'])

heatmap, xedges, yedges = np.histogram2d(x, y, bins=500, weights=z)
extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

plt.clf()
plt.title('PM2_5 heatmap example')
plt.ylabel('y')
plt.xlabel('x')
#plt.pcolor(heatmap, cmap='Greys', norm=LogNorm(vmin=min(z), vmax=max(z)))
plt.imshow(convolve(heatmap, Gaussian2DKernel(stddev=2)), extent=extent, cmap='inferno')
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
