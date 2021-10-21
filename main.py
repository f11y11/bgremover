from genericpath import isdir
from PIL import Image
from os import listdir, mkdir
from os.path import join, isfile, dirname, realpath

PATH = dirname(realpath(__file__))

files = [f for f in listdir(PATH) if isfile(join(PATH, f))]
files = [f for f in filter(lambda f: f.endswith(('.png', '.jpg', '.jpeg')) and not 'edited' in f, files)]

for f in files:
    data = []
    image = Image.open(realpath(join(PATH, f))).convert('RGBA')
    for pixel in image.getdata():
        if (pixel[0], pixel[1], pixel[2]) == (255, 255, 255):
            data.append((255, 255, 255, 0))
        else:
            data.append(pixel)

    image.putdata(data)
    if not isdir(join(PATH, 'results')): mkdir(join(PATH, 'results'))
    image.save(join(PATH, 'results', f'edited{files.index(f)}.png'))
