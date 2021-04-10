import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
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

#Creamos la ventana
window = tk.Tk()
window.title("Ajuste de brillo")
#Vamos a crear el contenedor de los elementos
frame = tk.Frame(master = window, width = 700, height = 460, bg = "black")
#Aquí empezamos a crear los elementos, empezamos por el título, que es un Label
tituloLb = tk.Label(text="Práctica #1 'Ajuste de brillo'", foreground="crimson", background="black", width="35", height="5", font=("Courier", 16))
tituloLb.place(x=115, y=0)
#Creamos un boton para el histograma a color y para el histograma de escala de grises
histcolorBt = tk.Button(text="HISTOGRAMA RGB", width=30, height=1, font=("Courier", 16), anchor="center", foreground="lime", background="black")
histcolorBt.bind("<Button-1>", histogramColor)
histcolorBt.place(x=145, y = 100)
histgrisBt = tk.Button(text="HISTOGRAMA GRISES", width=30, height=1, font=("Courier", 16), anchor="center", foreground="pink", background="black")
histgrisBt.bind("<Button-1>", histogramGris)
histgrisBt.place(x=145, y = 150)
#Creamos un botón para cargar una imagen
cargarImgBt = tk.Button(text="CARGAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="blue", background="black")
cargarImgBt.bind("<Button-1>", cargarImg)
cargarImgBt.place(x=145, y = 200)
#Creamos un label para saber el status del archivo
filestatus = tk.Label(text="No se ha seleccionado archivo...", foreground="white", background="black", width=50, height=1, font=("Courier", 10), anchor="center")
filestatus.place(x=145, y=250)

frame.pack()
file = None
ruta = None
filename = None
try:
    histograma = Histograma()
    window.mainloop()
except KeyboardInterrupt:
    sys.exit()