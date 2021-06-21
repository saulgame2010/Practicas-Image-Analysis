from morfologia import Morfologia
from brillo import Brillo
from histogram import Histograma
from filtros import Filtros
import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import simpledialog
import sys
import os

def cargarImg(event):
    global file
    global filestatus
    global ruta
    global filename
    file = askopenfilename()
    filestatus["text"] = str(file)
    ruta = str(file)    
    filename = os.path.split(ruta)

def histogramColor(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        histograma.histogramaColor(filename[1])

def histogramGris(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        histograma.histogramaGris(filename[1])

def ecualizarImg(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        brillo.ecualizacion(filename[1])

def expandirHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        intervaloMin = simpledialog.askinteger(title="Nuevo intervalo mínimo", prompt="Cuál será el nuevo intervalo mínimo para el histograma?:")
        intervaloMax = simpledialog.askinteger(title="Nuevo intervalo máximo", prompt="Cuál será el nuevo intervalo máximo para el histograma?:")
        brillo.expansion(filename[1], intervaloMin, intervaloMax)

def contraerHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        intervaloMin = simpledialog.askinteger(title="Nuevo intervalo mínimo", prompt="Cuál será el nuevo intervalo mínimo para el histograma?:")
        intervaloMax = simpledialog.askinteger(title="Nuevo intervalo máximo", prompt="Cuál será el nuevo intervalo máximo para el histograma?:")
        brillo.contraccion(filename[1], intervaloMin, intervaloMax)

def desplazarHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        des = simpledialog.askinteger(title="Desplazar histograma", prompt="Cuál será el desplazamiento del histograma?:")
        brillo.desplazamiento(filename[1], des)
    
def exponencial(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        alfa = simpledialog.askfloat(title="Define el alfa", prompt="Cuál será el valor alfa?:")
        brillo.ecExp(filename[1], alfa)

def promediador(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Tamaño de la matriz", prompt="¿De qué tamaño será la matriz?")
        filtro.filtroPromediador(filename[1], n)

def media(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Tamaño de la matriz", prompt="¿De qué tamaño será la matriz?")
        filtro.filtroMedia(filename[1], n)

def maximo(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="K", prompt="Cual es el tamaño de la matriz a usar?")
        filtro.maximumBoxFilter(n, filename[1])

def minimo(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="K", prompt="Cual es el tamaño de la matriz a usar?")
        filtro.minimumBoxFilter(n, filename[1])

def kir(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        k = simpledialog.askinteger(title="K", prompt="Cual kernel quieres utilizar?\nIngrese 9 si quiere aplicar todas las mascaras")
        filtro.Kirsch(filename[1], k)

def binarizar(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:        
        umbral = simpledialog.askinteger(title="Valor del umbral", prompt="Seleccione el valor del umbral")
        tipoBin = simpledialog.askinteger(title="Valor del umbral", prompt="Seleccione el tipo de binarizacion\n1.Normal\n2.Inversa")
        filtro.binarizacion(filename[1], umbral, tipoBin)

def salPim(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        porcentaje = simpledialog.askfloat(title="Valor del umbral", prompt="Seleccione el porcentaje de ruido")
        filtro.ruidoSalPim(filename[1], porcentaje)

def gauss(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        des = simpledialog.askfloat(title="Valor del umbral", prompt="Seleccione la desviacion estandar a utilizar")
        filtro.gaussiano(filename[1], des)

def Abrir(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Kernel", prompt="Establece el tamaño del kernel")
        morf.Abrir(filename[1], n)

def Cerrar(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Kernel", prompt="Establece el tamaño del kernel")
        morf.Cerrar(filename[1], n)

def MorfGrad(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Kernel", prompt="Establece el tamaño del kernel")
        morf.MorfGradiente(filename[1], n)

def topH(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Kernel", prompt="Establece el tamaño del kernel")
        morf.topHat(filename[1], n)

def blackH(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        n = simpledialog.askinteger(title="Kernel", prompt="Establece el tamaño del kernel")
        morf.blackHat(filename[1], n)

def metotsu(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        morf.Otsu(filename[1])

def Erosion(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        morf.Erosion(filename[1])

window = tk.Tk()
window.title("Práctica Final")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
#Vamos a crear el contenedor de los elementos
frame = tk.Frame(master = window, width = 1300, height = 580, bg = "black")
#Aquí empezamos a crear los elementos, empezamos por el título, que es un Label
tituloLb = tk.Label(text="Práctica Final", foreground="crimson", background="black", width="35", height="5", font=("Courier", 16))
tituloLb.place(x=420, y=0)
#Creamos un botón para cargar una imagen
cargarImgBt = tk.Button(text="CARGAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="red", background="black")
cargarImgBt.bind("<Button-1>", cargarImg)
cargarImgBt.place(x=40, y = 100)
#Creamos un label para saber el status del archivo
filestatus = tk.Label(text="No se ha seleccionado archivo...", foreground="white", background="black", width=50, height=1, font=("Courier", 10), anchor="center")
filestatus.place(x=40, y=150)
histcolorBt = tk.Button(text="HISTOGRAMA RGB", width=30, height=1, font=("Courier", 16), anchor="center", foreground="fuchsia", background="black")
histcolorBt.bind("<Button-1>", histogramColor)
histcolorBt.place(x=40, y = 200)
histgrisBt = tk.Button(text="HISTOGRAMA GRISES", width=30, height=1, font=("Courier", 16), anchor="center", foreground="lime", background="black")
histgrisBt.bind("<Button-1>", histogramGris)
histgrisBt.place(x=40, y = 250)
#Creamos un botón para ecualizar la imagen
ecImgBt = tk.Button(text="ECUALIZAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="yellow", background="black")
ecImgBt.bind("<Button-1>", ecualizarImg)
ecImgBt.place(x=40, y = 300)
#Boton para expandir histograma
expandirBtn = tk.Button(text="EXPANDIR HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="blue", background="black")
expandirBtn.bind("<Button-1>", expandirHist)
expandirBtn.place(x=40, y = 350)
#Boton para contraer histograma
contraerBtn = tk.Button(text="CONTRAER HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="orange", background="black")
contraerBtn.bind("<Button-1>", contraerHist)
contraerBtn.place(x=40, y = 400)
#Boton para desplazar el histograma
contraerBtn = tk.Button(text="DESPLAZAR HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="blueviolet", background="black")
contraerBtn.bind("<Button-1>", desplazarHist)
contraerBtn.place(x=40, y = 450)
#Boton para ecualización exponencial
expoBt = tk.Button(text="ECUALIZACIÓN EXPONENCIAL", width=30, height=1, font=("Courier", 16), anchor="center", foreground="orangered", background="black")
expoBt.bind("<Button-1>", exponencial)
expoBt.place(x=40, y = 500)
promediadorBt = tk.Button(text="FILTRO PROMEDIADOR", width=30, height=1, font=("Courier", 16), anchor="center", foreground="gold", background="black")
promediadorBt.bind("<Button-1>", promediador)
promediadorBt.place(x=450, y = 100)
mediaBt = tk.Button(text="FILTRO MEDIA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="pink", background="black")
mediaBt.bind("<Button-1>", media)
mediaBt.place(x=450, y = 150)
maxBt = tk.Button(text="FILTRO MÁXIMO", width=30, height=1, font=("Courier", 16), anchor="center", foreground="lightgreen", background="black")
maxBt.bind("<Button-1>", maximo)
maxBt.place(x=450, y = 200)
minBt = tk.Button(text="FILTRO MÍNIMO", width=30, height=1, font=("Courier", 16), anchor="center", foreground="coral", background="black")
minBt.bind("<Button-1>", minimo)
minBt.place(x=450, y = 250)
mascaraKirschBt = tk.Button(text="MÁSCARAS DE KIRSCH", width=30, height=1, font=("Courier", 16), anchor="center", foreground="slateblue", background="black")
mascaraKirschBt.bind("<Button-1>", kir)
mascaraKirschBt.place(x=450, y = 300)
binarizacionBt = tk.Button(text="BINARIZAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="tomato", background="black")
binarizacionBt.bind("<Button-1>", binarizar)
binarizacionBt.place(x=450, y = 350)
sal_pimBt = tk.Button(text="RUIDO SAL Y PIMIENTA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="brown", background="black")
sal_pimBt.bind("<Button-1>", salPim)
sal_pimBt.place(x=450, y = 400)
multiUmbBt = tk.Button(text="MULTIUMBRALIZACIÓN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="crimson", background="black")
multiUmbBt.bind("<Button-1>", )
multiUmbBt.place(x=450, y = 450)
otsuBt = tk.Button(text="UMBRALIZACIÓN DE OTSU", width=30, height=1, font=("Courier", 16), anchor="center", foreground="gray", background="black")
otsuBt.bind("<Button-1>",metotsu)
otsuBt.place(x=450, y = 500)
erosionBt = tk.Button(text="EROSIÓN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="darkslateblue", background="black")
erosionBt.bind("<Button-1>", Erosion)
erosionBt.place(x=860, y = 100)
dilatacionBt = tk.Button(text="DILATACIÓN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="darksalmon", background="black")
dilatacionBt.bind("<Button-1>", )
dilatacionBt.place(x=860, y = 150)
openingBt = tk.Button(text="OPENING", width=30, height=1, font=("Courier", 16), anchor="center", foreground="firebrick", background="black")
openingBt.bind("<Button-1>", )
openingBt.place(x=860, y = 200)
closingBt = tk.Button(text="CLOSING", width=30, height=1, font=("Courier", 16), anchor="center", foreground="white", background="black")
closingBt.bind("<Button-1>", )
closingBt.place(x=860, y = 250)
gradientBt = tk.Button(text="GRADIENTE", width=30, height=1, font=("Courier", 16), anchor="center", foreground="greenyellow", background="black")
gradientBt.bind("<Button-1>", )
gradientBt.place(x=860, y = 300)
top_hatBt = tk.Button(text="TOP HAT", width=30, height=1, font=("Courier", 16), anchor="center", foreground="goldenrod", background="black")
top_hatBt.bind("<Button-1>", topH)
top_hatBt.place(x=860, y = 350)
black_hatBt = tk.Button(text="BLACK HAT", width=30, height=1, font=("Courier", 16), anchor="center", foreground="khaki", background="black")
black_hatBt.bind("<Button-1>", blackH)
black_hatBt.place(x=860, y = 400)
frame.pack()
file = None
ruta = None
filename = None
try:
    filtro = Filtros()
    histograma = Histograma()
    brillo = Brillo()
    morf = Morfologia()
    window.mainloop()
except KeyboardInterrupt:
    sys.exit()