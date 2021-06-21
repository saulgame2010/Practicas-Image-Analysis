import cv2 as cv
import numpy as np

class Morfologia:
    def mostrarImagen(self, titulo, imgOriginal, imgProcesada, proceso, ruta):
        cv.imshow(titulo, np.hstack([imgOriginal, imgProcesada]))
        cv.imwrite("./img/" + proceso + "_" + ruta, imgProcesada)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def topHat(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
        self.mostrarImagen("Top hat", img, imgRes, "topH", ruta)

    def blackHat(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
        self.mostrarImagen("Black hat", img, imgRes, "blackH", ruta)

    def Erosion(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.erode(img,kernel,iterations = 1)
        self.mostrarImagen("Erosion", img, imgRes, "Eros", ruta)

    def Dilatacion(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.dilate(img,kernel,iterations = 1)
        self.mostrarImagen("Dilatacion", img, imgRes, "Dilat", ruta)

        
    def Otsu(self, ruta):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
        self.mostrarImagen("Otsu", img, th2, "Otsu", ruta)