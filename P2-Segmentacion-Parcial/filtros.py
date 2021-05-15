import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class Filtros:
    def filtroPromediador(self, ruta):
        img = cv2.imread("./img/" + ruta)        
        #Crea el kernel
        kernel = np.ones((5,5),np.float32)/25
        #Filtra la imagen utilizando el kernel anterior
        dst = cv2.filter2D(img,-1,kernel)
        cv2.imshow('Promediada', dst)
        """plt.subplot(121),plt.imshow(img),plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(dst),plt.title('Promediada')
        plt.xticks([]), plt.yticks([])
        plt.show() """       