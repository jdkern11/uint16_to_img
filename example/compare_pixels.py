import cv2
import numpy as np
import png
from uint16_to_img import convert_uint16 as conv16
import struct


fin = open('example.uint16', "rb")
data = []
try:
    while(True):
        data.append(struct.unpack('H', fin.read(2)))
except Exception as e:
    print(e)
    pass


fin.close()
data = [c[0] for c in data]
img = np.array(data).reshape(1840, 1456, 1)


image = cv2.imread('example.png', cv2.IMREAD_UNCHANGED)
print(image.dtype)
quit()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] != image[i][j]:
            print('{}: {}'.format(img[i][j], image[i][j]))
