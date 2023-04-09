import os
from PIL import Image
import sys

# input_folder = sys.argv[1]
# output_folder = sys.argv[2]

input_folder = ('images')
output_folder = ('converted_img')

path = f'./{output_folder}/'
fold = os.path.exists(path)

if fold is False:
    os.mkdir(f'./{output_folder}/')

mnfold = os.listdir(f'./{input_folder}/')

print(mnfold)

for filename in mnfold:
    i = Image.open(f'./{input_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    i.save(f'./{output_folder}/{clean_name}.png', 'png')
