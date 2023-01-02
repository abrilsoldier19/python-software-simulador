import tkinter 
from tkinter import filedialog
import pyautogui
from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image,ImageTk
from re import A
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


 #Se define el ejercicio ia opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opciona():
    filewin = Toplevel(root)
    filewin.title("ia) Cálculo de la Relación de transmisión de velocidad")
    filewin.configure(background='black')
  
    formula=Label(filewin, 
	text="""Simulación del cálculo de relación de transmisión de velocidad
              del mecanismo de un una correa plana en m""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)

    label_ejerc_1= Label(filewin,font=("Century Gothic",11) ,text="""Fórmula de la relación de transmisión

        i = D1/D2

        donde:
        i = relación de transmisión
        D1 = diametro polea menor
        D2 = diametro polea mayor""", fg="black",bg="#85D5FE")
    label_ejerc_1.pack(padx=3, pady=20)

    label_num_D1= Label(filewin,font=("Calibri",11) ,text="Proporcione el valor del diámetro D1 de la polea menor en mm:",fg="black",bg="#D3D6FB")
    label_num_D1.pack()
    campo_num_D1=Entry(filewin)
    campo_num_D1.pack(pady=8)

    label_num_D2= Label(filewin,font=("Calibri",11) ,text="Proporcione el valor del diámetro D2 de la polea mayor en mm:",fg="black",bg="#D3D6FB")
    label_num_D2.pack()
    campo_num_D2=Entry(filewin)
    campo_num_D2.pack(pady=8)


    #Definición de formulas

    def operacion(D1, D2):
        return (D1/D2)

    def ejecutar_operacion():
        valor_num_D1 = int(campo_num_D1.get())
        valor_num_D2 = int(campo_num_D2.get())

        resultado = operacion(valor_num_D1, valor_num_D2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton1=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion)
    boton1.pack(side=TOP, padx=5, pady=15)
    boton1.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="""La relación de transmisión de velocidad es i """,bg="black", fg="white")
    label_result.pack()

    label_valor_result= Label(filewin,font="Arial 12 bold" ,text="",bg="#D9D9D9", fg="#6600FF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



 #Se define el ejercicio iia opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opciona():
    filewin = Toplevel(root)
    filewin.title("iia) Cálculo de velocidad que gira el eje conducido")
    filewin.configure(bg="black")
    formula=Label(filewin, 
	text="""Simulacion del calculo de la velocidad que gira el eje conducido
                de correa plana en rpm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)

    label_ejerc_12= Label(filewin,font=("Century Gothic",11) ,text="""Fórmula de las velocidades
    (D1) * (N1) = (D2)* (N2)
                
    se despeja N2 de la ecuacion anterior:

    N2 = (N1)*(D1)/(D2)
                
    D1 diametro polea menor
    N1 velocidad giro inicial
    D2 diametro polea mayor
    N2 velocidad giro conducido""",
                          fg="black",bg="#85D5FE")
    label_ejerc_12.pack()

    label_num_D1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D1 de la polea menor en mm:",
                               fg="black",bg="#D3D6FB")
    label_num_D1.pack()
    campo_num_D1=Entry(filewin)
    campo_num_D1.pack()

    label_num_N1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del eje inicial en rpm:",
                               fg="black",bg="#D3D6FB")
    label_num_N1.pack()
    campo_num_N1=Entry(filewin)
    campo_num_N1.pack()

    label_num_D2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D2 de la polea mayor en mm:",
                               fg="black",bg="#D3D6FB")
    label_num_D2.pack()
    campo_num_D2=Entry(filewin)
    campo_num_D2.pack()


    #Definición de formulas

    def operacion(D1, N1, D2):
        return (D1)*(N1)/(D2)

    def ejecutar_operacion():
        valor_num_D1 = int(campo_num_D1.get())
        valor_num_N1 = int(campo_num_N1.get())
        valor_num_D2 = int(campo_num_D2.get())

        resultado = operacion(valor_num_D1, valor_num_N1, valor_num_D2)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton1=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton1.pack(side=TOP, padx=5, pady=15)
    boton1.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="El resultado de la velocidad que gira el eje conducido es N2 =  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opciona():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciona)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()


#Se define el ejercicio iiia opcion a --------------------------------------------------------------------------------------------------------------------
def ejercicio_3_opciona():
    filewin = Toplevel(root)
    filewin.title("iiia) Cálculo de Longitud de correa")
    filewin.configure(bg="black")
  
    
    titulo=Label(filewin, 
	text="""Simulacion del calculo de la longitud de la correa que se necesita en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)


    formula= Label (filewin, font=("Century Gothic", 11), text = """Fórmula de la ecuacion de longitud
                L = π*(L1 + L2) + 2*(math.sqrt((L3)**2 + (L1 - L2)**2))""", fg="white", bg="#292929")
    formula.pack()

    variables_formula= Label (filewin, font=("Century Gothic", 11), text = """donde:
                L longitud de la correa 
                L1 semicircunferencia de la polea conducida 
                L2 semicircunferencia de la polea conductora 
                   L3  distancia  entre  los  ejes de las poleas""", fg="white", bg="#292929")
    variables_formula.pack()

    label_num_longitud1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la semicircunferencia de la polea conducida en mm:",fg="black",bg="#D3D6FB")
    label_num_longitud1.pack()
    campo_num_longitud1=Entry(filewin, font=("Courier New", 11))
    campo_num_longitud1.pack(pady=8)

    label_num_longitud2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la semicircunferencia de la polea conductora en mm:",fg="black",bg="#D3D6FB")
    label_num_longitud2.pack()
    campo_num_longitud2=Entry(filewin, font=("Courier New", 11))
    campo_num_longitud2.pack(pady=8)

    label_num_longitud3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la distancia entre los ejes de las poleas en mm:",fg="black",bg="#D3D6FB")
    label_num_longitud3.pack()
    campo_num_longitud3=Entry(filewin, font=("Courier New", 11))
    campo_num_longitud3.pack(pady=8)


    #Definición de formulas

    def operacion(L1, L2, L3):
        return math.pi*(L1 + L2) + 2*(math.sqrt((L3)**2 + (L1 - L2)**2))

    def ejecutar_operacion():
        valor_num_longitud1 = int(campo_num_longitud1.get())
        valor_num_longitud2 = int(campo_num_longitud2.get())
        valor_num_longitud3 = int(campo_num_longitud3.get())

        resultado = operacion(valor_num_longitud1, valor_num_longitud2, valor_num_longitud3)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton51=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton51.pack(side=TOP, padx=5, pady=15)
    boton51.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="El resultado de la longitud de la correa es L =  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion a)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('longitud_correa.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()


#Se define el ejercicio 1 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opcionb():
    filewin = Toplevel(root)
    filewin.title("iiia) Cálculo de Longitud de correa")
    filewin.configure(bg="black")
    titulo=Label(filewin, 
	text="""Simulación del cálculo de relación de transmisión del mecanismo de un
tren de poleas constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)

    formula=Label(filewin, text="""Fórmula de relación de transmisión
    i = (D1 * D3 * D5) / (D2 * D4 * D6)""", font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=3, pady=15)
    
    label_datos= Label(filewin,font=("Century Gothic",11) ,text="""i relación de transmisión,
    D1 diámetro de polea motora 1
    D2 diámetro polea conducida 2
    D3 diámetro de polea motora 3
    D4 diámetro polea conducida 4
    D5 diámetro de polea motora 5
    D6 diámetro polea conducida 6""",fg="white",bg="#292929")
    label_datos.pack(padx=3, pady=15)

    label_num_diametroD1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D1 de la polea motora 1 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD1.pack()
    campo_num_diametroD1=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD1.pack(padx=2, pady=10)

    label_num_diametroD2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D2 de la polea conducida 2 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD2.pack()
    campo_num_diametroD2=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD2.pack(padx=2, pady=10)

    label_num_diametroD3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D3 de la polea motora 3 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD3.pack()
    campo_num_diametroD3=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD3.pack(padx=2, pady=10)

    label_num_diametroD4= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D4 de la polea conducida 4 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD4.pack()
    campo_num_diametroD4=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD4.pack(padx=2, pady=10)

    label_num_diametroD5= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D5 de la polea motora 5 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD5.pack()
    campo_num_diametroD5=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD5.pack(padx=2, pady=10)

    label_num_diametroD6= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro D6 de la polea conducida 6 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD6.pack()
    campo_num_diametroD6=Entry(filewin, font=("Courier New", 11))
    campo_num_diametroD6.pack(padx=2, pady=10)


    #Definición de formulas
    def operacion(D1, D2, D3, D4, D5, D6):
        return ((D1)*(D3)*(D5))/((D2)*(D4)*(D6))

    def ejecutar_operacion():
        valor_num_diametroD1 = int(campo_num_diametroD1.get())
        valor_num_diametroD2 = int(campo_num_diametroD2.get())
        valor_num_diametroD3 = int(campo_num_diametroD3.get())
        valor_num_diametroD4 = int(campo_num_diametroD4.get())
        valor_num_diametroD5 = int(campo_num_diametroD5.get())
        valor_num_diametroD6 = int(campo_num_diametroD6.get())

        resultado = operacion(valor_num_diametroD1, valor_num_diametroD2, valor_num_diametroD3, valor_num_diametroD4, valor_num_diametroD5, valor_num_diametroD6)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton21=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton21.pack(side=TOP, padx=5, pady=15)
    boton21.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="La relación de transmisión del mecanismo es: ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 2 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opcionb():
    filewin = Toplevel(root)
    filewin.title("iiia) Cálculo de Longitud de correa")
    filewin.configure(bg="black")
    titulo=Label(filewin, 
	text="""Simulación del cálculo de la velocidad del eje de salida de un tren de poleas
constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Apartir de la Fórmula de de relación de transmisión
        N6 = (i * N1)  """,font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack( pady=5)
    
    label_ejerc_22= Label(filewin,text="""i representa a relación de transmisión
     N6 representa velocidad del eje de salida 6
     N1 representa velocidad de la rueda de motora 1 """, font=("Century Gothic", 11), fg="white", bg="#292929")
    label_ejerc_22.pack(padx=5, pady=20)

    label_transmisioni= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de i la relación de transmisión del mecanismo:",fg="black",bg="#D3D6FB")
    label_transmisioni.pack()
    campo_transmisioni=Entry(filewin, font=("Courier New", 11))
    campo_transmisioni.pack(padx=3, pady=10)

    label_velocidadN1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad N1 de la rueda motora 1 en RPM",fg="black",bg="#D3D6FB")
    label_velocidadN1.pack()
    campo_velocidadN1=Entry(filewin,font=("Courier New", 11))
    campo_velocidadN1.pack(padx=2, pady=10)


    #Definición de formulas

    def operacion(i, N1):
        return (i*N1)

    def ejecutar_operacion():
        valor_num_transmisioni = float(campo_transmisioni.get())
        valor_num_velocidadN1 = int(campo_velocidadN1.get())

        resultado = operacion(valor_num_transmisioni, valor_num_velocidadN1)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton2b=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton2b.pack(side=TOP, padx=5, pady=15)
    boton2b.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La velocidad N6 del eje de salida 6 es de:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio 3 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_3_opcionb():
    filewin = Toplevel(root)
    filewin.title("iiia) Cálculo de Longitud de correa")
    filewin.configure(bg="black")
    
    contenedor = Frame(filewin)
    canvas = Canvas(contenedor, height = 300, width=360)
    scrollbar_v = Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    scrollbar_h = Scrollbar(contenedor, orient="vertical", command=canvas.xview)
    contenedor_scroll= Frame(canvas)
    contenedor_scroll.configure(bg="black")
    
    titulo=Label(filewin, 
	text="""Simulación del cálculo de la velocidad del último árbol de un tren de poleas
constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Apartir de la Fórmula de de relación de transmisión y regimen del funcionamiento del motor
        i = (D1)*(D3)*(D5)/(D2)*(D4)*(D6)  """,font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack( pady=5)
    
    label_ejerc_22= Label(filewin,text="""D1 diámetro polea motora 1,
    D2 diámetro polea conducida 2
    D3 diámetro de polea motora 3
    D4 diámetro polea conducida 4
    D5 diámetro de polea motora 5
    D6 diámetro polea conducida 6
    N1 velocidad del árbol motor 1
    N6 velocidad del último árbol 6""", font=("Century Gothic", 11), fg="white", bg="#292929")
    label_ejerc_22.pack(padx=5, pady=20)

    contenedor_scroll.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    ))
 
    canvas.create_window((0, 0), window=contenedor_scroll, anchor="nw")
 
    canvas.configure(yscrollcommand=scrollbar_v.set, xscrollcommand = scrollbar_h.set)

    label_num_diametroD1= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea motora D1 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD1.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD1=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD1.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_diametroD2= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea conducida 2 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD2.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD2=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD2.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_diametroD3= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea motora 3 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD3.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD3=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD3.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_diametroD4= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea conducida 4 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD4.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD4=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD4.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_diametroD5= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea motora 5 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD5.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD5=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD5.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_diametroD6= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea conducida 6 en mm:",fg="black",bg="#D3D6FB")
    label_num_diametroD6.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_diametroD6=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_diametroD6.pack(padx=5, pady=3, ipadx=5, ipady=3)

    label_num_velocidadN1= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione la velocidad del árbol motriz N1 en RPM:",fg="black",bg="#D3D6FB")
    label_num_velocidadN1.pack(padx=5, pady=3, ipadx=5, ipady=3)
    campo_num_velocidadN1=Entry(contenedor_scroll, font=("Courier New", 11))
    campo_num_velocidadN1.pack(padx=5, pady=3, ipadx=5, ipady=3)


    #Definición de formulas
    def operacioni(D1, D2, D3, D4, D5, D6):
        return ((D1)*(D3)*(D5))/((D2)*(D4)*(D6))

    def operacionN6(D1, D2, D3, D4, D5, D6, N1):
        return ((D1)*(D3)*(D5))/((D2)*(D4)*(D6))*(N1)

    def ejecutar_operacion():
        valor_num_diametroD1 = int(campo_num_diametroD1.get())
        valor_num_diametroD2 = int(campo_num_diametroD2.get())
        valor_num_diametroD3 = int(campo_num_diametroD3.get())
        valor_num_diametroD4 = int(campo_num_diametroD4.get())
        valor_num_diametroD5 = int(campo_num_diametroD5.get())
        valor_num_diametroD6 = int(campo_num_diametroD6.get())
        valor_num_velocidadN1 = int(campo_num_velocidadN1.get())

        resultado_i = operacioni(valor_num_diametroD1, valor_num_diametroD2, valor_num_diametroD3, valor_num_diametroD4,
                              valor_num_diametroD5, valor_num_diametroD6)
        label_resultado_i.config(text = resultado_i)

        resultado_N6 = operacionN6(valor_num_diametroD1, valor_num_diametroD2, valor_num_diametroD3, valor_num_diametroD4,
                              valor_num_diametroD5, valor_num_diametroD6, valor_num_velocidadN1)
        label_resultado_N6.config(text = resultado_N6)

    #BOTON DE EJECUCION

    boton2b=Button(contenedor_scroll, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton2b.pack(side=TOP, padx=5, pady=15)
    boton2b.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados de i
    label_result_i= Label(contenedor_scroll,font=("Calibri",11) ,text="La relación de transmisión del mecanismo es  ",fg="white",bg="black")
    label_result_i.pack(padx=1, pady=1, ipadx=1, ipady=1)

    label_resultado_i= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_resultado_i.pack(side=TOP, padx=3, pady=1)

    # Resultados de velocidad N6
    label_result_N6= Label(contenedor_scroll,font=("Calibri",11) ,text="La velocidad del último árbol N6 es de =  ",fg="white",bg="black")
    label_result_N6.pack(padx=1, pady=2, ipadx=1, ipady=2)

    label_resultado_N6= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_resultado_N6.pack(side=TOP, padx=3, pady=1)

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

    contenedor.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_v.pack(side="right", fill="y")
    scrollbar_h.pack(side="bottom", fill="x")

#Se define el ejercicio 4 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_4_opcionb():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")
    
    titulo=Label(filewin, 
	text="""Simulación del cálculo de la relación de transmisión de velocidad total de un tren de
poleas constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Apartir de la Fórmula velocidad del árbol de entrada y velocidad del árbol de salida
        i = velocidadN6/velocidadN1  """,font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack( pady=5)
    
    label_ejerc_22= Label(filewin,text="""i representa a relación de transmisión
     N6 representa velocidad del árbol de salida 6
     N1 representa velocidad del árbol de entrada 1 """, font=("Century Gothic", 11), fg="white", bg="#292929")
    label_ejerc_22.pack(padx=5, pady=20)

    label_velocidadN6= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad del árbol de salida 6 en RPM",fg="black",bg="#D3D6FB")
    label_velocidadN6.pack()
    campo_velocidadN6=Entry(filewin,font=("Courier New", 11))
    campo_velocidadN6.pack(padx=2, pady=10)

    label_velocidadN1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad del árbol de entrada 1 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN1.pack()
    campo_velocidadN1=Entry(filewin, font=("Courier New", 11))
    campo_velocidadN1.pack(padx=3, pady=10)


    #Definición de formulas

    def operacion(N6, N1):
        return (N6)/(N1)

    def ejecutar_operacion():
        valor_num_velocidadN6 = int(campo_velocidadN6.get())
        valor_num_velocidadN1 = int(campo_velocidadN1.get())

        resultado = operacion(valor_num_velocidadN6, valor_num_velocidadN1)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton2b=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton2b.pack(side=TOP, padx=5, pady=15)
    boton2b.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Calibri",11) ,text="La relación de transmisión del mecanismo es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()


#Se define el ejercicio 5 opcion b --------------------------------------------------------------------------------------------------------------------
def ejercicio_5_opcionb():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="""Simulación del cálculo del diámetro de la polea de un tren de poleas
constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Apartir de la Fórmula de diámetro de la polea
        D = (N1*D1*D3)/(D2*N4)  """,font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack( pady=5)
    
    label_ejerc_22= Label(filewin,text="""D diámetro polea que arrastra al eje de la cinta transportadora,
                D1 diámetro polea motora 1,
                D2 diámetro polea conducida 2,
                D3 diámetro polea motora 3,
                N1 velocidad del eje motor 1,
                N4 velocidad de giro de la cinta transportadora,""", font=("Century Gothic", 11), fg="white", bg="#292929")
    label_ejerc_22.pack(padx=5, pady=20)

    label_diametro1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea motora D1 en mm:",fg="black",bg="#D3D6FB")
    label_diametro1.pack()
    campo_diametro1=Entry(filewin, font=("Courier New", 11))
    campo_diametro1.pack(padx=3, pady=10)

    label_diametro2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea conducida D2 en mm",fg="black",bg="#D3D6FB")
    label_diametro2.pack()
    campo_diametro2=Entry(filewin,font=("Courier New", 11))
    campo_diametro2.pack(padx=2, pady=10)

    label_diametro3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del diámetro de la polea motora D3 en mm:",fg="black",bg="#D3D6FB")
    label_diametro3.pack()
    campo_diametro3=Entry(filewin, font=("Courier New", 11))
    campo_diametro3.pack(padx=3, pady=10)

    label_velocidadN1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad del eje motor N1 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN1.pack()
    campo_velocidadN1=Entry(filewin,font=("Courier New", 11))
    campo_velocidadN1.pack(padx=2, pady=10)

    label_velocidadN4= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad de giro de la cinta transportadora N4 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN4.pack()
    campo_velocidadN4=Entry(filewin,font=("Courier New", 11))
    campo_velocidadN4.pack(padx=2, pady=10)


    #Definición de formulas

    def operacion(N1, D1, D3, D2, N4):
        return ((N1)*(D1)*(D3))/((D2)*(N4))

    def ejecutar_operacion():
        valor_num_velocidadN1 = int(campo_velocidadN1.get())
        valor_num_diametroD1 = int(campo_diametro1.get())
        valor_num_diametroD3 = int(campo_diametro3.get())
        valor_num_diametroD2 = int(campo_diametro2.get())
        valor_num_velocidadN4 = int(campo_velocidadN4.get())

        resultado = operacion(valor_num_velocidadN1, valor_num_diametroD1, valor_num_diametroD3,
                              valor_num_diametroD2,valor_num_velocidadN4)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton5b=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion)
    boton5b.pack(side=TOP, padx=5, pady=15)
    boton5b.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier new",11) ,text="""El valor del diámetro D de la polea que arrastra
    al eje de la cinta transportadora es""",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio opcion c --------------------------------------------------------------------------------------------------------------------
def ejercicio_opcionc():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="Simulacion del calculo de la potencia nominal del sistema por correa",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Apartir de la Fórmula de
     Dp = (2*poleaMayor)
     dp = (2*poleamenor)
     rel_diam=((Dp/dp))
     r=(1800/1000)
     ksr=float(rel_diam)
     pnc=(dp*r)*(1004-(1652/dp)-(0.1547*math.pow(dp*r,2))-(0.2126*math.log(dp*r)))+((1652*r)*1-(1/ksr))""",
    font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11) ,text="""L longitud de la correa
    R1 radio de la polea mayor
    r1 radio de la  polea menor""", fg="white", bg="#292929")
    label_datos.pack()

    label_longitud= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la Longitud de la correa en m:",fg="black",bg="#D3D6FB")
    label_longitud.pack()
    campo_longitud=Entry(filewin)
    campo_longitud.pack()

    label_polea_mayor= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la dimensión del diámetro de la polea mayor en m: ",fg="black",bg="#D3D6FB")
    label_polea_mayor.pack()
    campo_polea_mayor=Entry(filewin)
    campo_polea_mayor.pack()


    label_polea_menor= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la dimensión del diámetro de la polea menor en m:",fg="black",bg="#D3D6FB")
    label_polea_menor.pack()
    campo_polea_menor=Entry(filewin)
    campo_polea_menor.pack()


    #Definición de formulas

    def operacionDp(polea_mayor):
        return 2*polea_mayor

    def operacion_dp(polea_menor):
        return  2*polea_menor

    def operacion_rel_diam(polea_mayor, polea_menor):
        return  (2*polea_mayor)/(2*polea_menor)

    def operacion_ksr(polea_mayor, polea_menor):
        return  (2*polea_mayor)/(2*polea_menor)

    def operacion_pnc(polea_mayor, polea_menor):
        return  ((2*polea_menor)*1.8)*(1004-(1652/(2*polea_menor))-(0.1547*math.pow((2*polea_menor)*(1.8),2))-(0.2126*math.log(2*polea_menor)*(1.8)))+((1652*(1.8))*1-(1/(2*polea_mayor)/(2*polea_menor)))

    def ejecutar_operacion3():
        valor_num_longitud = float(campo_longitud.get())
        valor_polea_mayor = float(campo_polea_mayor.get())
        valor_polea_menor = float(campo_polea_menor.get())

        resultadoDp = operacionDp(valor_polea_mayor)
        label_valor_result_Dp.config(text = resultadoDp)

        resultadodp = operacion_dp(valor_polea_menor)
        label_valor_result_dp.config(text = resultadodp)

        resultado_rel_diam = operacion_rel_diam(valor_polea_mayor,valor_polea_menor)
        label_valor_result_rel_diam.config(text = resultado_rel_diam)

        resultado_ksr = operacion_ksr(valor_polea_mayor,valor_polea_menor)
        label_valor_result_ksr.config(text = resultado_ksr)

        resultado_pnc = operacion_pnc(valor_polea_mayor,valor_polea_menor)
        label_valor_result_pnc.config(text = resultado_pnc)

    #BOTON DE EJECUCION
    botonc=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion3)
    botonc.pack(side=TOP, padx=5, pady=15)
    botonc.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result_Dp= Label(filewin,font=("Courier New",11) ,text="El valor de Dp es de:  ",fg="white",bg="black", cursor="cross")
    label_result_Dp.pack()
    label_valor_result_Dp= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_Dp.pack()

    label_result_dp= Label(filewin,font=("Courier New",11) ,text="El valor de dp es de:  ",fg="white",bg="black", cursor="cross")
    label_result_dp.pack()
    label_valor_result_dp= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_dp.pack()

    label_result_rel_diam= Label(filewin,font=("Courier New",11) ,text="El valor de rel_diam es de:  ",fg="white",bg="black", cursor="cross")
    label_result_rel_diam.pack()
    label_valor_result_rel_diam= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_rel_diam.pack()
    
    label_result_ksr= Label(filewin,font=("Courier New",11) ,text="El valor de Ksr es de:  ",fg="white",bg="black", cursor="cross")
    label_result_ksr.pack()
    label_valor_result_ksr= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_ksr.pack()
     
    label_result_pnc= Label(filewin,font=("Courier New",11) ,text="El valor de la potencia nominal es:  ",fg="white",bg="black", cursor="cross")
    label_result_pnc.pack()
    label_valor_result_pnc= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_pnc.pack()



#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio id opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opciond():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="""Simulación del cálculo de relación de transmisión del mecanismo de un Tren de engranajes
    simple constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""i = z1*z3*z5 / z2*z4*z6""",
	font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11) ,text="""i = relación de transmisión
    z1 = número entero 1
    z2 = número entero 2
    z3 = número entero 3
    z4 = número entero 4
    z5 = número entero 5
    z6 = número entero 6""",
                        fg="white", bg="#292929")
    label_datos.pack()

    label_número1= Label(filewin,font=("Arial Narrow",11), text="Proporcione el valor del número entero del engranaje de entrada z1 en mm:",fg="black",bg="#D3D6FB")
    label_número1.pack()
    campo_número1=Entry(filewin)
    campo_número1.pack()

    label_número2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del número entero del engranaje de salida z2 en mm:",fg="black",bg="#D3D6FB")
    label_número2.pack()
    campo_número2=Entry(filewin)
    campo_número2.pack()


    label_número3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del número entero del engranaje de entrada z3 en mm:",fg="black",bg="#D3D6FB")
    label_número3.pack()
    campo_número3=Entry(filewin)
    campo_número3.pack()

    label_número4= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del número entero del engranaje de salida z4 en mm:",fg="black",bg="#D3D6FB")
    label_número4.pack()
    campo_número4=Entry(filewin)
    campo_número4.pack()

    label_número5= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del número entero del engranaje de entrada z5 en mm:",fg="black",bg="#D3D6FB")
    label_número5.pack()
    campo_número5=Entry(filewin)
    campo_número5.pack()

    label_número6= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor del número entero del engranaje de salida z6 en mm: ",fg="black",bg="#D3D6FB")
    label_número6.pack()
    campo_número6=Entry(filewin)
    campo_número6.pack()


    #Definición de formulas

    def operacion32(número1, número2, número3, número4, número5, número6):
        return (número1*número3*número5)/(número2*número4*número6)

    def ejecutar_operacion32():
        valor_número1 = int(campo_número1.get())
        valor_número2 = int(campo_número2.get())
        valor_número3 = int(campo_número3.get())
        valor_número4 = int(campo_número4.get())
        valor_número5 = int(campo_número5.get())
        valor_número6 = int(campo_número6.get())

        resultado = operacion32(valor_número1, valor_número2, valor_número3, valor_número4, valor_número5, valor_número6)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    botonid=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacion32)
    botonid.pack(side=TOP, padx=5, pady=15)
    botonid.config(bg="#B13BA7",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courser New",11) ,text="La relación de transmisión es i :  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('Trenengranajessimple.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio iid opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opciond():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="""Simulación del cálculo de la velocidad del eje de salida de un Tren de engranajes simple
constituido por tres escalonamientos en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""a partir de la ecuación de relación de transmisión
    N2 = N1 / i""",
	font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11) ,text="""i = relación de transmisión
    Ns = velocidad del eje de salida
    Ne = velocidad de la rueda de entrada""",
                        fg="white", bg="#292929")
    label_datos.pack()

    label_i= Label(filewin,font=("Arial Narrow",11), text="Proporcione el valor de la relación de transmisión del mecanismo:",fg="black",bg="#D3D6FB")
    label_i.pack()
    campo_i=Entry(filewin)
    campo_i.pack()

    label_velocidadN1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione la velocidad Ne del eje de entrada en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN1.pack()
    campo_velocidadN1=Entry(filewin)
    campo_velocidadN1.pack()


    #Definición de formulas

    def operacioniid(velocidadN1, i):
        return (velocidadN1)/(i)

    def ejecutar_operacioniid():
        valor_i = float(campo_i.get())
        valor_velocidadN1 = float(campo_velocidadN1.get())

        resultado = operacioniid(valor_i, valor_velocidadN1)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    botonid=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacioniid)
    botonid.pack(side=TOP, padx=5, pady=15)
    botonid.config(bg="#B13BA7",fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courser New",11) ,text="La velocidad N2 del eje de salida es de:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Tren de engranajes simple")
        image = img.imread('Trenengranajessimple.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio iiid opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_3_opciond():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="""Simulación del cálculo de Velocidad de giro de un tren de engranajes formado por engranajes
        en rpm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""a partir de la ecuación:

            i = Z1/Z3

            i = n2/n1

        Se despeja n2 de la ecuacion anterior:

            n2 = i * n1""",
	font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11),
              text="""donde:
    i relación de transmisión,
    Z1 número de dientes rueda motriz
    Z3 número de dientes rueda conducida
    n1 velocidad del eje de entrada del primer engranaje en RPM
    n2 velocidad del eje conducido del tercer engranaje en RPM""",
                        fg="white", bg="#292929")
    label_datos.pack()

    label_dientesZ1= Label(filewin,font=("Arial Narrow",11), text="Proporcione el número de dientes Z1 del engranaje de entrada 1:",fg="black",bg="#D3D6FB")
    label_dientesZ1.pack()
    campo_dientesZ1=Entry(filewin)
    campo_dientesZ1.pack()

    label_dientesZ3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el número de dientes Z3 del engranaje conducida 3:",fg="black",bg="#D3D6FB")
    label_dientesZ3.pack()
    campo_dientesZ3=Entry(filewin)
    campo_dientesZ3.pack()

    label_velocidadn1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la velocidad del eje de entrada N1 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadn1.pack()
    campo_velocidadn1=Entry(filewin)
    campo_velocidadn1.pack()


    #Definición de formulas

    def operacioni_iiid(dientesZ1, dientesZ3):
        return dientesZ1/dientesZ3

    def operacion_n2_iiid(dientesZ1, dientesZ3, velocidadn1):
        return (dientesZ1/dientesZ3) *(velocidadn1)

    def ejecutar_operacioniiid():
        valor_dientesZ1 = float(campo_dientesZ1.get())
        valor_dientesZ3 = float(campo_dientesZ3.get())
        valor_velocidadn1 = float(campo_velocidadn1.get())

        resultado_i = operacioni_iiid(valor_dientesZ1, valor_dientesZ3)
        label_valor_result_i.config(text = resultado_i)

        resultado_n2 = operacion_n2_iiid(valor_dientesZ1, valor_dientesZ3, valor_velocidadn1)
        label_valor_result_n2.config(text = resultado_n2)

    #BOTON DE EJECUCION

    botonid=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacioniiid)
    botonid.pack(side=TOP, padx=5, pady=15)
    botonid.config(bg="#B13BA7",fg="white",cursor="cross")

    # Resultados
    label_result_i= Label(filewin,font=("Courser New",11) ,text="La relación de transmisión del mecanismo es i :  ",fg="white",bg="black")
    label_result_i.pack()

    label_valor_result_i= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_i.pack()
    
    label_result_n2= Label(filewin,font=("Courser New",11) ,text="La velocidad de giro del tecer engranaje es n2: ",fg="white",bg="black")
    label_result_n2.pack()

    label_valor_result_n2= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_n2.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Tren de engranajes)")
        image = img.imread('tren de engranajes.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()    

#Se define el ejercicio ivd opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_4_opciond():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")

    titulo=Label(filewin, 
	text="""Simulación del cálculo del número de dientes de las ruedas conducidas de un tren de engranajes en mm""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""a partir de la ecuación de la relación de transmisión:

                i = N2 / N1 = Z1 / Z2 = (Z1*Z3)/(Z2*Z4) = (Z1*Z3)/(Z)""",
	font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11),
              text="""donde:
                i relación de transmisión,
                N1 velocidad del eje de entrada en RPM,
                N2 velocidad del eje de salida en RPM,
                Z1 número de dientes del engranaje de entrada 1,
                Z3 número de dientes del engranaje de entrada 3,
                Z2 número de dientes del engranaje de salida 2,
                Z4 número de dientes del engranaje de salida 4,
                Z número de dientes del engranaje de salida,""",
                        fg="white", bg="#292929")
    label_datos.pack()

    label_velocidadN1= Label(filewin,font=("Arial Narrow",11), text="Proporcione el valor de la velocidad del eje de entrada N1 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN1.pack()
    campo_velocidadN1=Entry(filewin)
    campo_velocidadN1.pack()

    label_velocidadN2= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el valor de la velocidad del eje de salida N2 en RPM:",fg="black",bg="#D3D6FB")
    label_velocidadN2.pack()
    campo_velocidadN2=Entry(filewin)
    campo_velocidadN2.pack()


    label_dientesZ1= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el número de dientes Z1 del engranaje de entrada 1:",fg="black",bg="#D3D6FB")
    label_dientesZ1.pack()
    campo_dientesZ1=Entry(filewin)
    campo_dientesZ1.pack()

    label_dientesZ3= Label(filewin,font=("Arial Narrow",11) ,text="Proporcione el número de dientes Z3 del engranaje de entrada 3:",fg="black",bg="#D3D6FB")
    label_dientesZ3.pack()
    campo_dientesZ3=Entry(filewin)
    campo_dientesZ3.pack()


    #Definición de formulas

    def operacion_i_ivd(velocidadN2, velocidadN1):
        return (velocidadN2)/(velocidadN1)

    def operacion_Z_ivd(dientesZ1, dientesZ3, velocidadN2, velocidadN1):
        return math.sqrt((dientesZ1*dientesZ3*velocidadN1)/velocidadN2)

    def ejecutar_operacionivd():
        valor_velocidadN1 = int(campo_velocidadN1.get())
        valor_velocidadN2 = int(campo_velocidadN2.get())
        valor_dientesZ1 = int(campo_dientesZ1.get())
        valor_dientesZ3 = int(campo_dientesZ3.get())
      

        resultado_i = operacion_i_ivd(valor_velocidadN1, valor_velocidadN2)
        label_valor_result_i.config(text = resultado_i)

        resultado_Z = operacion_Z_ivd(valor_velocidadN1, valor_velocidadN2, valor_dientesZ1, valor_dientesZ3)
        label_valor_result_Z.config(text = resultado_Z)

    #BOTON DE EJECUCION

    botonid=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacionivd)
    botonid.pack(side=TOP, padx=5, pady=15)
    botonid.config(bg="#B13BA7",fg="white",cursor="cross")

    # Resultados
    label_result_i= Label(filewin,font=("Courser New",11) ,text="La relación de transmisión del mecanismo es:  ",fg="white",bg="black")
    label_result_i.pack()
    label_valor_result_i= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_i.pack()


    label_result_Z= Label(filewin,font=("Courser New",11) ,text="El número de dientes Z de las ruedas conducidas Z2 y Z4 es:  ",fg="white",bg="black")
    label_result_Z.pack()
    label_valor_result_Z= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_Z.pack()

    
#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('Tren_engranes.jpg')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

#Se define el ejercicio vd opcion d --------------------------------------------------------------------------------------------------------------------
def ejercicio_5_opciond():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    filewin.title("iiia) Cálculo de Longitud de correa")
    
    contenedor = Frame(filewin)
    canvas = Canvas(contenedor, height = 300, width=450)
    scrollbar_v = Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    scrollbar_h = Scrollbar(contenedor, orient="vertical", command=canvas.xview)
    contenedor_scroll= Frame(canvas)
    contenedor_scroll.configure(bg="black")

    titulo=Label(filewin, 
	text="""Simulación del cálculo de la potencia nominal en transmisión por correa dentada, considerando el
                funcionamiento con carga suave y constante""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula=Label(filewin, 
	text="""Las formulas involucradas son:
                v=((n1*pb*z1)/60000)*2
                zm=((z1/2)-((pb*z1)/(2*(math.pi*math.pi)*c)*(z2-z1))*3
                kw=(bs/bso)*4
                if zm<6:
                   kz=(1-0.2*(6-zm))*5
                else:
                   kz=5
           
                P=(Kz*Kw*Ta-((bs*m*(v*v))/bso)*((v*0.001)*1)) """,
	font=("Century Gothic", 11), fg="white", bg="#292929")
    formula.pack(padx=5, pady=20)
    
    label_datos= Label(filewin,font=("Century Gothic",11),
              text="""Especificación de valores:
    P:  Potencia nominal de la correa (kW)
    kz:  Factor de engrane de los dientes
    kw: Factor de ancho
    Ta: Fuerza maxima admisible en la correa segun el ancho de referencia (N)
    bs: Ancho de la correa en mm
    bso = Ancho de referencia para el paso de la correa en mm
    m = Masa lineal de la correa segun ancho de referencia en Kg/m 
    v = Velocidad de la correa en m/s
    n1 = Frecuencia de rotacion polea menor (min^-1)
    pb =  Paso de los dientes de la correa y poeleas en mm
    z1 = numero de dientes polea menor
    z2 = numero de dientes polea mayor  
    zm = Numero de dientes de la correa engranados con la polea menor
    C = Distancia entre centros de poleas en mm""",
                        fg="white", bg="#292929")
    
    contenedor_scroll.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    ))
 
    canvas.create_window((0, 0), window=contenedor_scroll, anchor="nw")
 
    canvas.configure(yscrollcommand=scrollbar_v.set, xscrollcommand = scrollbar_h.set)
    
    label_datos.pack()

    label_Ta= Label(contenedor_scroll,font=("Arial Narrow",11), text="Proporcione el la fuerza maxima admisible en Newtons:",fg="black",bg="#D3D6FB")
    label_Ta.pack()
    campo_Ta=Entry(contenedor_scroll)
    campo_Ta.pack()

    label_bs= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del ancho de la correa en mm:",fg="black",bg="#D3D6FB")
    label_bs.pack()
    campo_bs=Entry(contenedor_scroll)
    campo_bs.pack()

    label_bso = Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del ancho de referencia de la correa en mm:",fg="black",bg="#D3D6FB")
    label_bso.pack()
    campo_bso=Entry(contenedor_scroll)
    campo_bso.pack()

    label_m= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor de la masa de la correa según el ancho de referencia em kg:",fg="black",bg="#D3D6FB")
    label_m.pack()
    campo_m=Entry(contenedor_scroll)
    campo_m.pack()

    label_nl= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor de la frecuencia de rotación en la polea menor en minutos:",fg="black",bg="#D3D6FB")
    label_nl.pack()
    campo_nl=Entry(contenedor_scroll)
    campo_nl.pack()

    label_pb= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el valor del paso de los dientes de la correa y las poleas en mm:",fg="black",bg="#D3D6FB")
    label_pb.pack()
    campo_pb=Entry(contenedor_scroll)
    campo_pb.pack()

    label_zl= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el numero de los dientes de la polea menor:",fg="black",bg="#D3D6FB")
    label_zl.pack()
    campo_zl=Entry(contenedor_scroll)
    campo_zl.pack()

    label_z2= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione el numero de los dientes de la polea mayor:",fg="black",bg="#D3D6FB")
    label_z2.pack()
    campo_z2=Entry(contenedor_scroll)
    campo_z2.pack()

    label_c= Label(contenedor_scroll,font=("Arial Narrow",11) ,text="Proporcione la distancia entre centros de las poleas en mm:",fg="black",bg="#D3D6FB")
    label_c.pack()
    campo_c=Entry(contenedor_scroll)
    campo_c.pack()


    #Definición de formulas

    def operacion_v(n1, pb, z1):
        return ((n1*pb*z1)/60000)*2

    def operacion_zm(z1, pb, z2, c):
        return ((z1/2)-((pb*z1)/(2*(math.pi*math.pi)*c))*(z2-z1))*3

    def operacion_kw(bs, bso):
        return (bs/bso)*4

    def operacion_kz(z1, pb, z2, c):
        return(1-0.2*(6-((z1/2)-((pb*z1)/(2*(math.pi*math.pi)*c))*(z2-z1))*3))*5 
    
    def operacion_p(Ta, bs, m, n1, pb, z1, bso):
        return(Ta*5*Ta)-(bs*m*((((n1*pb*z1)/60000)*2)*(((n1*pb*z1)/60000)*2))/(bso))*(((((n1*pb*z1)/60000)*2)*(1/1000))*1)
    

    def ejecutar_operacionvd():
        valor_Ta = float(campo_Ta.get())
        valor_bs = float(campo_bs.get())
        valor_bso = float(campo_bso.get())
        valor_m = float(campo_m.get())
        valor_n1 = float(campo_nl.get())
        valor_pb = float(campo_pb.get())
        valor_z1 = float(campo_zl.get())
        valor_z2 = float(campo_z2.get())
        valor_c = float(campo_c.get())

        resultado_v = operacion_v(valor_n1, valor_pb, valor_z1)
        label_valor_result_v.config(text = resultado_v)
      
        resultado_zm = operacion_zm(valor_z1, valor_pb, valor_z2, valor_c)
        label_valor_result_zm.config(text = resultado_zm)
        
        resultado_kw = operacion_kw(valor_bs, valor_bso)
        label_valor_result_kw.config(text = resultado_kw)

        resultado_kz = operacion_kz(valor_z1, valor_pb, valor_z2, valor_c)
        label_valor_result_kz.config(text = resultado_kz)

        resultado_p = operacion_p(valor_Ta, valor_bs, valor_m, valor_n1, valor_pb, valor_z1, valor_bso)
        label_valor_result_p.config(text = resultado_p)

    #BOTON DE EJECUCION

    botonid=Button(contenedor_scroll, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15,text="Ejecutar",command=ejecutar_operacionvd)
    botonid.pack(side=TOP, padx=5, pady=15)
    botonid.config(bg="#B13BA7",fg="white",cursor="cross")

    # Resultados
    label_result_kz= Label(contenedor_scroll,font=("Courser New",11) ,text="El valor del factor del engranaje de los dientes es:  ",fg="white",bg="black")
    label_result_kz.pack()
    label_valor_result_kz= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_kz.pack()


    label_result_kw= Label(contenedor_scroll,font=("Courser New",11) ,text="El valor del factor de ancho es:  ",fg="white",bg="black")
    label_result_kw.pack()
    label_valor_result_kw= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_kw.pack()

    label_result_v= Label(contenedor_scroll,font=("Courser New",11) ,text="El valor de la velocidad de la correa es:  ",fg="white",bg="black")
    label_result_v.pack()
    label_valor_result_v= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_v.pack()

    label_result_zm= Label(contenedor_scroll,font=("Courser New",11) ,text="La cantidad de dientes de l correa engranados con la polea menor es:  ",fg="white",bg="black")
    label_result_zm.pack()
    label_valor_result_zm= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_zm.pack()

    label_result_p= Label(contenedor_scroll,font=("Courser New",11) ,text="La potencia nominal de la correa es:  ",fg="white",bg="black")
    label_result_p.pack()
    label_valor_result_p= Label(contenedor_scroll,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_p.pack()

    
#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('engranajes.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

    contenedor.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_v.pack(side="right", fill="y")
    scrollbar_h.pack(side="bottom", fill="x")


#Se define el ejercicio 1 opcion e --------------------------------------------------------------------------------------------------------------------
def ejercicio_1_opcione():
    filewin = Toplevel(root)
    filewin.title("e) división y módulo de rueda dentada")
    filewin.configure(bg="black")

    
    titulo=Label(filewin, 
	text="Ejercicio 1 opcion e) : Calcular el  Diámetro primitivo (Dp)",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    titulo.pack(padx=5, pady=20)
    
    formula= Label(filewin,font=("Century Gothic",11) ,text="Fórmula  de la Transmisión parcial -> Dp=m*Z",
                        fg="white", bg="#292929")
    formula.pack()

    label_num_m= Label(filewin,font=("Ariel Narrow",11) ,text="Ingrese el módulo (m) en mm",fg="black",bg="#D3D6FB")
    label_num_m.pack()
    campo_num_m=Entry(filewin, font=("Courier New", 11))
    campo_num_m.pack()

    label_num_dientesz= Label(filewin,font=("Ariel Narrow",11) ,text="Ingrese el número de dientes de la rueda (Z)",fg="black",bg="#D3D6FB")
    label_num_dientesz.pack()
    campo_num_dientesz=Entry(filewin, font=("Courier New", 11))
    campo_num_dientesz.pack()



    #Definición de formulas

    def operacion51(m, Z):
        return ((m*Z))

    def ejecutar_operacion51():
        valor_num_m = int(campo_num_m.get())
        valor_num_dientesz = int(campo_num_dientesz.get())

        resultado = operacion51(valor_num_m, valor_num_dientesz)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton51=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion51)
    boton51.pack(side=TOP, padx=5, pady=15)
    boton51.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="La Transmisión parcial 1 es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('engranaje_opcion_g).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()



#Se define el ejercicio 2 opcion e --------------------------------------------------------------------------------------------------------------------
def ejercicio_2_opcione():
    filewin = Toplevel(root)
    filewin.title("e) La rueda dentada y sus dimensiones")
    filewin.configure(bg="black")
    formula=Label(filewin, 
	text="""Fórmula  para calcular las dimensiones:
                         Altura del diente (h): h=2.25*m
                         Altura de la cabeza del diente (hc): hc=m
                         Altura del pie del diente (hp): hp=1.25*m
                         Espesor del diente (e): e=0.5*P
                         Anchura del diente (B): B=m*10""",
	font="Calibri 11 bold", fg="black", bg="#85D5FE")
    formula.pack(padx=5, pady=20)
    
    label_ejerc_21= Label(filewin,font=("Calibri",11) ,text="Ejercicio 5.1 opcion e) : Calcular el  Diámetro primitivo (Dp)",
                        fg="black",bg="#85D5FE")
    label_ejerc_21.pack()

    label_num_m= Label(filewin,font=("Arial Narrow",11) ,text="Ingrese el módulo (m) en mm",fg="black",bg="#D3D6FB")
    label_num_m.pack()
    campo_num_m=Entry(filewin)
    campo_num_m.pack()

    label_num_dientesz= Label(filewin,font=("Arial Narrow",11) ,text="Ingrese el número de dientes de la rueda (Z)",fg="black",bg="#D3D6FB")
    label_num_dientesz.pack()
    campo_num_dientesz=Entry(filewin)
    campo_num_dientesz.pack()



    #Definición de formulas

    def operacion51(m, Z):
        return ((m*Z))

    def ejecutar_operacion51():
        valor_num_m = int(campo_num_m.get())
        valor_num_dientesz = int(campo_num_dientesz.get())

        resultado = operacion51(valor_num_m, valor_num_dientesz)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton51=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion51)
    boton51.pack()
    boton51.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="La Transmisión parcial 1 es:  ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('engranaje_opcion_g).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
    


 #Se define el ejercicio 1--------------------------------------------------------------------------------------------------------------------
def ejercicio_61_opcionf():
    filewin = Toplevel(root)
    filewin.title("f) Accionamiento simple por Rueda dentada interdependencia y transmisión")
    filewin.configure(bg="black")
    
    label_ejerc_61= Label(filewin,font=("Calibri",11) ,text="Ejercicio 6.1: Calculo de numero de revoluciones por Accionamiento simple de Rueda Dentada",
                        fg="black",bg="#85D5FE")
    label_ejerc_61.pack()

    label_num_dientesz1= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 1",fg="black",bg="#D3D6FB")
    label_num_dientesz1.pack()
    campo_num_dientesz1=Entry(filewin)
    campo_num_dientesz1.pack(padx=5, pady=15)

    label_num_dientesz2= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 2",fg="black",bg="#D3D6FB")
    label_num_dientesz2.pack()
    campo_num_dientesz2=Entry(filewin)
    campo_num_dientesz2.pack(padx=5, pady=15)

    label_revol_ini= Label(filewin,font=("Arial Narrow",11) ,text="Revolucion Inicial",fg="black",bg="#D3D6FB")
    label_revol_ini.pack()
    campo_revol_ini=Entry(filewin)
    campo_revol_ini.pack(padx=5, pady=15)



    #Definición de formulas

    def operacion(z1,z2,n1):
        return (z1*n1)/z2

    def ejecutar_operacion():
        valor_num_dientesz1 = int(campo_num_dientesz1.get())
        valor_num_dientesz2 = int(campo_num_dientesz2.get())
        valor_revol_ini = int(campo_revol_ini.get())

        resultado = operacion(valor_num_dientesz1, valor_num_dientesz2, valor_revol_ini)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton61=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion)
    boton61.pack(side=TOP, padx=5, pady=15)
    boton61.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="El numero de revoluciones final de la rueda es:  ",fg="white",bg="black")
    label_result.pack(pady=2)

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack(pady=5)

#Generar grafica de opcion f)
    def GenerarGrafica_opcionf():
        plt.title("Rueda dentada de ejercicio opcion f)")
        image = img.imread('Rueda_dentada.png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionf)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()




#Se define el ejercicio2--------------------------------------------------------------------------------------------------------------------
def ejercicio_71_opciong():
    filewin = Toplevel(root)
    filewin.title("g) Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total.")
    filewin.configure(bg="black")

    label_ejerc_71= Label(filewin,font=("Courier New",11) ,text="""Ejercicio 7.1 opcion g): Calculo de transmision total
    de Accionamiento múltiple por Rueda dentada """,
                         fg="black",bg="#85D5FE")
    label_ejerc_71.pack()

    label_num_dientesz1= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 1",fg="black",bg="#D3D6FB")
    label_num_dientesz1.pack()
    campo_num_dientesz1=Entry(filewin)
    campo_num_dientesz1.pack(padx=5, pady=15)

    label_num_dientesz2= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 2",fg="black",bg="#D3D6FB")
    label_num_dientesz2.pack()
    campo_num_dientesz2=Entry(filewin)
    campo_num_dientesz2.pack(padx=5, pady=15)

    label_num_dientesz3= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 3",fg="black",bg="#D3D6FB")
    label_num_dientesz3.pack()
    campo_num_dientesz3=Entry(filewin)
    campo_num_dientesz3.pack(padx=5, pady=15)

    label_num_dientesz4= Label(filewin,font=("Arial Narrow",11) ,text="Numero de dientes 4",fg="black",bg="#D3D6FB")
    label_num_dientesz4.pack()
    campo_num_dientesz4=Entry(filewin)
    campo_num_dientesz4.pack(padx=5, pady=15)
  

    #Definición de formulas

    def operacion(z1,z2,z3,z4):
        return ((z2*z4)/(z1*z3))

    def ejecutar_operacion():
        valor_num_dientesz2 = int(campo_num_dientesz2.get())
        valor_num_dientesz4 = int(campo_num_dientesz4.get())
        valor_num_dientesz1 = int(campo_num_dientesz1.get())
        valor_num_dientesz3 = int(campo_num_dientesz3.get())

        resultado = operacion(valor_num_dientesz1, valor_num_dientesz2, valor_num_dientesz3, valor_num_dientesz4)
        label_valor_result.config(text = resultado)

    #BOTON DE EJECUCION

    boton71=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion)
    boton71.pack(side=TOP, padx=5, pady=15)
    boton71.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result= Label(filewin,font=("Courier New",11) ,text="La transmision total es: ",fg="white",bg="black")
    label_result.pack()

    label_valor_result= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result.pack()

    
#Se genera grafica del ejercicio opcion g)
    def GenerarGrafica_opciong():
        plt.title("Engranaje y rueda de ejercicio opcion g)")
        image = img.imread('engranaje_opcion_g).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

    

#EJERCICIO 3--------------------------------------------------------------------------------------------------------------
def ejercicio_81_opcionh():
    filewin = Toplevel(root)
    filewin.title("h) Accionamiento por cremallera y por tornillo sin fin, carrera de cremallera accionamiento por tornillo sin fin, interdependencias")
    filewin.configure(bg="black")

    label_ejerc_81= Label(filewin,font=("Calibri",11) ,text="Ejercicio 8.1 opcion h): Calculo de Accionamiento de cremallera sin fin",fg="black",bg="#85D5FE")
    label_ejerc_81.pack()

    label_dientes_cremallera= Label(filewin,font=("Arial Narrow",11) ,text="Dientes de la cremallera",fg="black",bg="#D3D6FB")
    label_dientes_cremallera.pack()
    campo_dientes_cremallera=Entry(filewin)
    campo_dientes_cremallera.pack(padx=5, pady=15)
    
    label_modulo_cremallera= Label(filewin,font=("Arial Narrow",11) ,text="Modulo",fg="black",bg="#D3D6FB")
    label_modulo_cremallera.pack()
    campo_modulo_cremallera=Entry(filewin)
    campo_modulo_cremallera.pack(padx=5, pady=15)


    #Definición de formulas
    def operacion_81(z,m):
        return (z*m*math.pi)

    def ejecutar_operacion_81():
    
        #valor dientes z
        valor_dientes_cremallera_z = int(campo_dientes_cremallera.get())
        #valor modulo m
        valor_modulo_cremallera_m = int(campo_modulo_cremallera.get())
       

        resultado_81 = operacion_81(valor_dientes_cremallera_z,valor_modulo_cremallera_m)
        label_valor_result_81.config(text = resultado_81)


    #BOTON DE EJECUCION
    boton81=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion_81)
    boton81.pack(side=TOP, padx=5, pady=15)
    boton81.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result_81= Label(filewin,font=("Courier New",11) ,text="El accionamiento de la cremallera es: ",fg="white",bg="black")
    label_result_81.pack()

    label_valor_result_81= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_81.pack()

#Se genera grafica del ejercicio opcion h)
    def GenerarGrafica_opciong():
        plt.title("Cremallera de ejercicio opcion h)")
        image = img.imread('cremallera_opcion_h).png')
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opciong)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()

#Ejercicio 9.1 opcion i) ---------------------------------------------------
def ejercicio_91_opcioni():

    filewin = Toplevel(root)
    filewin.title("i) Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas.")
    filewin.configure(bg="black")
    
    label_ejerc_91= Label(filewin,font=("Calibri",11) ,text="Ejercicio 9.1 opcion i): Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas",
                         fg="black",bg="#85D5FE")
    label_ejerc_91.pack()

    label_dato1_ej91= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de dientes del engranaje 1 de entrada:",fg="black",bg="#D3D6FB")
    label_dato1_ej91.pack()
    campo_dato1_ej91=Entry(filewin)
    campo_dato1_ej91.pack(padx=5, pady=15)

    label_dato2_ej91= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de dientes del engranaje 2 de entrada:",fg="black",bg="#D3D6FB")
    label_dato2_ej91.pack()
    campo_dato2_ej91=Entry(filewin)
    campo_dato2_ej91.pack(padx=5, pady=15)

    label_dato3_ej91= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de dientes del engranaje 1 de salida:",fg="black",bg="#D3D6FB")
    label_dato3_ej91.pack()
    campo_dato3_ej91=Entry(filewin)
    campo_dato3_ej91.pack(padx=5, pady=15)

    label_dato4_ej91= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de dientes del engranaje 2 de salida:",fg="black",bg="#D3D6FB")
    label_dato4_ej91.pack()
    campo_dato4_ej91=Entry(filewin)
    campo_dato4_ej91.pack(padx=5, pady=15)

    #Definición de formulas

    def operacion_91(z1,z2,z3,z4):
        return ((z1*z3)/(z2*z4))


    def ejecutar_operacion_91():

        #Cuantos dientes tiene el engranaje 1 de entrada
        valor_dientes_engranajez1 = int(campo_dato1_ej91.get())

        #Cuantos dientes tiene el engranaje 2 de entrada
        valor_dientes_engranajez3 = int(campo_dato2_ej91.get())

        #Cuantos dientes tiene el engranaje 1 de salida
        valor_dientes_engranajez2 = int(campo_dato3_ej91.get())
    
        #Cuantos dientes tiene el engranaje 2 de salida
        valor_dientes_engranajez4 = int(campo_dato4_ej91.get())

        resultado_91 = operacion_91(valor_dientes_engranajez1,valor_dientes_engranajez3,valor_dientes_engranajez2, valor_dientes_engranajez4)
        label_valor_result_91.config(text = resultado_91)


        #BOTON DE EJECUCION

    boton91=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion_91)
    boton91.pack()
    boton91.config(bg="#B13BA7", fg="white",cursor="cross")


    label_result_91= Label(filewin,font=("Courier New",11) ,text="La relación de transmisión de las ruedas es : ",fg="white",bg="black")
    label_result_91.pack()


    label_valor_result_91= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_91.pack()

#Se genera grafica del ejercicio opcion i)
    def GenerarGrafica_opcioni():
        plt.title("Juego de ruedas de ejercicio opcion i)")
        image = img.imread("juego_ruedas_opcioni).png")
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcioni)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
        
    


#Ejercicio 10.1 ---------------------------------------------------
def ejercicio_10_1_opcionj():
    
    filewin = Toplevel(root)
    filewin.title("j) Engranajes como convertidores de par, transmisión de engranajes y conversión de par.")
    filewin.configure(bg="black")
    
    label_ejerc_10_1= Label(filewin,font=("Calibri",17) ,text="Ejercicio 10.1 opcion j): Calculo momento de giro de engranaje conversion par",
                         fg="black",bg="#85D5FE")
    label_ejerc_10_1.pack()

    label_dato1_ej10_1= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de diente z1:",fg="black",bg="#D3D6FB")
    label_dato1_ej10_1.pack()
    campo_dato1_ej10_1=Entry(filewin)
    campo_dato1_ej10_1.pack(padx=5, pady=15)

    label_dato2_ej10_1= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero de dientes z2:",fg="black",bg="#D3D6FB")
    label_dato2_ej10_1.pack()
    campo_dato2_ej10_1=Entry(filewin)
    campo_dato2_ej10_1.pack(padx=5, pady=15)

    label_dato3_ej10_1= Label(filewin,font=("Arial Narrow",11) ,text="Introduzca el numero par de salida:",fg="black",bg="#D3D6FB")
    label_dato3_ej10_1.pack()
    campo_dato3_ej10_1=Entry(filewin)
    campo_dato3_ej10_1.pack(padx=5, pady=15)


    #Definición de formulas

    def operacion_10_1(z1,z2,M2):
        return ((M2*z1)/z2)

    def ejecutar_operacion_10_1():
    
        #valor z1
        valor_dientes_engrane_z1 = int(campo_dato1_ej10_1.get())
        #valor z2
        valor_dientes_engrane_z2 = int(campo_dato2_ej10_1.get())
        #valor M2
        valor_revol_engrane_M2 = int(campo_dato3_ej10_1.get())

        resultado_10_1 = operacion_5(valor_dientes_engrane_z1,valor_dientes_engrane_z2,valor_revol_engrane_M2)
        label_valor_result_10_1.config(text = resultado_10_1)


    #BOTON DE EJECUCION
    boton10_1=Button(filewin, font=("OCR A Extended", 13, "bold"), borderwidth=3, relief="solid", width=15, text="Ejecutar",command=ejecutar_operacion_10_1)
    boton10_1.pack(side=TOP, padx=5, pady=15)
    boton10_1.config(bg="#B13BA7", fg="white",cursor="cross")

    # Resultados
    label_result_10_1= Label(filewin,font=("Courier New",11) ,text="El momento de momento de giro de impulsión es: ",fg="white",bg="black")
    label_result_10_1.pack()

    label_valor_result_10_1= Label(filewin,font=("Cambria",11) ,text="",fg="white",bg="#2F03CF")
    label_valor_result_10_1.pack()

#Se genera grafica del ejercicio opcion j)
    def GenerarGrafica_opcionj():
        plt.title("Engranaje como convertidor par de ejercicio opcion j)")
        image = img.imread("engranaje_opcionj).png")
        plt.imshow(image)
        plt.show()

    buttonExample = Button(filewin, 
                text="Generar grafica",
                command=GenerarGrafica_opcionj)
    buttonExample.config(bg="#DCCFF3", fg="#7000B7")
    buttonExample.pack()
    
    

#abrir imagen de formulas de Accionamiento simple por Rueda dentada interdependencia y transmisión 
def abroimagenf11():
    messagebox.showinfo("Formula para calcular interdependencia de la rueda dentada",
                        message="Esta es la formula para calcular interdependencia de la rueda dentada")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x310+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento simple por Rueda dentada interdependencia")
    imagenf11=PhotoImage(file="formula_1_ejer_1_AS_ruedadent_interdepen.png", master=ventanaAbrir)
    lblImagen11=Label(ventanaAbrir,image=imagenf11)

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("400x310+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf11, command=descarga, height=240, width=330).place(x=30, y=30)
 #cambio de codigo en comando, original command=abroimagenf11
    ventanaAbrir.mainloop()
  


def abroimagenf12():
    messagebox.showinfo("Formula 2 para calcular transmision de la rueda dentada",
                        message="Esta es la formula para calcular transmision de la rueda dentada")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x220+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento simple por Rueda dentada transmisión")
    imagenf12=PhotoImage(file="formula_1_ejer_1_AS_ruedadent_transmision.png", master=ventanaAbrir)
    lblImagen12=Label(ventanaAbrir,image=imagenf12)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("400x310+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf12, command=descarga, height=168, width=260).place(x=65, y=30)
 #cambio de codigo en comando, original command=abroimagenf12
    ventanaAbrir.mainloop()


def abroimagenf13():
    messagebox.showinfo("Formula 3 para calcular la distancia entre ejes",
                        message="Esta es la formula para la distancia entre ejes")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("400x220+100+100")
    ventanaAbrir.title("Formula 3 de Accionamiento simple por Rueda dentada transmisión")
    imagenf13=PhotoImage(file="formula_1_ejer_2_AS_ruedadent_distancia.png", master=ventanaAbrir)
    lblImagen13=Label(ventanaAbrir,image=imagenf13)
    
#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula3_opcionf).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)

        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenf13, command=descarga, height=168, width=260).place(x=65, y=25)
 #cambio de codigo en comando, original command=abroimagenf13
    ventanaAbrir.mainloop()



#abrir imagen de formulas de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total
def abroimageng21():
    messagebox.showinfo("Formula 1 para calcular la transmision parcial",
                        message="Esta es la formula para calcular la transmision parcial")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("430x440+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total")
    imageng21=PhotoImage(file="formula_2_ejer_1_reuda_dent_TP.png", master=ventanaAbrir)
    lblImagen21=Label(ventanaAbrir,image=imageng21)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opciong).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageng21, command=descarga, height=405, width=400).place(x=10, y=20)
 #cambio de codigo en comando, original command=abroimageng21
    ventanaAbrir.mainloop()

def abroimageng22():
    messagebox.showinfo("Formula 2 para calcular la transmision total",
                        message="Esta es la formula para calcular la transmision total")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("445x320+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total")
    imageng22=PhotoImage(file="formula_2_ejer_2_reuda_dent_TT.png", master=ventanaAbrir)
    lblImagen22=Label(ventanaAbrir,image=imageng22)
    

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opciong).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageng22, command=descarga, height=267, width=405).place(x=10, y=30)
 #cambio de codigo en comando, original command=abroimageng22
    ventanaAbrir.mainloop()


#abrir imagen de formulas de Accionamiento por cremallera y por tornillo sin fin,
#carrera de cremallera accionamiento por tornillo sin fin, interdependencias
def abroimagenh31():
    messagebox.showinfo("Formula1 para calcular tornillo sin fin",
                        message="Esta es la formula para calcular tornillo sin fin")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("550x400+100+100")
    ventanaAbrir.title("Formula 1 de Accionamiento por cremallera y por tornillo sin fin")
    imagenh31=PhotoImage(file="formula_3_ejer_1_tornillo.png", master=ventanaAbrir)
    lblImagen31=Label(ventanaAbrir,image=imagenh31)
    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionh).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenh31, command=descarga, height=338, width=500).place(x=20, y=45)
 #cambio de codigo en comando, original command=abroimagenh31
    ventanaAbrir.mainloop()


def abroimagenh32():
    messagebox.showinfo("Formula 2 para calcular cremallera sin fin",
                        message="Esta es la formula para calcular cremallera sin fin")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("450x250+100+100")
    ventanaAbrir.title("Formula 2 de Accionamiento por cremallera y por tornillo sin fin")
    imagenh32=PhotoImage(file="formula_3_ejer_2_cremallera.png", master=ventanaAbrir)
    lblImagen32=Label(ventanaAbrir,image=imagenh32)

#Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula2_opcionh).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenh32, command=descarga, height=99, width=300).place(x=60, y=50)
 #cambio de codigo en comando, original command=abroimagenh32
    ventanaAbrir.mainloop()




#4 abrir imagen de formulas de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas
def abroimageni4():
    messagebox.showinfo("Formula para calcular ruedas de cambio interdependencia",
                        message="Esta es la formula para calcular  ruedas de cambio interdependencia")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("700x460+100+100")
    ventanaAbrir.title("Formula de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas")
    imageni4=PhotoImage(file="formula_4_ejer_1_ruedas.png", master=ventanaAbrir)
    lblImagen4=Label(ventanaAbrir,image=imageni4)
    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula_opcioni).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imageni4, command=descarga, height=314, width=666).place(x=60, y=90)
 #cambio de codigo en comando, original command=abroimageni4
    ventanaAbrir.mainloop() 



#5 abrir imagen de formulas de Engranajes como convertidores de par, transmisión de engranajes y conversión de par
def abroimagenj51():
    messagebox.showinfo("Formula 1 para calcular Transmisión de engranajes",
                        message="Esta es la formula para calcular Transmisión de engranajes")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("435x500+100+100")
    ventanaAbrir.title("Formula 1 de Engranajes como convertidores de par, transmisión de engranajes y conversión de par")
    imagenj51=PhotoImage(file="formula_5_ejer_1_engranajes_transmision.png", master=ventanaAbrir)
    lblImagen51=Label(ventanaAbrir,image=imagenj51)

    #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x110+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("formula1_opcionj).png", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenj51, command=descarga, height=314, width=400).place(x=10, y=100)
 #cambio de codigo en comando, original command=abroimagenj51
    ventanaAbrir.mainloop() 


def abroimagenj52():
    messagebox.showinfo("Formula para calcular Conversión de par",
                        message="Esta es la formula para calcular Conversión de par")
    
    ventanaAbrir=Tk()
    ventanaAbrir.geometry("435x400+100+100")
    ventanaAbrir.title("Formula 2 de Engranajes como convertidores de par, transmisión de engranajes y conversión de par")
    imagenj52=PhotoImage(file="formula_5_ejer_2_engranajes_conversion_par.png", master=ventanaAbrir)
    lblImagen52=Label(ventanaAbrir,image=imagenj52)
         #Interfaz    
    def descarga():
        ventana=Tk()
        ventana.geometry("310x100+100+100")
        ventana.title("Descarga de toma de Screenshot")

        label_guardar=Label(ventana,text="Guardar como: ", font=("",10,"bold"), bg="white")
        label_guardar.grid(row=1,column=0,pady=5,padx=5)

        ventana.texto_guardado=Entry(ventana, width = 30)
        ventana.texto_guardado.grid(row=1,column=1,pady=5,padx=5)


#Funcion para navegar y guardar la imagen
        def navegar():
            ventana.archivo= filedialog.asksaveasfilename(title="Guardar como: ",
                                                                          initialdir ="C:\\",
                                                                          defaultextension = " .png",
                                                                          filetypes=(("Archivo PNG", "*.png"), ("Todos los archivos","*.*")))
            ventana.texto_guardado.insert("1",ventana.archivo)

        def captura():
            
            captura = pyautogui.screenshot()

            captura = cv2.cvtColor(np.array(captura),
                                                   cv2.COLOR_RGB2BGR)
            cv2.imwrite("", captura) 
            messagebox.showinfo("Exito", "Captura guardada")
                            
 
        botonguardar= Button(ventana,text="Navegar",command=navegar,width=10)
        botonguardar.grid(row=1,column=2,pady=5,padx=5)

        botonnavegar= Button(ventana,text="Guardar",command=captura,width=10)
        botonnavegar.grid(row=2,column=1,pady=5,padx=5)
        ventana.mainloop()
    boton=Button(ventanaAbrir, image=imagenj52, command=descarga, height=235, width=400).place(x=10, y=30)
 #cambio de codigo en comando, original command=abroimagenj52
    ventanaAbrir.mainloop() 


root=Tk()
root.geometry("550x400+0+0")
root.title("Simulacion de mecanismos")
root.configure(width=1000, height=500)

#creamos imagen como background de la ventana root
fondo =  PhotoImage(file='codigofondo.png')
label_fondo = Label(root, image=fondo).place(x=0, y=0, relwidth = 1, relheight = 1)

#imagen =  PhotoImage(file='engranajes-gif-sin-fondo-4.gif')
#label_imagen = Label(root, image=imagen).place(x=0,y=0)


label_saludos= Label(root, font=("Century Gothic", 24),text="Bienvenido querido/a  estudiante", fg="white",bg="black")
label_saludos.place(x="5",y="0")
label_explicacion1= Label(root, font=("Century Gothic", 11), text="Lo invitamos a resolver problemas de mecanismos",
                          bg="black", fg="#6474D1")
label_explicacion2= Label(root, font=("Century Gothic", 11), text="para simular que se aplican en robotica",
                          bg="black", fg="#6474D1")
label_explicacion3= Label(root, font=("Century Gothic", 11), text="Buena suerte!",
                          bg="black", fg="#6474D1")
label_explicacion1.place(x=30,y=108, width=450, height=20)
label_explicacion2.place(x=30,y=128, width=450, height=20)
label_explicacion3.place(x=30,y=268, width=450, height=20)
menubar1 = Menu(root)
root.config(menu=menubar1)
        
        
opciones1 = Menu(menubar1)
submenu6= Menu(menubar1, tearoff=0)
#Submenu de Accionamiento simple por Rueda dentada interdependencia y transmisión con sus formulas
submenu6.add_command(label="Formula 1 para calcular la interdependencia", command=abroimagenf11)
submenu6.add_command(label="Formula 2 para calcular la transmision", command=abroimagenf12)
submenu6.add_command(label="Formula 3 para calcular distancia entre ejes", command=abroimagenf13)
opciones1.add_cascade(label="f) Accionamiento simple por Rueda dentada interdependencia y transmisión", menu= submenu6)


#Submenu de Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total
submenu7= Menu(menubar1, tearoff=0)
submenu7.add_command(label="Formula 1 para calcular la transmision parcial", command=abroimageng21)
submenu7.add_command(label="Formula 2 para calcular la transmision total", command=abroimageng22)
opciones1.add_cascade(label="g) Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total", menu= submenu7)


#Submenu de Accionamiento por cremallera y por tornillo sin fin, carrera de cremallera accionamiento por tornillo sin fin, interdependencias
submenu8=Menu(menubar1, tearoff=0)
submenu8.add_command(label="Formula 1 para calcular el tornillo sin fin", command=abroimagenh31)
submenu8.add_command(label="Formula 2 para calcular la creamellera sin fin", command=abroimagenh32)
opciones1.add_cascade(label="h) Accionamiento por cremallera y por tornillo sin fin,carrera de cremallera accionamiento por tornillo sin fin, interdependencias", menu= submenu8)

#Submenu de Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas
submenu9=Menu(menubar1, tearoff=0)
submenu9.add_command(label="Formula para calcular ruedas de interdependencia", command=abroimageni4)
opciones1.add_cascade(label="i) Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas", menu= submenu9)

#Submenu de Engranajes como convertidores de par, transmisión de engranajes y conversión de par
submenu10=Menu(menubar1, tearoff=0)
submenu10.add_command(label="Formula 1 para calcular Transmisión de engranajes", command=abroimagenj51)
submenu10.add_command(label="Formula 2 para calcular Conversión de par",command=abroimagenj52)
opciones1.add_cascade(label="j) Engranajes como convertidores de par, transmisión de engranajes y conversión de par", menu= submenu10)
      
opciones1.add_separator()
opciones1.add_command(label="Salir", font=("Century Gothic bold", 11), command=root.destroy)


menubar1.add_cascade(label="Formulas", font=("Century Gothic bold", 11), menu=opciones1) 


#Se crea el menu Ejercicios con sus submenus           
opciones2 = Menu(menubar1, tearoff=0)


#Submenu de Ejercicio opcion a) Sistema de polea y correa
submenu1=Menu(menubar1, tearoff=0)
submenu1.add_command(label="Ejercicio ia) Cálculo de la Relación de transmisión de velocidad ", command=ejercicio_1_opciona)
submenu1.add_command(label="Ejercicio iia) Cálculo de velocidad que gira el eje conducido ",command=ejercicio_2_opciona)
submenu1.add_command(label="Ejercicio iiia) Cálculo de Longitud de correa",command=ejercicio_3_opciona)
opciones2.add_cascade(label="a) Sistema de polea y correa", menu= submenu1)

#Submenu de Ejercicio opcion b) Tren de Poleas
submenu2=Menu(menubar1, tearoff=0)
submenu2.add_command(label="Ejercicio 1) Cálculo de la relación de transmisión del mecanismo", command=ejercicio_1_opcionb)
submenu2.add_command(label="Ejercicio 2) Cálculo de la velocidad del eje de salida",command=ejercicio_2_opcionb)
submenu2.add_command(label="Ejercicio 3) Cálculo de la velocidad del último árbol", command=ejercicio_3_opcionb)
submenu2.add_command(label="Ejercicio 4) Cálculo de la relación de transmisión de velocidad total",command=ejercicio_4_opcionb)
submenu2.add_command(label="Ejercicio 5) Cálculo de diámetro de polea", command=ejercicio_5_opcionb)
opciones2.add_cascade(label="b) Tren de Poleas", menu= submenu2)


#Submenu de Ejercicio opcion c) Potencia nominal de correa
submenu3=Menu(menubar1, tearoff=0)
submenu3.add_command(label="Calculo de potencia nominal de correa", command=ejercicio_opcionc)
opciones2.add_cascade(label="c) Calculo Potencia nominal de correa", menu= submenu3)


#Submenu de Ejercicio opcion d) Engranajes: tren de engranajes simple
submenu4=Menu(menubar1, tearoff=0)
submenu4.add_command(label="id) Cálculo de la relación de transmisión del mecanismo", command=ejercicio_1_opciond)
submenu4.add_command(label="iid) Cálculo de la velocidad del eje de salida",command=ejercicio_2_opciond)
submenu4.add_command(label="iiid) Cálculo de la Velocidad de giro",command=ejercicio_3_opciond)
submenu4.add_command(label="ivd) Cálculo de Número de dientes",command=ejercicio_4_opciond)
submenu4.add_command(label="vd) Cálculo de Potencia nominal en transmisión por correa dentada",command=ejercicio_5_opciond)
opciones2.add_cascade(label="d) Calculo de engranajes: tren de engranajes simple", menu= submenu4)


#Submenu de Ejercicio opcion e) La rueda dentada y sus dimensiones, división y módulo
submenu5=Menu(menubar1, tearoff=0)
submenu5.add_command(label="ie) Cálculo división y módulo de rueda dentada", command=ejercicio_1_opcione)
submenu5.add_command(label="iie) Cálculo La rueda dentada y sus dimensiones",command=ejercicio_2_opcione)
opciones2.add_cascade(label="e) La rueda dentada y sus dimensiones, división y módulo", menu= submenu5)


opciones2.add_command(label="Ejercicio f) Accionamiento simple por Rueda dentada interdependencia y transmisión", command=ejercicio_61_opcionf)
opciones2.add_command(label="Ejercicio g) Accionamiento múltiple por Rueda dentada transmisiones parciales transmisión total", command=ejercicio_71_opciong)
opciones2.add_command(label="Ejercicio h) Accionamiento por cremallera y por tornillo sin fin, carrera de cremallera accionamiento por tornillo sin fin, interdependencias", command=ejercicio_81_opcionh)
opciones2.add_command(label="Ejercicio i) Cálculo de ruedas de cambio interdependencia ruedas de cambio juegos de ruedas.", command=ejercicio_91_opcioni)
opciones2.add_command(label="Ejercicio j) Engranajes como convertidores de par, transmisión de engranajes y conversión de par.", command=ejercicio_10_1_opcionj)
menubar1.add_cascade(label="Ejercicios", font=("Century Gothic bold", 11), menu=opciones2) 

opciones2.add_separator()

#Se crea el submenu Ajustes
def gracias():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    label_gracias= Label(filewin,font=("a Astro Space",11) ,text="""
Gracias por usar el software de mecanismos simulados
                         """, fg="white",bg="black")
    label_gracias.pack()

def help():
    filewin = Toplevel(root)
    filewin.configure(bg="black")
    label_gracias= Label(filewin,font=("a Astro Space",11) ,text="""Si tiene alguna duda, comunicarse con los alumnos""", fg="white",bg="black")
    label_gracias.pack()

    label_alumnos= Label(filewin,font=("Cyberpunk",11) ,text="""Abril  Mejia  Rangel
    Raúl  Iván  Ramirez  Aguilar""", fg="yellow",bg="black")
    label_alumnos.pack()

def about():
    filewin = Toplevel(root)
    filewin.title("Que es nuestro software")
    label_about= Label(filewin,font=("a Astro Space",11) ,text="""Software simulador de mecanismos aplicados en robotica para
    practica de datos y decicado a los estudiantes del ITS""",fg="white",bg="black""")
    label_about.pack()


submenu1= Menu(menubar1, tearoff=0)
submenu1.add_command(label="Agradecimientos", font=("Century Gothic bold", 11), command=gracias)
submenu1.add_command(label="Ayuda", font=("Century Gothic bold", 11), command=help)
submenu1.add_command(label="Que es nuestro software", font=("Century Gothic bold", 11), command=about)
opciones2.add_cascade(label="Ajustes", font=("Century Gothic bold", 11), menu= submenu1)        


root.config(menu=menubar1)

#ventanaDescargar=Tk()
#ventanaDescargar.mainloop()
root.mainloop()
