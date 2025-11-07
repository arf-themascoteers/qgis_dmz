from qgis.core import QgsApplication
from osgeo import gdal
import os

qgs = QgsApplication([], False)
qgs.initQgis()

src_root = r"C:\Users\m.rahman\mixed\dmz\src"
clipped_root = r"C:\Users\m.rahman\mixed\dmz\clipped"
mask = "C:/temp2/DMS_Owned_Parcel/DMS_Owned_Parcel.shp"

for file in os.listdir(src_root):
    if not file.endswith(".tif"):
        continue
    raster = os.path.join(src_root, file)
    output = os.path.join(clipped_root, file)
    if os.path.exists(output):
        continue
    gdal.Warp(
        output,
        raster,
        cutlineDSName=mask,
        cropToCutline=True
    )

qgs.exitQgis()
