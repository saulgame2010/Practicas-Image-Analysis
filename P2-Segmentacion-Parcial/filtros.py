import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import time
from PIL import Image
from random import randint, uniform,random

class Filtros:

    def mostrarImagen(self, titulo, imgOriginal, imgProcesada, proceso, ruta):
        cv2.imshow(titulo, np.hstack([imgOriginal, imgProcesada]))
        cv2.imwrite("./imgRes/" + proceso + "_" + ruta, imgProcesada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def filtroPromediador(self, ruta, n):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        elementos = n * n;        
        #Crea el kernel
        kernel = np.ones((n,n),np.float32)/elementos
        #Filtra la imagen utilizando el kernel anterior
        dst = cv2.filter2D(img,-1,kernel)
        self.mostrarImagen("Promediada", img, dst, "prom", ruta)        

    def filtroMedia(self, ruta, n):        
        image = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)        
        dst = cv2.medianBlur(image, n)
        self.mostrarImagen("Media aritmetica", image, dst, "medArt", ruta)        

    def ObtenerVecinos(self, copia, i, j):
        pixel_list = []
        try: 
            pixel_list.append(copia.getpixel((i-1, j-1)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i, j-1)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i+1, j-1)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i-1, j)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i, j)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i+1, j)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i-1, j+1)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i, j+1)))
        except: 
            pixel_list.append((0, 0, 0))
        try: 
            pixel_list.append(copia.getpixel((i+1, j+1)))
        except: 
            pixel_list.append((0, 0, 0))
        return pixel_list

    def Maximo(self, nombre):
        tiempo_de_inicio = time.time()
        img = Image.open("./img/" + nombre)
        img.show()        

        copia = Image.new('RGB', img.size)
        datosImg = Image.Image.getdata(img)
        copia.putdata(datosImg)
        ancho, alto = img.size

        for i in range(ancho):
            for j in range(alto):
                r, g, b = copia.getpixel((i,j))
                x = (r + g + b) / 3
                intx = int (x)
                pixel = tuple ([intx, intx, intx])
                copia.putpixel((i,j), pixel)

        for i in range(ancho):
            for j in range(alto):
                vecindades = self.ObtenerVecinos(img, i, j)
                maxi = max(((vecindades[0][0]), (vecindades[1][0]), (vecindades[2][0]), 
                            (vecindades[3][0]), (vecindades[4][0]), (vecindades[5][0]), 
                            (vecindades[6][0]), (vecindades[7][0]), (vecindades[8][0])))
                res = maxi
                pixel = tuple([res, res, res])
                copia.putpixel((i, j), pixel)

        copia.show()
        copia.save("./imgRes/max_" + nombre)        
        tiempo_de_terminacion = time.time()
        print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

    def Minimo(self, nombre):
        tiempo_de_inicio = time.time()
        img = Image.open("./img/" + nombre)
        img.show()        

        copia = Image.new('RGB', img.size)
        datosImg = Image.Image.getdata(img)
        copia.putdata(datosImg)
        ancho, alto = img.size

        for i in range(ancho):
            for j in range(alto):
                r, g, b = copia.getpixel((i,j))
                x = (r + g + b) / 3
                intx = int (x)
                pixel = tuple ([intx, intx, intx])
                copia.putpixel((i,j), pixel)

        for i in range(ancho):
            for j in range(alto):
                vecindades = self.ObtenerVecinos(img, i, j)
                mini = min(((vecindades[0][0]), (vecindades[1][0]), (vecindades[2][0]), 
                            (vecindades[3][0]), (vecindades[4][0]), (vecindades[5][0]), 
                            (vecindades[6][0]), (vecindades[7][0]), (vecindades[8][0])))
                res = mini
                pixel = tuple([res, res, res])
                copia.putpixel((i, j), pixel)

        copia.show()
        copia.save("./imgRes/min_" + nombre)        
        tiempo_de_terminacion = time.time()
        print ("Abrir la imagen tardo: ", tiempo_de_terminacion - tiempo_de_inicio, " segundos")

    def Kirsch(self, ruta, k):
        image = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        k1 = [ [-3, -3, 5], [-3, 0, 5], [-3, -3, -5] ]
        npK1 = np.asarray(k1)
        k2 = [ [-3, 5, 5], [-3, 0, 5], [-3, -3, -3] ]
        npK2 = np.asarray(k2)
        k3 = [ [5, 5, 5], [-5, 0, -3], [-3, -3, -3] ]
        npK3 = np.asarray(k3)
        k4 = [ [5, 5, -3], [5, 0, -3], [-3, -3, -3] ]
        npK4 = np.asarray(k4)
        k5 = [ [5, -3, -3], [5, 0, -3], [5, -3, -3] ]
        npK5 = np.asarray(k5)
        k6 = [ [-3, -3, -3], [5, 0, -3], [5, 5, -3] ]
        npK6 = np.asarray(k6)
        k7 = [ [-3, -3, -3], [-3, 0, -3], [5, 5, 5] ]
        npK7 = np.asarray(k7)
        k8 = [ [-3, -3, -3], [-3, 0, 5], [-3, 5, 5] ]
        npK8 = np.asarray(k8)
        if k == 1:
            dst = cv2.filter2D(image,-1,npK1)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir1", ruta)            
        elif k == 2:
            dst = cv2.filter2D(image,-1,npK2)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir2", ruta)
        elif k == 3:
            dst = cv2.filter2D(image,-1,npK3)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir3", ruta)
        elif k == 4:
            dst = cv2.filter2D(image,-1,npK4)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir4", ruta)
        elif k == 5:
            dst = cv2.filter2D(image,-1,npK5)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir5", ruta)
        elif k == 6:
            dst = cv2.filter2D(image,-1,npK6)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir6", ruta)
        elif k == 7:
            dst = cv2.filter2D(image,-1,npK7)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir7", ruta)
        elif k == 8:
            dst = cv2.filter2D(image,-1,npK8)
            self.mostrarImagen("Mascara de Kirsch", image, dst, "kir8", ruta)

    def binarizacion(self, ruta, umbral, tipoBin):
        image = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        if tipoBin == 1:
            ret, imgBin = cv2.threshold(image, umbral, 255, cv2.THRESH_BINARY)
            self.mostrarImagen("Imagen binarizada", image, imgBin, "bin", ruta)            
        elif tipoBin == 2:
            ret, imgBin = cv2.threshold(image, umbral, 255, cv2.THRESH_BINARY_INV)
            self.mostrarImagen("Imagen binarizada", image, imgBin, "binInv", ruta)


    def ruidoSalPim(self, ruta, porcentaje):
        image = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        imgOriginal = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        ancho, alto = image.shape
        sal = np.ceil(porcentaje * image.size * 0.5)
        for x in range(ancho):
            for y in range(alto):
                image.itemset((randint(0, x), randint(0, y)), sal)
        pimienta = np.ceil(porcentaje * image.size * (1. -0.5))
        for x in range(ancho):
            for y in range(alto):
                image.itemset((randint(0, x), randint(0, y)), pimienta)
        self.mostrarImagen("Imagen con ruido", imgOriginal, image, "sal-pim", ruta)