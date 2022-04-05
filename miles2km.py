from tkinter import *


def millas_a_km():
    millas = float(millas_input.get())
    km = millas * 1.609
    km_resultado.config(text=f"{km}")


ventana = Tk()
ventana.title("Millas a km.")
ventana.minsize(width=200, height=100)
ventana.config(padx=20, pady=20)

millas_input = Entry(width=10)
millas_input.grid(column=1, row=0)
# millas_input.get()

es_igual = Label(text="Es igual a: ", font=("arial", 12, "bold"))
es_igual.grid(column=0, row=1)

millas_text = Label(text="millas", font=("arial", 12, "bold"))
millas_text.grid(column=2, row=0)

km_resultado = Label(text="0", font=("arial", 12, "bold"))
km_resultado.grid(column=1, row=1)

km_text = Label(text="km", font=("arial", 12, "bold"))
km_text.grid(column=2, row=1)

boton = Button(text="Calcular", command=millas_a_km)
boton.grid(column=1, row=2)







ventana.mainloop()
