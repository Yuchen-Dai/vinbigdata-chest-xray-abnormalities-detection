import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import glob
from PIL import Image

import matplotlib.pyplot as plt



def read_xray(path, voi_lut=True, fix_monochrome=True):
    dicom = pydicom.read_file(path)

    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array

    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data

    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)

    return data

if __name__ == '__main__':
    files = glob.glob(r'train/*.dicom')
    for f in files:

        img = read_xray(f)
        im = Image.fromarray(img)
        im.save(f"data/{f[:-6]}.jpg")
        
