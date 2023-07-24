from PIL import Image


def is_tif(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == 'TIFF'
    except IOError:
        return False


print(is_tif('/home/steve/Projects/trees-sat-count/data/mband/01.tif'))
