from PIL import Image
import sys, os

img_path = sys.argv[1]

if not os.path.exists(img_path):
    print(f"{img_path} not found")
    exit()

image = Image.open(img_path)
crop_box = (0, 0, 1080, 1080)
size = image.size
width = size[0]
height = size[1]
multiple = width / 1080

if (width % 1080) != 0:
    print(f'Width is not a multiple of 1080 instead it is {width}')
    exit()

if height != 1080:
    print(f'Height is not 1080 instead it is {height}')
    exit()

stripped = img_path.split('.')[0]
extension = img_path.split('.')[1]
out_path = f'{stripped}_out'
os.mkdir(out_path)

for i in range(0, multiple):
    crop_box = (i * 1080, 0, 1080, 1080)
    image = image.crop(crop_box)
    path = os.path.join(out_path, "image" + str(i) + extension)
    image.save(path)