import sys
import os
from pathlib import Path
from PIL import Image

main_path = os.getcwd()

#grab the first and the second arg
image_folder = f'{main_path}/Pokedex/'
output_folder = f'{main_path}/New/'

#check if the new folder exists, if not create it
Path(output_folder).mkdir(parents=True, exist_ok=True)


#loop through folder and convert images to .png
for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done')
