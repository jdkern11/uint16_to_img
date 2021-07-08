import struct
import os
import logging
logging.basicConfig(level=logging.INFO)

import numpy as np
import png


def convert(file_path: str, width: int, height: int, depth: int=1, 
        img_type: str='tiff', save_name: str=None):
    """Converts uint16 files to images

    You must provide the accurate width, height and depth dimensions of the 
    file.

    Args:
        file_path (str):
            Path to file
        width (int):
            Width of uint16 images
        height (int):
            Height of uint16 images
        depth (int):
            Depth of uint16 images
        img_type (str):
            Optional. Type of image to create. Default is tiff.
        save_name (str):
            Optional. If None added, files save as the same name as the
            file_path, but as .tiff (or png, etc...) instead.
            
    """
    if save_name is None:
        save_name = os.path.splitext(file_path)[0]
    save_name += ('.' + img_type)
    logging.info('Saving file to ' + save_name)

    fin = open(file_path, "rb")
    data = []
    try:
        while(True):
            data.append(struct.unpack('H', fin.read(2)))
    except Exception as e:
        pass

    data = [c[0] for c in data]
    img = np.array(data).reshape(height, width, depth)
    with open(save_name, 'wb') as f:
        writer = png.Writer(width=img.shape[1], height=img.shape[0], bitdepth=16)
        # Convert z to the Python list of lists expected by
        # the png writer.
        w_img = img.reshape(-1, img.shape[1]*img.shape[2]).tolist()
        writer.write(f, w_img)
        logging.info('{} saved.'.format(save_name))
