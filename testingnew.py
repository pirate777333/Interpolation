import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from scipy.interpolate import griddata
import numpy as np
import pandas as pd

##df=pd.read_csv('testing_z.csv')
##
##x = list(df.x_axis.values) #1D
##y = list(df.y_axis.values) #1D
##Z = list(df.z_axis.values) #1D
##
##extent = (0.0007190530413037077, 99.9859991089324, 0.02118211044100926, 149.97696465048583)
##xs,ys = np.mgrid[extent[0]:extent[1]:10000j, extent[2]:extent[3]:10000j] #2D x,y
##Z_resampled = griddata((x, y), Z, (xs, ys)) #2D z
##
##
##plt.imshow(Z_resampled, interpolation="gaussian", extent=extent, origin="lower")
##plt.show()

x=[0,0,10,10,1,2,3,4,5,6,7,8,9,10,2,3,4,7,8,9,2,3,4,7,8,9,2,3,4,7,8,9,2,3,4,7,8,9,5.5,5.5,5.5,5.5,5.5,5.5,5.5,5.5,5.5,5.5]
y=[0,10,0,10,6,6,6,6,6,6,6,6,6,6,4,4,4,4,4,4,3,3,3,3,3,3,9,9,9,9,9,9,8,8,8,8,8,8,1,2,3,4,5,6,7,8,9,10]

Z=[0,0,0,0,10,10,10,10,10,10,10,10,10,10,5,5,5,5,5,5,1,1,5,5,1,1,1,1,5,5,1,1,5,5,5,5,5,5,10,10,10,10,10,10,10,10,10,10]
#print(len(x),len(y),len(Z))
plt.figure(figsize=(10,10))
plt.scatter(x,y)
#plt.axis('off')
#plt.savefig('dots.png')
plt.show()
extent = (0,10,0,10)
xs,ys = np.mgrid[extent[0]:extent[1]:10j, extent[2]:extent[3]:10j] #2D x,y
Z_resampled = griddata((x, y), Z, (xs, ys)) #2D z

plt.figure(figsize=(10,10))
plt.imshow(Z_resampled, interpolation="gaussian", extent=extent, origin="lower")
#plt.axis('off')
#plt.savefig('interP.png')
plt.show()
