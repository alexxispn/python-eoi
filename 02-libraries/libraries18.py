from PIL import Image

im = Image.open("leon.png")
region = im.crop((150, 320, 280, 440))
region.save("box_leon.png")

reverse = region.transpose(Image.Transpose.ROTATE_180)
reverse.save("reverse_leon.png")

im.paste(reverse, (150, 320, 280, 440))
im.save("leon2.png")

r, g, b = im.split()
r.save("leon_r.png")
g.save("leon_g.png")
b.save("leon_b.png")


