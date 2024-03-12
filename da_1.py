from PIL import Image, ImageDraw
import random

# Size of the image
width = 800
height = 800

# Create an image
img = Image.new('RGB', (width, height), "white")
draw = ImageDraw.Draw(img)

# Draw random spots
for i in range(1000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    radius = random.randint(1, 5)
    draw.ellipse((x, y, x + radius, y + radius), fill=(0, 0, 0))

# Save the image
img.save('spot_painting.png')