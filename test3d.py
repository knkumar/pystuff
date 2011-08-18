from mpl_toolkits.mplot3d import axes3d
import matplotlib as plt
plt.use('PS')
from pylab import *

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
print "X - data"
print X
print "Y - data"
print Y
print "Z - data"
print Z
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40)
cset = ax.contour(X, Y, Z, zdir='y', offset=40)

ax.set_xlabel('X')
ax.set_xlim3d(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim3d(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim3d(-100, 100)

plt.savefig("test.ps")

