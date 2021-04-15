import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import simpledialog
import sys
import os
from histogram import Histograma

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
        histograma.ecualizacion(filename[1])

def expandirHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        intervaloMin = simpledialog.askinteger(title="Nuevo intervalo mínimo", prompt="Cuál será el nuevo intervalo mínimo para el histograma?:")
        intervaloMax = simpledialog.askinteger(title="Nuevo intervalo máximo", prompt="Cuál será el nuevo intervalo máximo para el histograma?:")
        histograma.expansion(filename[1], intervaloMin, intervaloMax)

def contraerHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        intervaloMin = simpledialog.askinteger(title="Nuevo intervalo mínimo", prompt="Cuál será el nuevo intervalo mínimo para el histograma?:")
        intervaloMax = simpledialog.askinteger(title="Nuevo intervalo máximo", prompt="Cuál será el nuevo intervalo máximo para el histograma?:")
        histograma.contraccion(filename[1], intervaloMin, intervaloMax)

def desplazarHist(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        des = simpledialog.askinteger(title="Desplazar histograma", prompt="Cuál será el desplazamiento del histograma?:")
        histograma.desplazamiento(filename[1], des)
    
def exponencial(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        alfa = simpledialog.askinteger(title="Define el alfa", prompt="Cuál será el valor alfa?:")
        histograma.ecExp(filename[1], alfa)
    

#Creamos la ventana
window = tk.Tk()
window.title("Ajuste de brillo")
#Vamos a crear el contenedor de los elementos
frame = tk.Frame(master = window, width = 900, height = 460, bg = "black")
#Aquí empezamos a crear los elementos, empezamos por el título, que es un Label
tituloLb = tk.Label(text="Práctica #1 'Ajuste de brillo'", foreground="crimson", background="black", width="35", height="5", font=("Courier", 16))
tituloLb.place(x=220, y=0)
#Creamos un boton para el histograma a color y para el histograma de escala de grises
histcolorBt = tk.Button(text="HISTOGRAMA RGB", width=30, height=1, font=("Courier", 16), anchor="center", foreground="lime", background="black")
histcolorBt.bind("<Button-1>", histogramColor)
histcolorBt.place(x=40, y = 200)
histgrisBt = tk.Button(text="HISTOGRAMA GRISES", width=30, height=1, font=("Courier", 16), anchor="center", foreground="pink", background="black")
histgrisBt.bind("<Button-1>", histogramGris)
histgrisBt.place(x=40, y = 250)
#Creamos un botón para cargar una imagen
cargarImgBt = tk.Button(text="CARGAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="blue", background="black")
cargarImgBt.bind("<Button-1>", cargarImg)
cargarImgBt.place(x=40, y = 100)
#Creamos un label para saber el status del archivo
filestatus = tk.Label(text="No se ha seleccionado archivo...", foreground="white", background="black", width=50, height=1, font=("Courier", 10), anchor="center")
filestatus.place(x=40, y=150)
#Creamos un botón para ecualizar la imagen
cargarImgBt = tk.Button(text="ECUALIZAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="red", background="black")
cargarImgBt.bind("<Button-1>", ecualizarImg)
cargarImgBt.place(x=40, y = 300)
#Boton para expandir histograma
expandirBtn = tk.Button(text="EXPANDIR HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="yellow", background="black")
expandirBtn.bind("<Button-1>", expandirHist)
expandirBtn.place(x=40, y = 350)
#Boton para contraer histograma
contraerBtn = tk.Button(text="CONTRAER HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="orange", background="black")
contraerBtn.bind("<Button-1>", contraerHist)
contraerBtn.place(x=450, y = 100)
#Boton para desplazar el histograma
contraerBtn = tk.Button(text="DESPLAZAR HISTOGRAMA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="purple", background="black")
contraerBtn.bind("<Button-1>", desplazarHist)
contraerBtn.place(x=450, y = 150)
#Boton para ecualización exponencial
contraerBtn = tk.Button(text="ECUALIZACIÓN EXPONENCIAL", width=30, height=1, font=("Courier", 16), anchor="center", foreground="magenta", background="black")
contraerBtn.bind("<Button-1>", exponencial)
contraerBtn.place(x=450, y = 200)

frame.pack()
file = None
ruta = None
filename = None
try:
    histograma = Histograma()
    window.mainloop()
except KeyboardInterrupt:
    sys.exit()