import tkinter
Ventana = tkinter.Tk()
Ventana.geometry("450x200")
Ventana.title('¡Mundo Burguer!')
Ventana.config(bg = 'green')

etiqueta1 = tkinter.Label(Ventana, text = 'Sabrosas y deliciosas Hamburguesas', font = 'Times 15')
etiqueta1.pack()

def Boton():
  print('Su orden se iniciara a Tomar')

Boton1 = tkinter.Button(Ventana, text = 'Ordenar', command = Boton)
Boton1.pack() 
Ventana.mainloop()