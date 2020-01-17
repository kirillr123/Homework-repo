from PIL import Image
import os


def compress_image(image, desired_volume, size=(256, 256)):
    quality = 100
    fname = f"{image.filename[5::-1][::-1]}_thumbnail.jpg"
    if not image.mode == 'RGB':
        image = image.convert('RGB')
    while True:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(fname, quality=quality, optimize=True)
        quality = quality - 1
        print(f"QUALITY: {quality}%, FILESIZE: {os.stat(fname).st_size}")
        if os.stat(fname).st_size < desired_volume:
            print(f"Все прошло успешно! Сжатый файл находится в папке со скриптом, название {fname}")
            break
        elif quality == 1:
            print("Сжать файл еще сильнее невозможно!")
            break


im = Image.open(input("Здравствуйте! Данный скрипт может сжимать картинки, "
                      "для этого картинка должна находиться в одной папке со скриптом и иметь формат .jpg или .png.\n"
                      "Введите название файла в формате photo.jpg\n"))
lim = int(input("Введите лимит байтов на сжатие\n"))
resolution = input("Введите 2 числа через пробел, разрешение по вертикали и диагонали, "
                   "либо не вводите ничего чтобы сжатие произошло к 256х256."
                   "Введите '1' чтобы оставить разрешение без изменений\n")
if resolution == '1':
    compress_image(im, lim, im.size)
elif resolution.strip() == '':
    compress_image(im, lim)
else:
    compress_image(im, lim, (int(resolution.split()[0]), int(resolution.split()[1])))



