# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:11:16 2022

@author: Nestor
"""


import os
print(f'Hola, {os.getlogin()}!, ¡¿Listo para empezar?!')

# comentario

5+5 # Expresión con output

5+5; # Expresión sin salida

a = 5+5 # Asigna el valor a la variable "a"


a = 5 # Asignación
a
a = 2*a  # Asignación a mismo objeto
a

a= 2; b= 1; a + b


7 % 3 # Modular
2 ** 3 # 2 elevado al cubo
pow(2, 3) # 2 elevado al cubo


import math

math.factorial(3) # Factorial

math.log(math.exp(2)) # Logaritmo natural


os.getcwd() # Verificar el directorio de trabajo
os.listdir("./")

import pandas as pd
archivo_csv= "Data/Data_Banco.csv" # Ruta al archivo
data_banco_csv = pd.read_csv(archivo_csv, sep = ";") # Notese el sep= ";"

data_banco_csv.head(5) # Mostrar 5 primeras filas del DataFrame












