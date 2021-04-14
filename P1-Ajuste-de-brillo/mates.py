import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class Mates:
    def ecRecta(self, x1, x2, y1, y2, intensidadPixel):
        #Recordemos que una recta es y = mx + b
        m = (y2-y1)/(x2-x1)
        b = y1 - (m * x1)
        
        return m * intensidadPixel + b
    
    def contraer(self, cmax, cmin, rmax, rmin, rk):
        return ((cmax - cmin)/ (rmax - rmin)) * (rk - rmin) + cmin