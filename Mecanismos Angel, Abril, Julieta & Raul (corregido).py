header = """Simulación de Mecanismos aplicados en Robótica
Los modelos con enfoque impulsado por datos data-driven,
se emplean en las empresas para la toma de decisiones estratégicas
basadas en el análisis de datos y la interpretación.

Mecanismos que universalmente se emplean en robótica

"""
print(header)

import numpy as np
import math
print(math.pi)

def menu():
   print("\nSeleccione una opción")
   print(" \t a capture a para calcular el Sistema de polea y correa ")
   print(" \t\t ia) Cálculo de la Relación de transmisión de velocidad  ")
   print(" \t\t iia) Cálculo de velocidad que gira el eje conducido ")
   print(" \t\t iiia) Cálculo de Longitud de correa  ")
   print(" \t\t iva) Capture la letra q para salir de Sistema de polea y correa")
   print(" \t b capture b para calcular tren de poleas  ")
   print("\t\t 1) Cálculo de la relación de transmisión del mecanismo")
   print("\t\t 2) Cálculo de la velocidad del eje de salida")
   print("\t\t 3) Cálculo de la velocidad del último árbol")
   print("\t\t 4) Cálculo de la relación de transmisión de velocidad total")
   print("\t\t 5) Cálculo de diámetro de polea")
   print("\t\t 6) Capture la letra q para salir de Tren de poleas")
   print(" \t c Calculo de potencia nominal de correa  ")
   print(" \t d Calculo de engranajes: tren de engranajes simple  ")
   print(" \t\t id) Cálculo de la relación de transmisión del mecanismo")
   print(" \t\t iid) Cálculo de la velocidad del eje de salida ")
   print(" \t\t iiid) Cálculo de la Velocidad de giro  ")
   print(" \t\t ivd) Cálculo de Número de dientes  ")
   print(" \t\t vd) Cálculo de Potencia nominal en transmisión por correa dentada  ")
   print(" \t q Capture la letra q para salir ")
while ( True ):
   menu()
   opcionMenu = input(" Escriba la letra de la opción ")
   if opcionMenu == "a":
      print ("selecciono a")


      menuItems = np.array(["ia","iia","iiia","q"])
      while True:
           menu()
           opcionMenu = input("""Escriba el número de la opción de Sistema de polea y correa o q para salir del mecanismo
de Sistema de polea y correa """)
           if opcionMenu == "ia":
              print ("Seleccionó ia")
              header = """Simulación del cálculo de relación de transmisión de velocidad
              del mecanismo de un una correa plana en m
              a partir de la ecuación de relación de transmisión:
              
              i = D1/D2

              donde: 
              i = relación de transmisión
              D1 = diametro polea menor
              D2 = diametro polea mayor
              
              valores sugeridos:
              El Diametro D1 de la polea menor es de 150 mm
              El diametro D2 de la polea mayor es de 450 mm
              Solución relación de transmisión es i = 0.333
              """ 
              print(header)
              diametro1 = input("Proporcione el valor del diámetro de la polea menor en mm: ")
              diametro1=float(diametro1)
              diametro2 = input("Proporcione el valor del diámetro de la polea mayor en mm: ")
              diametro2=float(diametro2)

              i =(diametro1)/(diametro2)

              print("""\
              
              El valor del diametro de la motora menor D1 = %.2f mm
              El valor del diametro de la motora mayor D2 = %.2f mm
              La relación de transmisión de velocidad es i = %.2f 
              """ %(diametro1, diametro2, i))
              
           elif opcionMenu == "iia":
                print ("Seleccionó iia")
                header = """Simulacion del calculo de la velocidad que gira el eje conducido
                de correa plana en rpm
                a partir de la ecuacion de las velocidades:
                (D1) * (N1) = (D2)* (N2)
                
                se despeja N2 de la ecuacion anterior:

                N2 = (N1)*(D1)/(D2)
                
                D1 diametro polea menor
                N1 velocidad giro inicial
                D2 diametro polea mayor
                N2 velocidad giro conducido
                
                valores sugeridos: 
                El Diametro D1 de la polea menor es de 150 mm
                La velocidad de giro inicial N1 de la polea menor es de 1200 rpm
                El diametro D2 de la polea mayor es de 450 mm
                Solución velocidad que gira el eje conducido  N2 = es 400 rpm

               """
                print(header)
                diametro1 = input("Proporcione el valor del diámetro de la polea menor en mm: ")
                diametro1=float(diametro1)
                N1=input("Proporcione el valor del eje inicial en rpm: ")
                N1=float(N1)
                diametro2 = input("Proporcione el valor del diámetro de la polea mayor en mm: ")
                diametro2=float(diametro2)
                
         
                N2 =(diametro1)*(N1)/(diametro2)
                
                print("""\
                
                El valor del diametro de la motora menor D1 = %.2f mm
                El valor de la velocidad de giro inicial es N1 = %.2f rpm
                El valor del diametro de la motora mayor D2 = %.2f mm
                El resultado de la velocidad que gira el eje conducido es N2 = %.2f rpm
                """ %(diametro1, N1, diametro2, N2))
           
           elif opcionMenu == "iiia":
                print ("Seleccionó iiia")
                import math
                header = """Simulacion del calculo de la longitud de la correa que se necesita en mm
                a partir de la ecuacion de longitud:

                L = π*(L1 + L2) + 2*(math.sqrt((L3)**2 + (L1 - L2)**2))

                donde:
                L longitud de la correa, 
                L1 semicircunferencia de la polea conducida, 
                L2 semicircunferencia de la polea conductora, 
                L3 distancia entre los ejes de las poleas,
                
                Valores sugeridos:
                La semicircunferencia de la polea conducida es de L1 = 225 mm
                La semicircunferencia de la polea conductora es de L2 = 75 mm
                La distancia entre los ejes de las poleas es de L3 = 600 mm
                Solucion de la longitud de la correa L = 2179.41 mm
                """ 
                print(header)
                longitud1= input("Proporcione el valor de la semicircunferencia de la polea conducida en mm:  ")
                longitud1=float(longitud1)
                longitud2= input("Proporcione el valor de la semicircunferencia de la polea conductora en mm: ")
                longitud2=float(longitud2)
                longitud3= input("Proporcione el valor de la distancia entre los ejes de las poleas en mm: ")
                longitud3=float(longitud3)

                L = math.pi*(longitud1 + longitud2) + 2*(math.sqrt((longitud3)**2 + (longitud1 - longitud2)**2))
                
                print("""\
                
                El valor de la semicircunferencia de la polea conducida es L1  = %.2f mm
                El valor de la semicircunferencia de la polea conductora es  L2 = %.2f mm
                El valor de la distancia entre los ejes de las poleas es  L3 = %.2f mm
                El resultado de la longitud de la correa es L = %.2f mm
                """%(longitud1, longitud2, longitud3, L))

           elif opcionMenu =="q":
              print ("Seleccionó q")
              break


   

   elif opcionMenu == "b":
       print ("Seleccionó b")
       import math
       header = """Simulacion del cálculo de Tren de poleas

       
       """
       menuItems = np.array(["1","2","3","4","5","q"])
       while True:
           menu()
           opcionMenu = input("""Escriba el número de la opción de Tren de poleas o q para salir del mecanismo de Tren de poleas """)
           if opcionMenu == "1":
              print ("Seleccionó 1")
              header = """Simulación del cálculo de relación de transmisión del mecanismo de un tren de poleas constituido por tres escalonamientos en mm a partir de la ecuación de relación de transmisión, donde:
              i relación de transmisión,
              D1 diámetro polea motora 1,
              D2 diámetro polea conducida 2,
              D3 diámetro polea motora 3,
              D4 diámetro polea conducida 4,
              D5 diámetro polea motora 5,
              D6 diámetro polea conducida 6,

              Valores sugeridos:
              El diámetro D1 de la polea motora 1 es de 10 mm
              El diámetro D2 de la polea conducida 2 es de 40 mm
              El diámetro D3 de la polea motora 3 es de 20 mm
              El diámetro D4 de la polea conducida 4 es de 50 mm
              El diámetro D5 de la polea motora 5 es de 30 mm
              El diámetro D6 de la polea conducida 6 es de 60 mm
              Solución relación de transmisión del mecanismo i= 0.05 

              
              """ 
              print(header)
              diametro1 = input("Proporcione el valor del diámetro de la polea motora 1 en mm: ")
              diametro1=float(diametro1)
              diametro2 = input("Proporcione el valor del diámetro de la polea conducida 2 en mm: ")
              diametro2=float(diametro2)
              diametro3 = input("Proporcione el valor del diámetro de la polea motora 3 en mm: ")
              diametro3=float(diametro3)
              diametro4 = input("Proporcione el valor del diámetro de la polea conducida 4 en mm: ")
              diametro4=float(diametro4)
              diametro5 = input("Proporcione el valor del diámetro de la polea motora 5 en mm: ")
              diametro5=float(diametro5)
              diametro6 = input("Proporcione el valor del diámetro de la polea conducida 6 en mm: ")
              diametro6=float(diametro6)

              i =(diametro1*diametro3*diametro5)/(diametro2*diametro4*diametro6)
              print("""\
              
              El valor del diámetro de la polea motora 1 es= %.2f mm
              El valor del diámetro de la polea conducida 2 es = %.2f mm
              El valor del diámetro de la polea motora 3 es= %.2f cm
              El valor del diámetro de la polea conducida 4 es = %.2f mm
              El valor del diámetro de la polea motora 5 es= %.2f mm
              El valor del diámetro de la polea conducida 6 es = %.2f mm
              La relación de transmisión del mecanismo es: %.2f
              """ %(diametro1, diametro2,diametro3, diametro4,diametro5, diametro6, i))
              
           elif opcionMenu == "2":
                print ("Seleccionó 2")
                header = """Simulación del cálculo de la velocidad del eje de salida de un tren de poleas constituido por tres escalonamientos en mm a partir de la ecuación de relación de transmisión, donde:
                i relación de transmisión,
                N6 velocidad del eje de salida 6,
                N1 velocidad de la rueda de motora 1,
                         
                Valores sugeridos:
                La relación de transmisión del mecanismo i= 0.05
                La velocidad N1 de la rueda de motora 1 es de 3000 RPM
                Solución velocidad N6 del eje de salida 6 es de 150 RPM
         
                
                """ 
                print(header)
                i = input("Proporcione el valor de la relación de transmisión del mecanismo: ")
                i = float(i)
                velocidadN1 = input("Proporcione la velocidad de la rueda motora 1 en RPM: ")
                velocidadN1=float(velocidadN1)
                
         
                VelocidadN6 =(i * velocidadN1)
                print("""\
                
                La relación de transmisión del mecanismo es: %.2f
                La velocidad N1 de la rueda de motora 1 es de = %.2f mm
                La velocidad N6 del eje de salida 6 es de: %.2f
                """ %(i, velocidadN1, VelocidadN6))
           
           elif opcionMenu == "3":
                print ("Seleccionó 3")
                header = """Simulación del cálculo de la velocidad del último árbol de un tren de poleas constituido por tres escalonamientos en mm a partir de la ecuación de la relación de transmisión y regimen del funcionamiento del motor, donde:
                D1 diámetro polea motora 1,
                D2 diámetro polea conducida 2,
                D3 diámetro polea motora 3,
                D4 diámetro polea conducida 4,
                D5 diámetro polea motora 5,
                D6 diámetro polea conducida 6,
                N1 velocidad del árbol motor 1,
                N6 velocidad del último árbol 6,

                Valores sugeridos:
                El diámetro D1 de la polea motora 1 es de 150 mm
                El diámetro D2 de la polea conducida 2 es de 300 mm
                El diámetro D3 de la polea motora 3 es de 150 mm
                El diámetro D4 de la polea conducida 4 es de 300 mm
                El diámetro D5 de la polea motora 5 es de 150 mm
                El diámetro D6 de la polea conducida 6 es de 300 mm
                La relación de transmisión del mecanismo es de i= 0.125
                La velocidad del árbol motor N1 es de 1000 RPM
                Solución velocidad del último árbol N6 es de 125 RPM

                
                """ 
                print(header)
                diametro1 = input("Proporcione el valor del diámetro de la polea motora D1 en mm: ")
                diametro1=float(diametro1)
                diametro2 = input("Proporcione el valor del diámetro de la polea conducida 2 en mm: ")
                diametro2=float(diametro2)
                diametro3 = input("Proporcione el valor del diámetro de la polea motora 3 en mm: ")
                diametro3=float(diametro3)
                diametro4 = input("Proporcione el valor del diámetro de la polea conducida 4 en mm: ")
                diametro4=float(diametro4)
                diametro5 = input("Proporcione el valor del diámetro de la polea motora 5 en mm: ")
                diametro5=float(diametro5)
                diametro6 = input("Proporcione el valor del diámetro de la polea conducida 6 en mm: ")
                diametro6=float(diametro6)
                velocidadN1 = input("Proporcione la velocidad del árbol motriz N1 en RPM: ")
                velocidadN1=float(velocidadN1)

                i =(diametro1*diametro3*diametro5)/(diametro2*diametro4*diametro6)
                VelocidadN6=i*velocidadN1
                print("""\
                
                El valor del diámetro de la polea motora 1 es= %.2f mm
                El valor del diámetro de la polea conducida 2 es = %.2f mm
                El valor del diámetro de la polea motora 3 es= %.2f cm
                El valor del diámetro de la polea conducida 4 es = %.2f mm
                El valor del diámetro de la polea motora 5 es= %.2f mm
                El valor del diámetro de la polea conducida 6 es = %.2f mm
                La relación de transmisión del mecanismo es: %.3f
                La velocidad del árbol motriz N1 es de = %.2f RPM
                La velocidad del último árbol N6 es de = %.2f RPM
                """ %(diametro1, diametro2,diametro3, diametro4,diametro5, diametro6, i, velocidadN1, VelocidadN6))

           elif opcionMenu == "4":
                print ("Seleccionó 4")
                header = """Simulación del cálculo de la relación de transmisión de velocidad total de un tren de poleas constituido por tres escalonamientos en mm a partir de la ecuación de velocidad del árbol de entrada y velocidad del árbol de salida, donde:
                i relación de transmisión,
                N6 velocidad del árbol de salida 6,
                N1 velocidad del árbol de entrada 1,
                         
                Valores sugeridos: 
                La velocidad N6 del árbol de salida es de 125 RPM
                La velocidad N1 del árbol de entrada es de 1000 RPM
                Solución la relación de transmisión de velocidad total del mecanismo i= 0.125
         
                
                """ 
                print(header)
                velocidadN6 = input("Proporcione la velocidad del árbol de salida 6 en RPM: ")
                velocidadN6=float(velocidadN6)
                velocidadN1 = input("Proporcione la velocidad del árbol de entrada 1 en RPM: ")
                velocidadN1=float(velocidadN1)
                
         
                i =velocidadN6/velocidadN1
                print("""\
                
                La velocidad N6 del árbol de salida 6 es de: %.2f
                La velocidad N1 del árbol de entrada 1 es de = %.2f mm
                La relación de transmisión del mecanismo es: %.3f
                """ %(velocidadN6, velocidadN1, i))

           elif opcionMenu == "5":
                print ("Seleccionó 5")
                header = """Simulación del cálculo del diámetro de la polea de un tren de poleas constituido por tres escalonamientos en mm a partir de la ecuación de diámetro de la polea, donde:
                D diámetro polea que arrastra al eje de la cinta transportadora,
                D1 diámetro polea motora 1,
                D2 diámetro polea conducida 2,
                D3 diámetro polea motora 3,
                N1 velocidad del eje motor 1,
                N4 velocidad de giro de la cinta transportadora,

                Valores sugeridos:
                El diámetro D1 de la polea motora 1 es de 2 mm
                El diámetro D2 de la polea conducida 2 es de 100 mm
                El diámetro D3 de la polea motora 3 es de 8 mm
                La velocidad del eje motor N1 es de 3000 RPM
                La velocidad de giro de la cinta transportadora N4 es de 5 RPM
                Solución diámetro de la polea que arrastra al eje de la cinta transportadora D es de 96 mm

                
                """ 
                print(header)
                diametro1 = input("Proporcione el valor del diámetro de la polea motora D1 en mm: ")
                diametro1=float(diametro1)
                diametro2 = input("Proporcione el valor del diámetro de la polea conducida 2 en mm: ")
                diametro2=float(diametro2)
                diametro3 = input("Proporcione el valor del diámetro de la polea motora 3 en mm: ")
                diametro3=float(diametro3)
                velocidadN1 = input("Proporcione la velocidad del eje motor N1 en RPM: ")
                velocidadN1=float(velocidadN1)
                velocidadN4 = input("Proporcione la velocidad de giro de la cinta transportadora N4 en RPM: ")
                velocidadN4=float(velocidadN4)

                
                D= (velocidadN1*diametro1*diametro3)/(diametro2*velocidadN4)

                print("""\
                
                El valor del diámetro de la polea motora 1 es= %.2f mm
                El valor del diámetro de la polea conducida 2 es = %.2f mm
                El valor del diámetro de la polea motora 3 es= %.2f cm
                La velocidad del árbol motriz N1 es de = %.2f RPM
                La velocidad del último árbol N4 es de = %.2f RPM
                El valor del diámetro D de la polea que arrastra al eje de la cinta transportadora es = %.2f mm
                """ %(diametro1, diametro2, diametro3, velocidadN1, velocidadN4, D))

           elif opcionMenu == "q":
               print ("Seleccionó q")
               break


   elif opcionMenu == "c":
      print ("selecciono c")
      import math
      header = """Simulacion del calculo de la potencia nominal del
      sistema por correa a partir de la ecuacion
      L longitud de la correa, R1 radio de la polea mayor, r1 radio de la  polea menor
      valores sugeridos: La longitud L de la correa es de 1.444 m
      El Radio R de la polea mayor es de 0.14 m
      El radio r de la polea menor es de 0.06 m
      Solución distancia entre los centros de las poleas C= 0.4 m


      """
      print(header)
      longitud=input("Proporcione el valor de la Longitud de la correa en m: ")
      longitud=float(longitud)
      polea_mayor = input("Proporcione la dimensión del diámetro de la polea mayor en m: ")
      polea_mayor=float(polea_mayor)
      polea_menor = input("Proporcione la dimensión del diámetro de la polea menor en m: ")
      polea_menor=float(polea_menor)

      Dp=(2*polea_mayor)
      dp=(2*polea_menor)
      rel_diam=((Dp/dp))
      r=(1800/1000)
      ksr=float(rel_diam)
      pnc=(dp*r)*(1004-(1652/dp)-(0.1547*math.pow(dp*r,2))-(0.2126*math.log(dp*r)))+((1652*r)*1-(1/ksr))

      print("""\
      El valor de la longitud de la correa: = %.2f m
      El valor del diametro de la polea mayor: = %.2f m
      El valor del diametro de la polea menor es: = %.2f m
      El valor de Ksr es de: %.2f m
      El valor de la potencia nominal es: %.2f m
      """ %(longitud, polea_mayor, polea_menor, ksr,pnc))
     

   elif opcionMenu == "d":
      print ("selecciono d")


      menuItems = np.array(["id","iid","iiid", "ivd", "vd","q"])
      while True:
           menu()
           opcionMenu = input("""Escriba el número de la opción de Tren de engranajes simple o q para salir del mecanismo
de tren de engranajes simple """)
           if opcionMenu == "id":
              print ("Seleccionó id")
              import math
              import matplotlib.pyplot as plt
              import matplotlib.image as mpimg
                
              header = """Simulación del cálculo de relación de transmisión del mecanismo de un Tren de engranajes simple constituido por tres escalonamientos en mm
              a partir de la ecuación de relación de transmisión:
              
              i = z1*z3*z5 / z2*z4*z6
              
              donde: 
              i = relación de transmisión
              z1 = número entero 1
              z2 = número entero 2
              z3 = número entero 3
              z4 = número entero 4
              z5 = número entero 5
              z6 = número entero 6
              
              valores sugeridos:
              El número entero del engranaje de entrada z1 es de 150 mm
              El número entero del engranaje de salida z2 es de 450 mm
              El número entero del engranaje de entrada z3 es de 200 mm
              El número entero del engranaje de salida z4 es de 400 mm
              El número entero del engranaje de entrada z5 es de 100 mm
              El número entero del engranaje de salida z6 es de 300 mm
              Solución relación de transmisión es i = 0.055
              """ 
              print(header)
              número1 = input("Proporcione el valor del número entero del engranaje de entrada z1 en mm: ")
              número1 =float(número1)
              
              número2 = input("Proporcione el valor del número entero del engranaje de salida z2 en mm: ")
              número2 =float(número2)
              
              número3 = input("Proporcione el valor del número entero del engranaje de entrada z3 en mm: ")
              número3 =float(número3)
              
              número4 = input("Proporcione el valor del número entero del engranaje de salida z4 en mm: ")
              número4 =float(número4)
              
              número5 = input("Proporcione el valor del número entero del engranaje de entrada z5 en mm: ")
              número5 =float(número5)
              
              número6 = input("Proporcione el valor del número entero del engranaje de salida z6 en mm: ")
              número6 =float(número6)


              i =(número1*número3*número5)/(número2*número4*número6)
              
              print("""\   
              El valor del número entero del engranaje de entrada z1 = %.2f mm
              El valor del número entero del engranaje de salida z2 = %.2f mm
              El valor del número entero del engranaje de entrada z3 = %.2f mm
              El valor del número entero del engranaje de salida z4 = %.2f mm
              El valor del número entero del engranaje de entrada z5 = %.2f mm
              El valor del número entero del engranaje de salida z6 = %.2f mm
              La relación de transmisión es i = %.2f
              """ %(número1, número2, número3, número4, número5, número6, i))


              img = mpimg.imread('Trenengranajessimple.png')
              imgplot = plt.imshow(img)
              plt.show()


           elif opcionMenu == "q":
               print ("Seleccionó q")
               break

            
           elif opcionMenu == "iid":
                print ("Seleccionó iid")
                import math
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                
                header = """Simulación del cálculo de la velocidad del eje de salida de un Tren de engranajes simple
constituido por tres escalonamientos en mm

               a partir de la ecuación de relación de transmisión, donde:

                i = relación de transmisión,
                Ns = velocidad del eje de salida,
                Ne = velocidad de la rueda de entrada,

                Valores sugeridos:
                La relación de transmisión del mecanismo i = 18 
                La velocidad Ne de la rueda de entrada es de 2000 RPM
                Solución velocidad Ns del eje de salida es de 111.11 RPM
                """

                print(header)
                i = input("Proporcione el valor de la relación de transmisión del mecanismo: ")
                i = float(i)
                velocidadN1 = input("Proporcione la velocidad Ne del eje de entrada en RPM: ")
                velocidadN1=float(velocidadN1)

                velocidadN2 =(velocidadN1)/(i)

                print("""\
                
                La relación de transmisión del mecanismo es: %.2f
                La velocidad N1 de la rueda de entrada es de = %.2f rpm
                La velocidad N2 del eje de salida es de: %.2f rpm
                """ %(i, velocidadN1, velocidadN2))

                
                img = mpimg.imread('Trenengranajessimple.png')
                imgplot = plt.imshow(img)
                plt.show()
                
           elif opcionMenu == "q":
               print ("Seleccionó q")
               break

            
           elif opcionMenu == "iiid":
                print ("Seleccionó iiid")
                import math
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                
                header = """Simulación del cálculo de Velocidad de giro de un tren de engranajes formado por engranajes
                en rpm

               a partir de la ecuación:

                i = Z1/Z3

                i = n2/n1

                Se despeja n2 de la ecuacion anterior:

                n2 = i * n1
                

                donde:
                i relación de transmisión,
                Z1 número de dientes rueda motriz
                Z3 número de dientes rueda conducida
                n1 velocidad del eje de entrada del primer engranaje en RPM,
                n2 velocidad del eje conducido del tercer engranaje en RPM,
      

                Valores sugeridos:
                El número de dientes Z1 del engranaje de entrada 1 es de 90,
                El número de dientes Z3 del engranaje conducida 3 es de 180,
                La relación de transmisión del mecanismo i= 90/180 = 1/2 
                La velocidad del eje de entrada n1 es de 400 RPM,
                Solución de la velocidad de giro del tecer engranaje es de 200 rpm,

                
                """ 
                print(header)

                dientesZ1 = input("Proporcione el número de dientes Z1 del engranaje de entrada 1: ")
                dientesZ1=float(dientesZ1)
                dientesZ3 = input("Proporcione el número de dientes Z3 del engranaje conducida 3: ")
                dientesZ3 =float(dientesZ3)

                velocidadn1 = input("Proporcione el valor de la velocidad del eje de entrada N1 en RPM: ")
                velocidadn1=float(velocidadn1)

                
                i = dientesZ1/dientesZ3
                n2 = i * velocidadn1
                
                
                
                print("""\

                El número de dientes Z1 del engranaje de entrada 1 es = %.2f dientes
                El número de dientes Z3 del engranaje conducida 3 es = %.2f dientes
                La relación de transmisión del mecanismo es i = %.2f
                La velocidad del eje de entrada n1 es = %.2f RPM
                Solución de la velocidad de giro del tecer engranaje es n2 = %.2f RPM
                
                           
                """ %(dientesZ1, dientesZ3, i, velocidadn1, n2))

                img = mpimg.imread('tren de engranajes.png')
                imgplot = plt.imshow(img)
                plt.show()

                
           elif opcionMenu == "q":
               print ("Seleccionó q")
               break


            
           elif opcionMenu == "ivd":
                print ("Seleccionó ivd")
                import math
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                
                
                header = """Simulación del cálculo del número de dientes de las ruedas conducidas de un tren de engranajes en mm 
a partir de la ecuación de la relación de transmisión, 

                i = N2 / N1 = Z1 / Z2 = (Z1*Z3)/(Z2*Z4) = (Z1*Z3)/(Z) 

                donde:
                i relación de transmisión,
                N1 velocidad del eje de entrada en RPM,
                N2 velocidad del eje de salida en RPM,
                Z1 número de dientes del engranaje de entrada 1,
                Z3 número de dientes del engranaje de entrada 3,
                Z2 número de dientes del engranaje de salida 2,
                Z4 número de dientes del engranaje de salida 4,
                Z número de dientes del engranaje de salida,


                Valores sugeridos:
                La velocidad del eje de entrada N1 es de 2500 RPM,
                La velocidad del eje de salida N2 es de 200 RPM,
                El número de dientes Z1 del engranaje de entrada 1 es de 10,
                El número de dientes Z3 del engranaje de entrada 3 es de 20,
                La relación de transmisión del mecanismo i= 200/2500 = 2/25 = 0.08 
                Solución el número de dientes Z del engranaje de salida Z2 y Z4 es de 50,

                
                """ 
                print(header)
                velocidadN1 = input("Proporcione el valor de la velocidad del eje de entrada N1 en RPM: ")
                velocidadN1=float(velocidadN1)
                velocidadN2 = input("Proporcione el valor de la velocidad del eje de salida N2 en RPM: ")
                velocidadN2=float(velocidadN2)
                dientesZ1 = input("Proporcione el número de dientes Z1 del engranaje de entrada 1: ")
                dientesZ1=float(dientesZ1)
                dientesZ3 = input("Proporcione el número de dientes Z3 del engranaje de entrada 3: ")
                dientesZ3 =float(dientesZ3)
                i = velocidadN2/velocidadN1
                Z = math.sqrt((dientesZ1*dientesZ3*velocidadN1)/velocidadN2)
                
                
                
                print("""\
            
                La velocidad del eje de entrada N1 es = %.2f RPM
                La velocidad del eje de salida N2 es = %.2f RPM
                El número de dientes Z1 del engranaje de entrada 1 es = %.2f dientes
                El número de dientes Z3 del engranaje de entrada 3 es = %.2f dientes
                La relación de transmisión del mecanismo es: %.2f
                El número de dientes Z de las ruedas conducidas Z2 y Z4 es = %.2f dientes                
                """ %(velocidadN1, velocidadN2, dientesZ1, dientesZ3 , i , Z))

                img = mpimg.imread('Tren_engranes.jpg')
                imgplot = plt.imshow(img)
                plt.show()

           elif opcionMenu == "q":
               print ("Seleccionó q")
               break


            
           elif opcionMenu == "vd":
                print ("Seleccionó vd")
                import math
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                
                header = """Simulación del cálculo de la potencia nominal en transmisión por correa dentada, considerando el
                funcionamiento con carga suave y constante:

                Las formulas involucradas son:
                v=((n1*pb*z1)/60000)*2
                zm=((z1/2)-((pb*z1)/(2*(math.pi*math.pi)*c)*(z2-z1))*3
                kw=(bs/bso)*4
                if zm<6:
                   kz=(1-0.2*(6-zm))*5
                else:
                   kz=5
           
                P=(Kz*Kw*Ta-((bs*m*(v*v))/bso)*((v*0.001)*1)) 

                Especificación de valores:
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
                C = Distancia entre centros de poleas en mm
     
                """ 
                print(header)
                Ta = input("Proporcione el la fuerza maxima admisible en Newtons: ")
                Ta = float(Ta)
                bs = input("Proporcione el valor del ancho de la correa en mm: ")
                bs = float(bs)
                bso = input("Proporcione el valor del ancho de referencia de la correa en mm: ")
                bso = float(bso)
                m = input("Proporcione el valor de la masa de la correa según el ancho de referencia em kg: ")
                m = float(m)
                n1 = input("Proporcione el valor de la frecuencia de rotación en la polea menor en minutos: ")
                n1 = float(n1)
                pb = input("Proporcione el valor del paso de los dientes de la correa y las poleas en mm: ")
                pb = float(pb)
                z1= input("Proporcione el numero de los dientes de la polea menor: ")
                z1= float(z1)
                z2 = input("Proporcione el numero de los dientes de la polea mayor: ")
                z2 = float(z2)
                c = input("Proporcione la distancia entre centros de las poleas en mm: ")
                c = float(c)
                
                v=((n1*pb*z1)/60000)*2
                zm=((z1/2)-((pb*z1)/(2*(math.pi*math.pi)*c))*(z2-z1))*3
                kw=(bs/bso)*4

                if zm<6:
                   kz=(1-0.2*(6-zm))*5
                else:
                  kz=5
                p=(Ta*kz*Ta)-(bs*m*(v*v)/bso)*((v*0.001)*1)
                
                print("""\
             
                El valor del factor del engranaje de los dientes es = %.2f 
                El valor del factor de ancho es = %.2f 
                El valor de la fuerza maxima admisible en la correa es: = %.2f N
                El valor del ancho de la correa es = %.2f mm
                El valor del ancho de referencia para el paso de la correa es: = %.2f mm
                El valor de la masa lineal de la correa es: = %.2f kg
                El valor de la velocidad de la correa es: = %.2f m/s
                El valor de la frecuencia frecuencia de rotación de la polea menor es: = %.2f min
                El valor del paso de los dientes en la correa y poleas es: = %.2f mm
                La cantidad de dientes de la polea menor es: = %.2f 
                La cantidad de dientes de la polea mayor es: = %.2f 
                La cantidad de dientes de l correa engranados con la polea menor es: = %.2f 
                El valor de la distancia entre centros de poleas es: = %.2f mm
                La potencia nominal de la correa es: = %.2f
                """ %(kz,kw,Ta,bs,bso,m,v,n1,pb,z1,z2,zm,c,p))

                img = mpimg.imread('engranajes.png')
                imgplot = plt.imshow(img)
                plt.show()

                   
           elif opcionMenu == "q":
                   print ("Seleccionó q")
                   break
    

   elif opcionMenu == "q":
       print ("selecciono q")
       break
   else:
      print ("no selecciono ")
      print ("no selecciono ")

