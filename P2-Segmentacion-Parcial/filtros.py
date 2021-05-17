import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import time
from PIL import Image, ImageFilter

class Filtros:
    def filtroPromediador(self, ruta, n):
        img = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        elementos = n * n;        
        #Crea el kernel
        kernel = np.ones((n,n),np.float32)/elementos
        #Filtra la imagen utilizando el kernel anterior
        dst = cv2.filter2D(img,-1,kernel)
        cv2.imshow("Promediada", dst)
        cv2.imwrite("./imgRes/promediador_" + ruta, dst)

    def filtroMedia(self, ruta, n):
        
        image = cv2.imread("./img/" + ruta, cv2.IMREAD_GRAYSCALE)
        
        dst = cv2.medianBlur(image, n)
        
        cv2.imshow("Media aritmética", dst)
        
        cv2.imwrite("./imgRes/media_" + ruta, dst)
        
        cv2.waitKey(0)

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
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir1_" + ruta, dst)
        elif k == 2:
            dst = cv2.filter2D(image,-1,npK2)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir2_" + ruta, dst)
        elif k == 3:
            dst = cv2.filter2D(image,-1,npK3)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir3_" + ruta, dst)
        elif k == 4:
            dst = cv2.filter2D(image,-1,npK4)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir4_" + ruta, dst)
        elif k == 5:
            dst = cv2.filter2D(image,-1,npK5)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir5_" + ruta, dst)
        elif k == 6:
            dst = cv2.filter2D(image,-1,npK6)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir6_" + ruta, dst)
        elif k == 7:
            dst = cv2.filter2D(image,-1,npK7)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir7_" + ruta, dst)
        elif k == 8:
            dst = cv2.filter2D(image,-1,npK8)
            cv2.imshow("Promediada", dst)
            cv2.imwrite("./imgRes/kir8_" + ruta, dst)