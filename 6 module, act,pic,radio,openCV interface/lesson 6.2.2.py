from PIL import Image, ImageDraw
image = Image.open('image.jpg')
draw = ImageDraw.Draw(image)
draw.ellipse((200,200,300,300),fill=(255,0,0))
image.save('draw6.2.2.png')

