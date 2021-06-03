from scipy.ndimage.interpolation import rotate
x = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
r = rotate(x, angle=45)
print(r)