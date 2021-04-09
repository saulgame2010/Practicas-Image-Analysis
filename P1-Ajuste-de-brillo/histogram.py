import cv2
import numpy as np
from matplotlib import pyplot as plt

class Histograma:
    def histogramaColor(self, ruta):
        img = cv2.imread(ruta)
        cv2.imshow(ruta, img)

        color = ('b','g','r')

        for i, c in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(hist, color = c)
            plt.xlim([0,256])

        plt.show()

        cv2.destroyAllWindows()

    def histogramaGris(self, ruta):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        cv2.imshow(ruta, img)

        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()

        cv2.destroyAllWindows()