# Creando un dataframe
import pandas as pd
diccionario={"columna1":[2,1,2,3,4],"columna2":[4.5.6.7.3]}
data = pd.DataFrame(diccionario)
data = data.astype(float)
print(data)
