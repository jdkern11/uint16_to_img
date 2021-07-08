import struct
import numpy as np
import png

fin = open("Corrected1372.uint16", "rb")
data = []
try:
    while(True):
        data.append(struct.unpack('H', fin.read(2)))
except Exception as e:
    print("End of file")

data = [c[0] for c in data]
#img = np.array(data).reshape(1456, 1840)
img = np.array(data).reshape(1840, 1456)
with open('img.tiff', 'wb') as f:
    writer = png.Writer(width=img.shape[1], height=img.shape[0], bitdepth=16)
    # Convert z to the Python list of lists expected by
    # the png writer.
    z2list = img.reshape(-1, img.shape[1]).tolist()
    writer.write(f, z2list)
