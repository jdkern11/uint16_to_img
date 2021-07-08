# uint16\_to\_img
This package converts uint16 files into images

## Author
Joseph Kern (jkern34@gatech.edu)  
If you use this for academic purposes please add me to your acknowledgments :-)

## Install
### pip install
`pip install https://github.com/jdkern11/uint16_to_img.git`  
or  
`pip install git@github.com/jdkern11/uint16_to_img.git`

### Anaconda install
1. Install anaconda or miniconda
2. In your terminal type `conda create --name ui16_to_img python=3.7`
3. Then type `conda activate ui16_to_img`
4. Finally, in your terminal [run pip install](#pip-install)

## Usage

To run in python, write a similar script to this.

```Python
from uint16_to_img import convert_uint16 as conv16

# My script is in the folder with my image, so I don't have to give the 
# exact path to the folder
my_file = 'example.uint16'

# I know my file widths are 1456 pixels and heights are 1840
conv16.convert(my_file, width=1456, height=1840, depth=1, img_type='tiff')
```

width is the width of your images in pixels, height the height in pixels,
and depth the depth (if you have a colored image this will be 3, if you have
a colored image with an alpha value, then it will be 4). img\_type is optional
and defaults to tiff.

If you want to control where the images are saved, you can use the save\_name
parameter.
```Python
# If you want to save the file with a different name
conv16.convert(my_file, width=1456, height=1840, depth=1, img_type='tiff',
               save_name='test')
```

If you want to do batch processing, I would suggest putting all the related
files in a separate folder, then running something like the following code:
```Python
import os
from uint16_to_img import convert_uint16 as conv16

# Lists contents of directory
batch_folder = 'example_batch'
files = os.listdir(batch_folder)
# Ensure only uint16 files are used
files = [f for f in files if '.uint16' in f]

# Want to save files in a separate folder
my_img_folder = 'example_batch_img_folder'
# Throws error if older already exists
try:
    os.mkdir(my_img_folder)
except Exception as e:
    pass

for f in files:
    # Remove .uint16 part of name
    save_name = os.path.splitext(f)[0]
    # save to the correct folder
    save_name = os.path.join(my_img_folder, save_name)
    # Need to make sure code knows where the files are located
    file_path = os.path.join(batch_folder, f)
    conv16.convert(file_path, width=1456, height=1840, save_name=save_name)
```

## FAQ
### What should I do if I have an error?
Add it to the issues tab on github or email me

### I need help with a similar problem but a different file type
You can email me
