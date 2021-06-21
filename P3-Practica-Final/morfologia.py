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

    def Abrir(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
        self.mostrarImagen("Opening", img, imgRes, "Op", ruta)

    def Cerrar(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
        self.mostrarImagen("Closing", img, imgRes, "Cl", ruta)

    def MorfGradiente(self, ruta, n):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        kernel = np.ones((n, n), np.uint8)
        imgRes = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
        self.mostrarImagen("Gradiente Morfológico", img, imgRes, "MorfG", ruta)

    def xor(self, ruta, ruta2):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread("./img/" + ruta2, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_xor(img,img2)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)

    def oor(self, ruta, ruta2):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread("./img/" + ruta2, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_or(img,img2)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)

    def aand(self, ruta, ruta2):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread("./img/" + ruta2, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_and(img,img2)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)

    def nott(self, ruta, ruta2):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread("./img/" + ruta2, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_nott(img,img2)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)