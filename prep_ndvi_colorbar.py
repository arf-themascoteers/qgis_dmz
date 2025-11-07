import os
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from matplotlib import cm, colors

src_root = r"C:\Users\m.rahman\mixed\dmz\clipped"
exported_root = r"C:\Users\m.rahman\mixed\dmz\ndvi2"

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

    fig, ax = plt.subplots(figsize=(6,6))
    im = ax.imshow(rgba, origin='upper')
    ax.axis('off')
    cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
    cbar.set_label('NDVI value')
    plt.savefig(output, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
