import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图


def set_sphere_projection(HEIGHT, WIDTH):
	'''initialize the (x,y,z) unit sphere coordinate'''
	direction_x = np.zeros((HEIGHT,WIDTH))
	direction_y = np.zeros((HEIGHT,WIDTH))
	direction_z = np.zeros((HEIGHT,WIDTH))
	p = np.arccos((2 * np.arange(1, HEIGHT+1) / (HEIGHT+1)) -1) 
	q = 2 * np.pi * np.arange(WIDTH) / WIDTH
	direction_x = np.outer(np.sin(p), np.cos(q)) # col vector * row vector
	direction_y = np.outer(np.sin(p), np.sin(q))
	direction_z += np.cos(p)[:, np.newaxis] # col vector, horizontal broadcast
	return direction_x, direction_y, direction_z

def marsaglia(numbers):
	X, Y, Z = [], [], []
	u = np.random.uniform(-1, 1, (numbers))
	v = np.random.uniform(-1, 1, (numbers))
	r2 = np.array((u**2 + v**2) < 1) + 0
	index = np.argwhere(r2>=1)
	for i in index:
		uu, vv = u[i], v[i]
		x = 2 * uu * np.sqrt(1 - (uu**2 + vv**2))
		y = 2 * vv * np.sqrt(1 - (uu**2 + vv**2))
		z = 1 - 2 * (uu**2 + vv**2)
		X.append(x)
		Y.append(y)
		Z.append(z)
	X, Y, Z = np.array(X), np.array(Y), np.array(Z)
	return X, Y, Z


if __name__ == '__main__':
	x, y, z = marsaglia(3600)
	# x, y, z = set_sphere_projection(60, 60)
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(x, y, z)
	ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
	ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
	ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
	plt.show()