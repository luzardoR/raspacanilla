import generador_de_password as gp 
from tkinter import *
import random
import pyperclip

root = Tk()
root.title("Generador de Contraseñas");

texto= Label(root, text="click abajo para generar su contraseña.")
texto.grid(row=0)


def crear():
  eleccion = random.randint(1,3)
  if eleccion == 1:
    a = gp.formato1()
    clave_valor1 = a
  else:
    if eleccion == 2:
      a = gp.formato2()
      clave_valor1 = a
    else:
      if eleccion == 3:
        a = gp.formato3()
        clave_valor1 = a
  resultado= Label(root,text=clave_valor1).grid(row=2)
  def copi():
    pyperclip.copy(clave_valor1)

  copiar = Button(root, text="copiar",command=copi).grid(row=3)

  
boton = Button(root, text="generar",command=crear).grid(row=1)
  
root = mainloop()