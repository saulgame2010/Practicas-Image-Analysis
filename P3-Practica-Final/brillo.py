import cv2
import numpy as np
from matplotlib import pyplot as plt
from mates import Mates

class Brillo:
    def ecualizacion(self, ruta):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        img = cv2.equalizeHist(img)

        cv2.imshow('Histogramas', img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )

        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.imwrite("./imgRes/ecualizada_"+ruta, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def expansion(self, ruta, nuevoMin, nuevoMax):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape #(ancho, alto)
        print(tamanioImg)
        pixeles = [] #lista
        for x in range(tamanioImg[0]): #(min, max)
            for y in range(tamanioImg[1]):                
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg = np.unique(npPixeles) #arreglo
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
        cv2.imwrite("./imgRes/expansion_"+ruta, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def contraccion(self, ruta, nuevoMin, nuevoMax):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        pixeles = []
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):                
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg = np.unique(npPixeles)#arreglo
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
        cv2.imwrite("./imgRes/contraccion_"+ruta, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def desplazamiento(self, ruta, des):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
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
        cv2.imwrite("./imgRes/desplazamiento_"+ruta, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def ecExp(self, ruta, alfa):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        tamanioImg = img.shape
        totalElementos = img.size
        pixeles = []
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                pixeles.append(img.item(x, y))
        npPixeles = np.array(pixeles)
        infoImg, indices, frecuencias = np.unique(npPixeles,return_inverse=True, return_counts=True) #Tupla (arreglo, num apariciones)        
        probabilidad = []        
        min = np.amin(infoImg)         
        for i in range(0, len(infoImg)):
            probabilidad.append(frecuencias[i]/totalElementos)        
        ecu = Mates()        
        pG = []        
        for i in range(0, len(probabilidad) - 1):
            if(i == 0):
                pG.append(probabilidad[i])
            else: 
                pG.append(probabilidad[i] + pG[i-1])                
        cont = 0
        for i in range(0, len(probabilidad)-1):
            infoImg[i] = ecu.ecualizacionExp(min, alfa, pG[i], npPixeles[i])        
        
        cont = 0        
        for x in range(tamanioImg[0]):
            for y in range(tamanioImg[1]):
                img.itemset((x, y), infoImg[indices[cont]])                
                cont = cont + 1
        cv2.imshow("Histograma", img)
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color='gray' )
        plt.xlabel('intensidad de iluminacion')
        plt.ylabel('cantidad de pixeles')
        plt.show()
        cv2.imwrite("./imgRes/ecExp_"+ruta, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()