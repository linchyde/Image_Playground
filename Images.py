from PIL import  Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
img = Image.open('./random_pics/wolfgang.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')

print(img.size)


# filtered_image = img.filter(ImageFilter.SMOOTH)
# filtered_image2 = img.convert('L')
# filtered_img3 = img.convert('L')
#
# # filtered_image.save('blur', 'png')
# box = (100, 100, 400, 400)
# region = filtered_img3.crop(box)
# filtered_image2.save('grey.png', 'png')
# rotated = filtered_image2.rotate(90)
# resize = filtered_image2.resize((300, 300))

# filtered_image2.show()
