from PIL import Image

img = Image.open('6805.tif')

img_resize = img.resize((7680, 4320))
img_resize.save('6805_resize_nearest.tif')

img_resize_lanczos = img.resize((7680, 4320), Image.LANCZOS)
img_resize_lanczos.save('6805_resize_lanczos.tif')