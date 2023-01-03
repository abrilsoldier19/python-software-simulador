import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import tkinter as tk
from tkinter import ttk
 
ventana = tk.Tk()
ventana.geometry("900x790")
ventana.title("Tren de Poleas")
var=tk.StringVar()
variable1=tk.StringVar()
contenedor = ttk.Frame(ventana)
canvas = tk.Canvas(contenedor, height = 350,width =450)
ventana.configure(background='black')
scrollbar_v = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
scrollbar_h = ttk.Scrollbar(contenedor, orient="horizontal", command=canvas.xview)
contenedor_scroll= ttk.Frame(canvas)



#--------Mostrar cálculo a realizar--------------
formula=tk.Label(ventana,
	text="""Simulación del cálculo de la velocidad del último árbol de
un tren de poleas constituido por tres escalonamientos en mm
a partir de la ecuación de la relación de transmisión y regimen del funcionamiento del motor""",
	font=("Century Gothic", 11), bg='black', fg='pink')
formula.pack(padx=20, pady=10)


#--------Mostrar fórmula de la relación de transmisión múltiple---------
calculo_name=tk.Label(ventana, text="""  Fórmula de la relación de transmisión multiple
    i =(D1*D3*D5)/(D2*D4*D6)
    VelocidadN6=i*velocidadN1""",
	fg="#D684CF", bg='black',
	font=("Century Gothic",10, 'bold'))
calculo_name.pack(padx=5, pady=16)

#-----Imagen------
img=tk.PhotoImage(file="tren_poleas_31.png")
lbl_img=tk.Label(ventana, image=img)
lbl_img.pack(padx=5, pady=10)
 
contenedor_scroll.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    ))
 
canvas.create_window((0, 0), window=contenedor_scroll, anchor="nw")
 
canvas.configure(yscrollcommand=scrollbar_v.set, xscrollcommand = scrollbar_h.set)


#-----------Definición de funciones--------------
def operacion_3b_1(D1, D2, D3, D4, D5, D6):
    return var.set((D1*D3*D5)/(D2*D4*D6))

def operacion_3b_2(diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, velocidadN1):
    return variable1.set((diametro1*diametro3*diametro5)/(diametro2*diametro4*diametro6)*velocidadN1)

def ejecutar_operacion_3b():

 
    valor_diametro1 = int(D1.get())
    
    valor_diametro2 = int(D2.get())
    
    valor_diametro3 = int(D3.get())

    valor_diametro4 = int(D4.get())

    valor_diametro5 = int(D5.get())

    valor_diametro6 = int(D6.get())

    valor_velocidadN1 = int(velN1.get())


    resultado_3b_1 = operacion_3b_1(valor_diametro1, valor_diametro2, valor_diametro3, valor_diametro4, valor_diametro5, valor_diametro6)
    label_valor_result_3b_1.config(text = resultado_3b_1)

    resultado_3b_2 = operacion_3b_2(valor_diametro1, valor_diametro2, valor_diametro3, valor_diametro4, valor_diametro5, valor_diametro6, valor_velocidadN1)
    label_valor_result_3b_2.config(text = resultado_3b_2)
    
def salir():
	ventana.destroy()

for i in range(1,2):

    #--------Campo valor del diámetro de la polea motora D1------------
    D1=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea motora D1 en mm:""",  width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D1.pack(padx=5, pady=3, ipadx=25, ipady= 3)
    D1=tk.Entry(contenedor_scroll)
    D1.pack(padx=5, pady=3, ipadx=5, ipady=3)


    #--------Campo valor del diámetro de la polea conducida D2------------
    D2=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea conducida D2 en mm:""",  width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D2.pack(padx=5, pady=3, ipadx=25, ipady= 3)
    D2=tk.Entry(contenedor_scroll)
    D2.pack(padx=5, pady=2, ipadx=5, ipady=2)

 
    #--------Campo valor del diámetro de la polea motora D3------------
    D3=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea motora D3 en mm:""",  width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D3.pack(padx=5, pady=3, ipadx=25, ipady=3)
    D3=tk.Entry(contenedor_scroll)
    D3.pack(padx=5, pady=2, ipadx=5, ipady=2)


    #--------Campo valor del diámetro de la polea conducida D4 ------------
    D4=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea conducida D4 en mm:""",  width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D4.pack(padx=5, pady=3, ipadx=25, ipady=3)
    D4=tk.Entry(contenedor_scroll)
    D4.pack(padx=5, pady=2, ipadx=5, ipady=2)

    #--------Campo valor del diámetro de la polea motora D5------------
    D5=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea motora D5 en mm: """,  width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D5.pack(padx=5, pady=3, ipadx=25, ipady=3)
    D5=tk.Entry(contenedor_scroll)
    D5.pack(padx=5, pady=2, ipadx=5, ipady=2)

    #--------Campo valor del diámetro de la polea conducida D6 ------------
    D6=tk.Label(contenedor_scroll, text="""Ingrese el valor del diámetro de la polea conducida D6 en mm:""", width=40, fg="#B50386",
                font=("Comic Sans MS", 9))
    D6.pack(padx=5, pady=3, ipadx=25, ipady=3)
    D6=tk.Entry(contenedor_scroll)
    D6.pack(padx=5, pady=2, ipadx=5, ipady=2)

    #--------Campo valor de la velocidad del árbol motriz N1 en RPM ------------
    velN1=tk.Label(contenedor_scroll, text="""Ingrese el valor de la velocidad del árbol motriz N1 en RPM:""", width=40, fg="#B50386",
                 font=("Comic Sans MS", 8))
    velN1.pack(padx=5, pady=2, ipadx=25, ipady=2)
    velN1=tk.Entry(contenedor_scroll)
    velN1.pack(padx=5, pady=2, ipadx=5, ipady=2)



    #-------------Botón calcular--------------
    b1 = tk.Button(contenedor_scroll, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text='Calcular', command=ejecutar_operacion_3b)
    b1.config(bg="#B13BA7", fg="white")
    b1
    b1.pack(side=tk.TOP, padx=5, pady=15)
    
    
    #--------Resultado del cálculo------------
    label_result_3b_1=tk.Label(contenedor_scroll, font="Arial 9 bold", 
    text="""La relación de transmisión del mecanismo es i =""", 
	width=70)
    label_result_3b_1.pack(padx=1, pady=1, ipadx=1, ipady=1)
 
    label_valor_result_3b_1=tk.Label(contenedor_scroll, font="Arial 13 bold", bg="#D9D9D9", fg="#6600FF", textvariable=var, padx=5, pady=5, width=20)
    label_valor_result_3b_1.pack(side=tk.TOP, padx=3, pady=1)

    label_result_3b_2=tk.Label(contenedor_scroll, font="Arial 9 bold", 
	text=""" La velocidad del último árbol N6 es de = """,
	width=70)
    label_result_3b_2.pack(padx=1, pady=2, ipadx=1, ipady=2)
    label_valor_result_3b_2=tk.Label(contenedor_scroll, font="Arial 13 bold", bg="#D9D9D9", fg="#6600FF", textvariable=variable1, padx=5, pady=5, width=20)
    label_valor_result_3b_2.pack(side=tk.TOP, padx=3, pady=1)


             #-------------Botón salir----------------
    b2 = tk.Button(ventana, font="Arial 13 bold", width=15, text='Salir', relief="flat", command=salir)
    b2.config(bg="#DCCFF3", fg="#7000B7")
    b2.place(x="420", y="730")


 
contenedor.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar_v.pack(side="right", fill="y")
scrollbar_h.pack(side="bottom", fill="x")
 
ventana.mainloop()

