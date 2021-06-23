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

    def nott(self, ruta):
        img = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        XOR = cv.bitwise_not(img)
        self.mostrarImagen("Xor", img, XOR, "xor", ruta)

    def Identificador(self, ruta, ruta2):

        # Leer las imágenes que vamos a comparar
        # Imagen sobre la que vamos a detectar si existe otra imagen
        img = cv.imread("./img/" + ruta)
        img1 = cv.imread("./img/" + ruta)
        # Imagen que comprobamos si existe en la imagen Todo
        img2 = cv.imread("./img/" + ruta2)

        # Tamaño de la imagen 1.jpg
        w, h = img2.shape[:-1]

        # Función que sirve para detectar si una imagen está contenida en otra
        res = cv.matchTemplate(img1, img2, cv.TM_CCOEFF_NORMED)

        # Umbral admitido
        threshold = .75

        # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # Cambiar columnas y filas
            cv.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

        self.mostrarImagen("Identificador", img, img1, "Identificador", ruta)

        """img = cv.imread("./img/"+ruta)
        img1 = cv.imread("./img/" + ruta, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread("./img/"+ruta2, cv.IMREAD_GRAYSCALE)
        img1 = np.array(img1, dtype="uint8")
        img2 = np.array(img2, dtype="int")
        if ruta2 == "gatoblanco.jpg":
            tamanioImg2 = img2.shape #(ancho, alto)
            for x in range(tamanioImg2[0]): #(min, max)
                for y in range(tamanioImg2[1]):
                    if img2.item(x, y) == 0:
                        img2.itemset((x, y), -1)
                    if img2.item(x, y) == 255:
                        img2.itemset((x, y), 1)
        else:
            tamanioImg2 = img2.shape #(ancho, alto)
            for x in range(tamanioImg2[0]): #(min, max)
                for y in range(tamanioImg2[1]):
                    if img2.item(x, y) == 0:
                        img2.itemset((x, y), 1)
                    if img2.item(x, y) == 255:
                        img2.itemset((x, y), -1)
        output_image = cv.morphologyEx(img1, cv.MORPH_HITMISS, img2)
        self.mostrarImagen("Hit", img1, output_image, "hitme", ruta)
        tamanio = img.shape
        for x in range(tamanio[0]):
            for y in range (tamanio[1]):
                if output_image[x,y]==255:
                    cv.rectangle(img,(x,y),(x+20,y+30),(0,255,0),2)
        ##self.mostrarImagen("Hit", img1, img, "hitme", ruta)"""


        

    """def marcarhallazgos(self,img,img2,ret, ruta):
        for i in range(len(img)-len(img2)+1):
            for j in range(len(img[0])-len(img2[0])+1):
                if (img2==img[i:i+len(img2),j:j+len(img2[0])]).all():
                    ret[(i+1),j:(j+len(img2[0]))] = [0,255,255]
                    ret[i+len(img2),j:j+len(img2[0])] = [0,255,255]
                    ret[i+1:i+len(img2),j+len(img2[0])] = [0,255,255]
                    ret[i+1:i+len(img2),j] = [0,255,255]
        self.mostrarImagen("Hit", img, ret, "hitme", ruta)"""