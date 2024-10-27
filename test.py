from PIL import Image
from PIL import ImageFilter, ImageEnhance

with Image.open('download.jpg') as picture:
    print("Розмір зображення", picture.size)
    print("Формат зображення", picture.format)
    print("Тип зображення", picture.mode)
    picture.show()

    grey = picture.convert("L")
    grey.save("grey.jpg")
    grey.show()

    rotated = picture.transpose(Image.ROTATE_180)
    rotated.save("rotated.jpg")
    rotated.show()

    flipped = picture.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save("flipped.jpg")
    flipped.show()

    contrast = ImageEnhance.Contrast(picture)
    contrast = picture.enhance(1.5)
    contrast.save("contrast.jpg")
    contrast.show()