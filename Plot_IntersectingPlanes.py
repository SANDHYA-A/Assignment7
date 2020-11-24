# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:07:41 2020

@author: sandhya
"""

'''Plot from individual equation of planes'''
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(num=1, clear=True)
ax = fig.add_subplot(1, 1, 1, projection='3d')

(x, y) = np.meshgrid(np.arange(-2, 2.1, 1), np.arange(-1, 1, .25))
k =2/(((2*(13)**0.5))**0.5 +5)
k1 = (((-2*(13)**0.5) +5)**0.5)/2
z = k*( -x-y*k1)

ax.plot_surface(x, y, z)
(x1, y1) = np.meshgrid(np.arange(-2, 2.1, 1), np.arange(-1, 1, .25))
k3 =2*(((2*(13)**0.5))**0.5 +5)
k4 = (((-2*(13)**0.5) +5)**0.5)*2
z1 = (4*x1-y1*k4)/k3


ax.plot_surface(x1, y1, z1)
ax.set(xlabel='x', ylabel='y', zlabel='z')
#ax.set_title(r'(x + $\frac{\sqrt{5-2\sqrt{13}}}{2}$y + $\frac{\sqrt{5+2\sqrt{13}}}{2}$z)(-4x + $2\sqrt{5-2\sqrt{13}}$y + $2\sqrt{5+2\sqrt{13}}$z) =0 ')
ax.set_title(r'$-4x^{2} + (5-2\sqrt{13})y^{2} + (5+2\sqrt{13})z^2=0$ ')
fig.tight_layout()
plt.savefig('./planes.jpg')
plt.show()

'''
(x2, y2) = np.meshgrid(np.arange(-2, 2.1, 1), np.arange(-1, 1, .25))

#z2 = (3*x2-2*y2-1)


ax.plot_surface(x2, y2, z2)
ax.set(xlabel='x', ylabel='y', zlabel='z', title='Intersecting planes')
fig.tight_layout()

(x3, y3) = np.meshgrid(np.arange(-2, 2.1, 1), np.arange(-1, 1, .25))

#z3 = (3*x3+2*y3+1)


ax.plot_surface(x3, y3, z3)
ax.set(xlabel='x', ylabel='y', zlabel='z', title='Intersecting planes')
'''
