import re
import numpy as np
import pandas as pd
from time import time
from json import load

# Al cargar todas las hojas de un excel, Pandas agrupa la informacion en un diccionario de dataframes.
# Se guardan los dataframes en una lista y se eliminan las hojas que no poseen datos de pollos.
tic=time()
archivo=list(pd.read_excel('prueba.xlsx', sheet_name=None, header=None).values())
for i in [0,-1]:
    archivo.pop(i)

# Se crea un dataframe base que servirá para replicar los datos de cada pollo.
# Ademas se obtiene informacion de interes como los nombres de las columnas del archivo final
# y los tipos de lesiones que pueden tener los pollos.    
columnas= pd.read_excel('sample.xlsx').columns
datos_base= pd.DataFrame(columns=columnas[:3])
datos_base[datos_base.columns[[0,2]]]=archivo[0].loc[6:,1:2].drop(index=[12,35,36,37,38]).reset_index(drop=True)
indices_lesion=archivo[0].loc[6:,1:2].drop(index=[12,35,36,37,38]).index
tipo_lesion = load(open('aux_data.json'))[0]['tipo lesion']
datos_base[columnas[0]]=datos_base[columnas[0]].apply(lambda x: tipo_lesion[x] if x in tipo_lesion else x)

# Esta funcion permite iterar sobre el archivo(lista de dataframes) y transformar cada elemento(dataframe)
# en el formato buscado
def iterar_archivo(tabla):
    datos=datos_base.copy()
    datos[columnas[1]]=tabla.iloc[2,1].strftime('%d-%m-%Y %H:%M:%S')
    
    d=3
    lista=[]
    for a in np.arange(3,archivo[0].shape[1]-2,6):
        datos[columnas[3]]=tabla.loc[0,a]
        datos[columnas[4]]=re.sub(r'[^0-9]+','',str(tabla.loc[1,a]))
        datos[columnas[5]]=tabla.loc[2,a]
        datos[columnas[6]]=tabla.loc[4,a]
        datos[columnas[7]]=tabla.loc[0,a+3]
        datos[columnas[8]]=tabla.loc[1,a+3]
        datos[columnas[9]]=tabla.loc[2,a+3]
        datos[columnas[10]]=tabla.loc[3,a+3]
        
        for b in np.arange(5):
            datos[columnas[11]]=tabla.loc[indices_lesion,d].values
            datos[columnas[12]]=b+1
            interes=tabla.loc[[37,12,35,38]]
            for c in np.arange(4):
                datos[columnas[c+13]]=interes.iloc[c,d]
            lista.append(datos.copy())
            d+=1
        d+=1
    return pd.concat(lista)

# Se emplea la funcion, se crea la tabla pedida, se llenan datos vacios,
# se ajustan los tipos de datos y por ultimo, se exporta la tabla.
tabla_final=pd.concat(list(map(iterar_archivo,archivo)))
tabla_final.fillna(
    {'lesionPromedio':0,
     'bursometro':0,
     'integridadIntestinal':0,
     'sexoAnimales':'-',
     'condicionHigado':'-'
    },inplace=True)
tabla_final.convert_dtypes().to_csv('ETL.csv',index=False)
toc=time()
print("Tiempo total ETL:",toc-tic)