import os.path

from PIL import Image, ImageDraw, ImageFont

path = './images'
new_path = './updated images//'
dirs = os.listdir(path)


def crop():
    for i in dirs:
        fullpath = os.path.join(path, i)
        if os.path.isfile(fullpath):
            image = Image.open(fullpath)
            file_name = os.path.basename(fullpath)
            f, e = os.path.splitext(file_name)

            width, height = image.size
            new_width, new_height = 1080, 1080

            left = (width - new_width) / 2
            top = (height - new_height) / 2
            right = (width + new_width) / 2
            bottom = (height + new_height) / 2

            new_image = image.crop((left, top, right, bottom))
            new_image.save(new_path + f + '.jpg', "JPEG", quality=100)


crop()

water_path = './updated images//'
water_dirs = os.listdir(water_path)


def watermark():
    for i in water_dirs:
        fullpath = os.path.join(water_path, i)
        if os.path.isfile(fullpath):
            image = Image.open(fullpath)
            file_name = os.path.basename(fullpath)
            f, e = os.path.splitext(file_name)

            width, height = image.size
            draw = ImageDraw.Draw(image)
            text = "AUSTIN TEXAS"

            font = ImageFont.truetype('Arial.ttf', 40)
            text_width, text_height = draw.textsize(text, font)

            margin = 50
            x = width - text_width - margin
            y = height - text_height - margin

            draw.text((x, y), text, font=font)
            image = image.convert(mode='L')
            image.save(water_path + f + '.jpg', 'JPEG')


watermark()