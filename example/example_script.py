from uint16_to_img import convert_uint16 as conv16

# My script is in the folder with my image, so I don't have to give the 
# exact path to the folder
my_file = 'example.uint16'

# I know my file widths are 1456 pixels and heights are 1840
conv16.convert(my_file, width=1456, height=1840, depth=1, img_type='png')

# If you want to save the file with a different name and image type
conv16.convert(my_file, width=1456, height=1840, depth=1, img_type='tiff',
        save_name='test')

# If you want to save the file with a different name and image type, and check 
# that no pixels are lost 
conv16.convert(my_file, width=1456, height=1840, depth=1, img_type='tiff',
        save_name='test', check_pixels=True)

# Check iif some pixels are lost
conv16.compare_file_to_img(my_file, 'test.tiff', width=1456, 
        height=1840, depth=1)
