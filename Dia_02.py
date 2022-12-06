# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:19:43 2022

@author: Nestor
"""

import pandas as pd

# Debe estar seteado el chdir
xlsx = pd.ExcelFile( 'Data//Data_Banco.xlsx' ) # Carga todo el spreadsheet
print(xlsx.sheet_names) # Ver hojas del archivo

data_banco = xlsx.parse('Data')
data_banco.head(5)

archivo_xlsx = 'Data//Data_Banco.xlsx' # Ruta al archivo
# OPCION 2
data_banco_xlsx = pd.read_excel(archivo_xlsx, sheet_name = 'Data')
data_banco_xlsx.head(5)


a= 'Hola Mundo'
a

z = "hola mundo" # Crear objeto
z.capitalize() # Usar metodo para letra capital (primera mayuscula)

z= z.capitalize() # Cambiar z
z # mostar z

z.isupper() # TRUE si todos son mayuscula

z.upper() # transforma todo a mayuscula

z.upper().isupper() # Concatenar metodos


a= [2, 4]
a


a = pd.Series([2, 4])
a


lista = [10, 20, 30]
lista

lista[1] # Nótese la forma de indexar
lista[0] 

lista[3] 

lista[1:3] 
lista[0:2] # Mostrar 1ro y 2do elemento
len(lista) # largo del vector

lista3 = ['a', 12, 'c']  # Las listas en Python permiten mezclar tipos de datos
lista3[0]

listaZ = [10, 20, 30, 40, 'a', 'b']

listaZ[3:6]
listaZ[3:7]
listaZ[7]

# Python
lista[1] = 200
lista

lista.append(400)
lista
lista.append(400)
lista

lista.pop(1) #Elimina segundo elemento
lista

lista.remove(400) # Elimina el primer 400 que encuentra
lista

del lista[1] #Elimina segundo elemento
lista

listaZ + [5, 6, 7]
listaZ

lista1 = [10, 20, 30]
lista2 = ['a', 'b', 'c']
lista1.extend(lista2) # Agregar lista2 a lista1
lista1


lista1 = [10, 20, 30]
lista2 = ['a', 'b', 'c']
for i, j in zip(lista1, lista2) :
    print( i, j )
## Intenten con listas de diferente largo
## Python coge el menor tamaño


lista1 = [10, 20, 30]
lista2 = lista1 # nueva variable pero apuntando al mismo objeto
lista1[1] = 200 # Cambiamos la lista1
lista1
lista2

lista1 = [10, 20, 30]
lista2 = list(lista1) # Nuevo objeto
lista1[1] = 200 # Cambiamos la lista1
lista1
lista2

len(lista1)

id(lista1)
help(id)

lista1 = [10, 20, 30]
lista2 = lista1

id(lista1)
id(lista2)


Nombre = ['Ana', 'Berni', 'Carlos']
Edad = [20,19,20]
Ciudad = ['Gye', 'Uio', 'Cue']
df_1= pd.DataFrame({'Nombre': Nombre, 
                    'Edad': Edad, 
                    'Ciudad': Ciudad})
df_1


df_2= pd.DataFrame({
        'Nombre' : ['Ana', 'Berni', 'Carlos'],
        'Edad' : [20,19,20],
        'Ciudad' : ['Gye', 'Uio', 'Cue']
        })
df_2



df_3= pd.DataFrame({
        'Nombre' : ['Ana', 'Berni', 'Carlos'],
        'Edad' : [20,19,20],
        'Ciudad' : ['Gye', 'Uio', 'Cue']
        }, index= ['a', 'b', 'c'])
df_3


df_3.tail(2)

## Visualizar la estructura   
df_3.info()

df_3.rename( columns= {'Nombre':'Name', 
                       'Edad':'Age', 
                       'Ciudad':'City'}) # No cambia el objeto

df_3

df_3.rename( columns= {'Nombre':'Name', 'Edad':'Age', 'Ciudad':'City'},
inplace= True) # Cambia el objeto
df_3

data_banco_xlsx.__class__

data_sucursal = pd.read_excel('Data//Data_Banco.xlsx', 
                              sheet_name = 'Data_Sucursal')
data_sucursal.head()

type(data_sucursal)

data_banco_xlsx.info()







