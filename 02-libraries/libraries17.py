from PIL import Image

im = Image.open("incredibles.png")
thumbail = im.crop((280, 0, 360, 80))
thumbail.save("thumbnail.png")
