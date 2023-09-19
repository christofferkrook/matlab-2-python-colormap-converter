import numpy as np
import matplotlib.colors as mcolors

def conv_matlab_cmap_to_python(dir):
    data = np.loadtxt(dir)
    colorm = []
    xvals = np.linspace(0, 1, len(data[:, 0]))
    for i in range(len(data[:, 0])):
        colorm.append((xvals[i], mcolors.rgb2hex((data[i, 0], data[i, 1], data[i, 2]))))
    return mcolors.LinearSegmentedColormap.from_list('my_colormap', colorm, N=256)