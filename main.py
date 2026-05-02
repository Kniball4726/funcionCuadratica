import cmath
import os
import matplotlib.pyplot as plt
import numpy as np

# Funcion para borrar pantalla

def borrarpantalla():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

#Se ingresan datos de las 3 terminos de la funcion a,b,c

print(f"Calculo de la funcion cuadratica de la forma f(x)=ax\u00b2+bx+c\n")
a=float(input("Indique el valor de a:\n"))
b=float(input("Indique el valor de b:\n"))
c=int(input("Indique el valor de c:\n"))

#Se caculan los vertices de x & y 

vx=-(b)/(2*(a))
vy=(a*((vx)**2))+((b)*(vx))+(c)

vx = round(vx.real, 2)
vy = round(vy.real, 2)

canonica= f"f(x)={a}(x-({vx}))^2+({vy})"

#Se determina concavidad, la imagen y los intervalos 

if a > 0:
    concavidad="El conjunto abre hacia arriba"
    imagen = f"[{vy.real:.2f};\u221e)"
    icreci = f"({vx.real:.2f};\u221e)"
    idecre = f"()-\u221e;{vx:.2f})"
else:
    concavidad="El conjunto abre hacia abajo"
    imagen = f"(-\u221e;{vy.real:.2f}]"
    icreci = f"(-\u221e;{vx.real:.2f})"
    idecre = f"({vx.real:.2f};\u221e)"

#Calcula discriminante para determinar raices

d=((b)**2)-(4*(a)*(c))

if d > 0:
    discriminante = ("\nLa discriminante es positiva,\npor lo tanto la funcion tiene 2 raices")
elif d == 0:
    discriminante = ("\nLa discriminante es 0,\n por lo tanto La funcion tiene 1 raiz")
else:
    discriminante = ("\nLa discriminante es negativa,\npor lo tanto la grafica flota en el plano\n")

#Calculo de las raices y los conjuntos con la ecuación resolvente

x1 = (-(b) + cmath.sqrt(d)) / (2*(a))
x2 = (-(b) - cmath.sqrt(d)) / (2*(a))

x1 = round(x1.real, 2)
x2 = round(x2.real, 2)

factorizada= f"f(x) = {a}(x - ({x1}))(x - ({x2}))"

if x1.real > x2.real:
    cpos = f"({x2.real:.2f};{x1.real:.2f})"
    cneg = f"(-\u221e;{x2.real:.2f}) U ({x1.real:.2f};\u221e)"
elif x2.real > x1.real:
    cpos = f"({x1.real:.2f};{x2.real:.2f})"
    cneg = f"(-\u221e;{x1.real:.2f}) U ({x2.real:.2f};\u221e)"
else:
    if a > 0:   
        cpos = f"(-\u221e;\u221e)"
        cneg = f"Conjunto vacio"
    else:
        cpos = f"Conjunto vacio"
        cneg = f"(-\u221e;\u221e)"
a=int(a)
b=int(b)

#Se imprimen todos los resultados
borrarpantalla()
print("-------------------\nPara la función:\n")
print(f"f(x)={a}x\u00b2+{b}x+{c}\n")
print(f"Concavidad: a={a}, {concavidad}\n")
print("Dominio: R\n")
print(f"Imagen: {imagen}\n")
print(f"Ordenadas al origen: (0;{c})\n")
print(f"Vertices: ({vx:.2f};{vy:.2f})\n")
print(f"Eje de simetria: ({vx:.2f})\n")
print(f"Raices: ({x1.real:.2f};{x2.real:.2f})\n")
print(f"Discriminante: ∆ = b\u00b2-4.a.c = {d} {discriminante}\n")
print(f"C+: {cpos}\n")
print(f"C-: {cneg}\n")
print(f"I\u2191: {icreci}\n")
print(f"I\u2193: {idecre}\n")
print(f"Canonica: {canonica}\n")
print(f"Factorizada: {factorizada}\n")
#Grafica de la funcion
x = np.linspace(vx - 10, vx + 10, 200)
y = a * (x ** 2) + b * x + c
plt.figure(figsize=(10, 6))

plt.plot(x, y, label='f(x)={}x\u00b2+{}x+{}'.format(a, b, c))

plt.plot([x1], [0], 'go', color='green', label='Raices')
plt.text(x1, 0 + 0.2, f'({x1}, {0})', 
             fontsize=5, ha='left', fontweight='bold')
plt.plot([x2], [0], 'go', color='green', label='Raices')
plt.text(x2, 0 + 0.2, f'({x2}, {0})', 
             fontsize=5, ha='left', fontweight='bold')
plt.plot([0], [c], 'bo', color='blue', label='Ordenada al origen')
plt.text(0, c + 0.2, f'(0, {c})', 
             fontsize=5, ha='left', fontweight='bold')
plt.axhline(0, color='black', lw=1, ls='--')
plt.axvline(0, color='black', lw=1, ls='--')
plt.scatter([vx], [vy], color='red', label='Vértice')
plt.text(vx, vy + 0.2, f'({vx}, {vy})', 
             fontsize=5, ha='left', fontweight='bold')
plt.title('Gráfica de la función cuadrática')
plt.xlabel('x')
plt.ylabel(f'f(x)={a}x\u00b2+{b}x+{c}')
plt.legend()
plt.grid()
plt.show()

