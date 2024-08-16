from PIL import Image
image = Image.open('image.jpg')
#image.show()
gray_image = image.convert('L')
resize_image = gray_image.resize((500,250))
resize_image.save('resizedby6.2.jpg')#.png тоже можно

