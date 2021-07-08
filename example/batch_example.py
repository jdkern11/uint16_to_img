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
