from tkinter import *

root = Tk()
root.title("MOD MENU FREE FIRE")
root.config(bg="white")
root.geometry("500x400")
root.resizable(0,0)


label1 = Label(root, text=" FREE FIRE MOD MENU V1", bg="white", fg="red", font=("arial 20"))
label1.pack()

imagen = PhotoImage(file="fre.png")
img = Label(root, image = imagen). pack(side=LEFT)

frame1 = Frame(root, bg="white")
frame1.pack(side=RIGHT)
l1 = Checkbutton(frame1, text="Headshot 100%", bg="red", fg="white", onvalue=1, offvalue=0)
l1.pack()
l2 = Checkbutton(frame1, text="Invisible", bg="red", fg="white", onvalue=1, offvalue=0)
l2.pack()
l3 = Checkbutton(frame1, text="Bullet 100%", bg="red", fg="white", onvalue=1, offvalue=0)
l3.pack()
l4 = Checkbutton(frame1, text="Vida Infinita", bg="red", fg="white", onvalue=1, offvalue=0)
l4.pack()
l5 = Checkbutton(frame1, text="Correr al 30%", bg="red", fg="white", onvalue=1, offvalue=0)
l5.pack()
l6 = Checkbutton(frame1, text="Correr al 50%", bg="red", fg="white", onvalue=1, offvalue=0)
l6.pack()
l7 = Checkbutton(frame1, text="Correr al 70%", bg="red", fg="white", onvalue=1, offvalue=0)
l7.pack()
l8 = Checkbutton(frame1, text="Correr al 100%", bg="red", fg="white", onvalue=1, offvalue=0)
l8.pack()

boton = Button(frame1, text="Guardar cambios", bg="red", fg="white", bd=10)
boton.pack()





root.mainloop()