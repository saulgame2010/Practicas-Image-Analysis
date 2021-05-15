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
        filtro.Maximo(filename[1])

def minimo(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        filtro.Minimo(filename[1])

def kir(event):
    if(ruta == None):
        messagebox.showerror("Error", "Selecciona una imagen primero")
    else:
        k = simpledialog.askinteger(title="K", prompt="Cual kernel quieres utilizar?")
        filtro.Kirsch(filename[1], k)

window = tk.Tk()
window.title("Segmentación Parcial")
#Vamos a crear el contenedor de los elementos
frame = tk.Frame(master = window, width = 900, height = 460, bg = "black")
#Aquí empezamos a crear los elementos, empezamos por el título, que es un Label
tituloLb = tk.Label(text="Práctica #2 'Segmentación parcial'", foreground="crimson", background="black", width="35", height="5", font=("Courier", 16))
tituloLb.place(x=220, y=0)
#Creamos un botón para cargar una imagen
cargarImgBt = tk.Button(text="CARGAR IMAGEN", width=30, height=1, font=("Courier", 16), anchor="center", foreground="blue", background="black")
cargarImgBt.bind("<Button-1>", cargarImg)
cargarImgBt.place(x=40, y = 100)
#Creamos un label para saber el status del archivo
filestatus = tk.Label(text="No se ha seleccionado archivo...", foreground="white", background="black", width=50, height=1, font=("Courier", 10), anchor="center")
filestatus.place(x=40, y=150)
promediadorBt = tk.Button(text="FILTRO PROMEDIADOR", width=30, height=1, font=("Courier", 16), anchor="center", foreground="lime", background="black")
promediadorBt.bind("<Button-1>", promediador)
promediadorBt.place(x=40, y = 200)
mediaBt = tk.Button(text="FILTRO MEDIA", width=30, height=1, font=("Courier", 16), anchor="center", foreground="pink", background="black")
mediaBt.bind("<Button-1>", media)
mediaBt.place(x=40, y = 250)
maxBt = tk.Button(text="FILTRO MAXIMO", width=30, height=1, font=("Courier", 16), anchor="center", foreground="yellow", background="black")
maxBt.bind("<Button-1>", maximo)
maxBt.place(x=40, y = 300)
minBt = tk.Button(text="FILTRO MINIMO", width=30, height=1, font=("Courier", 16), anchor="center", foreground="yellow", background="black")
minBt.bind("<Button-1>", minimo)
minBt.place(x=40, y = 350)
mascaraKirschBt = tk.Button(text="MÁSCARA DE KIRSCH", width=30, height=1, font=("Courier", 16), anchor="center", foreground="orange", background="black")
mascaraKirschBt.bind("<Button-1>", kir)
mascaraKirschBt.place(x=450, y = 100)
frame.pack()
file = None
ruta = None
filename = None
try:
    filtro = Filtros()
    window.mainloop()
except KeyboardInterrupt:
    sys.exit()