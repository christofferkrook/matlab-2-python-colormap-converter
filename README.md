# matlab-2-python-colormap-converter
Converts .txt-files with rows of comma-delimited rbg-values as a colormap to a colormap which you can use in python.

HOW TO USE IT

import import matlab_colormap_2_python_colormap

import matplotlib.pyplot as plt

colorm = matlab_colormap_2_python_colormap.conv_matlab_cmap_to_python("directory/colormmap_file.txt")

plt.imshow(your_data, cmap=colorm)
