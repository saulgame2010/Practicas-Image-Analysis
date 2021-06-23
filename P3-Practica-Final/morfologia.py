import cv2 as cv
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

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

    def nott(self, ruta):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_not(img)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)

    def hitmmiss(self, ruta, ruta2):
        img = cv.imread("./img/"+ruta)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img2 = cv.imread("./img/"+ruta2, cv.IMREAD_GRAYSCALE)
        gray = np.array(gray, dtype="uint8")
        img2 = np.array(img2, dtype="int")
        if ruta2 == "gatoblanco.jpg":
            tamanioImg = img2.shape #(ancho, alto)
            for x in range(tamanioImg[0]): #(min, max)
                for y in range(tamanioImg[1]):                
                    if img2.item(x, y) == 0:
                        img2.itemset((x, y), -1)
                    if img2.item(x, y) == 255:
                        img2.itemset((x, y), 1)
        else:
            tamanioImg = img2.shape #(ancho, alto)
            for x in range(tamanioImg[0]): #(min, max)
                for y in range(tamanioImg[1]):                
                    if img2.item(x, y) == 0:
                        img2.itemset((x, y), 1)
                    if img2.item(x, y) == 255:
                        img2.itemset((x, y), -1)
        output_image = cv.morphologyEx(gray, cv.MORPH_HITMISS, img2)
        #img2 = np.zeros((len(img2), len(img2[0])))
        #img2[int(len(img2)/2), int(len(img2[0])/2)] = 255
        self.mostrarImagen("Hit", img, output_image, "hitme", ruta)
        #self.marcarhallazgos(output_image, img2, img, ruta)
        

    """def marcarhallazgos(self,img,img2,ret, ruta):
        for i in range(len(img)-len(img2)+1):
            for j in range(len(img[0])-len(img2[0])+1):
                if (img2==img[i:i+len(img2),j:j+len(img2[0])]).all():
                    ret[(i+1),j:(j+len(img2[0]))] = [0,255,255]
                    ret[i+len(img2),j:j+len(img2[0])] = [0,255,255]
                    ret[i+1:i+len(img2),j+len(img2[0])] = [0,255,255]
                    ret[i+1:i+len(img2),j] = [0,255,255]
        self.mostrarImagen("Hit", img, ret, "hitme", ruta)"""