from PIL import Image
import numpy as np


def MakeImageBWMosaic(mosaic=10, grayStep=50, inputImage="img2.jpg", output="res"):
    """
        название
       :param mosaic: Размер "Пикселя"
       :param grayStep: - больше, меньше градации
       :param inputImage: исходное имя файла
       :param output: имя итогого файла, без разрешения
       :return: Изображение в ЧБ и мозайкой
       :raise grayStep и mosaic не должны быть равны нулю
    """
    if mosaic == 0 or grayStep == 0:
        raise Exception("Mosaic or GrayStep can't be 0")

    def Init():
        image = np.array(Image.open(inputImage))
        x = len(image)
        y = len(image[1])
        return image, x, y



    def FindBright():
        # что-то я забыл, как избавиться от for и всё сделать через генератор
        answer = 0
        for pixelX in range(i, i + x):
            for pixelY in range(j, j + y):
                answer += sum(image[pixelX][pixelY])

        return answer // (x * y)

    def BuildImage():
        """
        редактирует файл изображения в прямоугольнике x/y:
        """
        # так же и тут, как-то не могу вспомнить, как сделать простой срез по range
        for pixelX in range(i, i + x):
            for pixelY in range(j, j + y):
                image[pixelX][pixelY][:] = bright // grayStep * grayStep / 3

    def ExportToFile():
        """
        сохраняет изображение
        """
        answer = Image.fromarray(image)
        answer.save(output + ".jpg")

    image, imageLenX, imageLenY = Init()
    bright = 0
    i = 0
    while i < imageLenX:
        j = 0
        x = imageLenX - i if i + mosaic > imageLenX else mosaic
        while j < imageLenY:
            y = imageLenY - j if j + mosaic > imageLenY else mosaic
            bright = FindBright()
            BuildImage()
            j = j + mosaic
        i = i + mosaic

    ExportToFile()


MakeImageBWMosaic(0, 50)

