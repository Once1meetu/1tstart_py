from PIL import Image
image = Image.open('image.jpg')
#image.show()
gray_image = image.convert('L')
resize_image = gray_image.resize((500,250))
resize_image.save('resizedby6.2.jpg')#.png тоже можно
#gray_image.rotate(45)
#gray_image.crop(100,100,400,400)
"""
for x in [0,200]:
    for y in [0,200]:
        image.putpixel((x,y),(255,0,0))
image.save('reddottedimageby6.2.png')
"""
