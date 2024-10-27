from PIL import Image, ImageFilter

class ImageEditor:
    def __init__(self, filename):
        self.filename =filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("File not found!")
        self.original.show()

    def rotate_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        temp = self.filename.split(".")
        new = temp[0] + str(len(self.changed)) + ".jpg"
        rotated.save(new)

    def crop_image(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        temp = self.filename.split(".")
        new = temp[0] + str(len(self.changed)) + ".jpg"
        cropped.save(new)

img = ImageEditor("download.jpg")
img.open()

img.rotate_left()
img.crop_image()

for i in img.changed:
    i.show()