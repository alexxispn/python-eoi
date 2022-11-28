from PIL import Image, ImageFilter

crome = Image.open("croma.png")
(width, height) = crome.size
mask = Image.new("L", (width, height), 0)
crome_map = crome.load()
mask_map = mask.load()

for x in range(width):
    for y in range(height):
        red, green, blue, alpha = crome_map[x, y]
        if green > blue + red:
            mask_map[x, y] = 0
        else:
            mask_map[x, y] = 255

background = Image.open("fondo.jpg")
background = background.resize((width, height))
mask = mask.filter(ImageFilter.GaussianBlur(5))
background.paste(crome, (0, 0), mask)
background.show()
