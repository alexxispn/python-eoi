from PIL import Image
from PIL import ImageDraw

image = Image.open("leon.png")
width, height = image.size
canvas = ImageDraw.Draw(image)
for x in range(0, width, 100):
    canvas.line((x, 0, x, height), fill="white", width=12)
for y in range(0, height, 100):
    canvas.line((0, y, width, y), fill="white", width=12)
image.save("leon_grid.png")
