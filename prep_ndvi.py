import os
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from matplotlib import cm, colors

src_root = r"C:\Users\m.rahman\mixed\dmz\clipped"
exported_root = r"C:\Users\m.rahman\mixed\dmz\ndvi"

for file in os.listdir(src_root):
    if not file.endswith(".tif"):
        continue
    raster = os.path.join(src_root, file)
    png_name = os.path.splitext(file)[0] + ".png"
    output = os.path.join(exported_root, png_name)
    if os.path.exists(output):
        continue
    ds = gdal.Open(raster)
    arr = ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
    mask0 = arr == 0
    norm = colors.Normalize(vmin=-1, vmax=1)
    cmap = plt.colormaps['RdYlGn']
    rgba = cmap(norm(arr))
    rgba[mask0, :] = [1,1,1,0]

    plt.imsave(output, rgba)