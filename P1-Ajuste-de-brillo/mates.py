import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class Mates:
    def ecRecta(self, x1, x2, y1, y2, intensidadPixel):
        #Recordemos que una recta es y = mx + b
        m = (y2-y1)/(x2-x1)
        b0 = y2 - (m * x2)
        b1 = y1 - (m * x1)
        if b0 == b1:
            b = b1
        else:
            print("Esta mal jaja")
        return m * intensidadPixel + b