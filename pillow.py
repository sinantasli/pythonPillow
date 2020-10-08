from PIL import Image , ImageFilter

image = Image.open("kus.jpg")

image.rotate(180).save("kus2.jpg")

image.rotate(65).save("kus3.jpg")

image.convert(mode="L").save("kus4.jpg")

degistir = (960,600)

image.thumbnail(degistir)

image.save("kus5.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("kus6.jpg")

kırpılacak_alan = (340,0,950,600)

image.crop(kırpılacak_alan).save("kus7.jpg")


