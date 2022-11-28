from PIL import Image, ImageDraw

im = Image.open("incredibles.png")
WIDTH, HEIGHT = im.size
canvas = ImageDraw.Draw(im, "RGBA")
txt = f"{WIDTH}x{HEIGHT} pixels"

width, height = canvas.textsize(txt)
print(width, height)

x = (WIDTH // 2) - (width // 2)
y = (HEIGHT // 2) - (height // 2)
rect = (x, y, x + width, y + height)
canvas.rectangle(rect, fill="red")
canvas.text((x, y), txt, fill="white")
im.save("incredibles_text.png")
