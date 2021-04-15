import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from mates import Mates

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
    
    def ecualizacion(self, ruta):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        img = cv2.equalizeHist(img)

        cv2.imshow('Histogramas', img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.waitKey()

    def expansion(self, ruta, nuevoMin, nuevoMax):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        print(tamanioImg)
        pixeles = []
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):                
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg = np.unique(npPixeles)
        max = np.amax(infoImg)
        min = np.amin(infoImg)
        recta = Mates()
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                img.itemset((x, y), recta.ecRecta(min, max, nuevoMin, nuevoMax, img.item(x, y)))
        cv2.imshow("Histograma", img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.destroyAllWindows()
    
    def contraccion(self, ruta, nuevoMin, nuevoMax):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        pixeles = []
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):                
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg = np.unique(npPixeles)
        max = np.amax(infoImg)
        min = np.amin(infoImg)
        contraccion = Mates()
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                img.itemset((x, y), contraccion.contraer(nuevoMax, nuevoMin, max, min, img.item(x, y)))
        cv2.imshow("Histograma", img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.destroyAllWindows()

    def desplazamiento(self, ruta, des):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        desplazamiento = Mates()
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                img.itemset((x, y), desplazamiento.desplazar(des, img.item(x, y)))
        cv2.imshow("Histograma", img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.destroyAllWindows()

    def ecExp(self, ruta, alfa):
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        totalElementos = img.size
        pixeles = []
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg = np.unique(npPixeles, return_counts=True)        
        frecuencias = np.array(infoImg[1])        
        probabilidad = []        
        min = np.amin(infoImg[0])        
        for i in range(0, len(infoImg[0])):
            probabilidad.append(frecuencias[i]/totalElementos)        
        ecu = Mates()
        """for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                img.itemset((x, y), ecu.ecualizacionExp(min, alfa, sumatoria, img.item(x, y)))
        cv2.imshow("Histograma", img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.destroyAllWindows()"""