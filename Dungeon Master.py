from tkinter import *
ventana = Tk()
ventana.geometry("550x270")
ventana.title("Dungeon game")

position = "centre"
key = False
lock = True
wo = "Wrong option"
salida = False


def textoinicial():
    textomid = "  YOU ARE IN THE MIDDLE ROOM  "
    etiqueta["text"] = textomid

etiquetaup = Label(ventana, text = " ", font = "Consolas 24")
etiquetaup.grid(row = 0, column = 0, columnspan = 2)
etiqueta = Label(ventana, font = "Consolas 24")
etiqueta.grid(row = 1, column = 0, columnspan = 2)
etiquetadown = Label(ventana, text = " ", font = "Consolas 18")
etiquetadown.grid(row = 2, column = 0, columnspan = 2)

textoinicial()

def textolabelleft():
    global position
    global key
    if position == "centre" and key == False:
        texto = "  YOU ARE IN THE LEFT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - YOU FOUND A KEY!! - "
        position = "left"
    
    elif position == "centre" and key == True:
        texto = "  YOU ARE IN THE LEFT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - YOU ALREADY HAVE THE KEY!! - "
        position = "left"

    elif position == "left" and key == False:
        texto = "  YOU ARE IN THE LEFT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - KEY COLLECTED!!! -  "
        key = True
    elif position == "left" and key == True:
        texto = "  YOU ARE IN THE LEFT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - YOU ALREADY HAVE THE KEY!! -  "

  
    elif position == "right":
        texto = "  YOU ARE IN THE MIDDLE ROOM  "
        etiqueta["text"] = texto
        position = "centre"


def textolabelright():
    global position
    global lock
    global key
    if position == "centre" and lock == True:
        texto = "  YOU ARE IN THE RIGHT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - YOU FOUND A DOOR!! - "
        position = "right"

    elif position == "centre" and lock == False:
        texto = "  YOU ARE IN THE RIGHT ROOM  "
        etiqueta["text"] = texto
        etiquetadown["text"] = "  - DOOR IS OPEN!!! - "
        position = "right"

    elif position == "right" and key == False:
        texto = "  - DOOR IS LOCKED!!! -  "
        etiquetadown["text"] = texto
    
    elif position == "right" and key == True:
        texto = "  - DOOR IS OPEN NOW!!! -  "
        etiquetadown["text"] = texto
        lock = False
  
    elif position == "left":
        texto = "  YOU ARE IN THE MIDDLE ROOM  "
        etiqueta["text"] = texto
        position = "centre"



def textoinicial1():
    
    boton1["text"] = "Go left"

def textoinicial2():
    boton2["text"] = "Go right"






boton1 = Button(ventana, font = "Consolas 18", width = 12, height = 3, command = lambda: [textolabelleft(), boton1text(), textoinicial2(), saldeahi()])
boton1.grid(row = 3, column = 0)
boton2 = Button(ventana, font = "Consolas 18", width = 12, height = 3, command = lambda: [textolabelright(), boton2text(), textoinicial1(), vete()])
boton2.grid(row = 3, column = 1)

textoinicial1()
textoinicial2()

def saldeahi():
    global salida
    salida = False

# Quit
def vete():
    global salida
    global lock
    global position
    if position == "centre" or position == "left":
        salida = False
    elif salida == False and lock == False:
        salida = True
    elif salida == True:
        exit()


# boton izquierda
def boton1text():
    global position
    global key
    if position == "left" and key == False:
        boton1["text"] = "Pick up key"

    elif position == "left" and key == True:
        boton1["text"] = "[   🗝️]"

    else:
        boton1["text"] = "Go left"
        etiquetadown["text"] = " "

# boton derecha
def boton2text():
    global position
    global key
    global lock
    if position == "right" and lock == True:
        boton2txt0 = "Open door"
        boton2["text"] = boton2txt0
    
    elif position == "right" and lock == False:
        boton2txt0 = "Go exit"
        boton2["text"] = boton2txt0

    else:
        boton2txt0 = "Go right"
        boton2["text"] = boton2txt0
        etiquetadown["text"] = " "





  



ventana.mainloop()

