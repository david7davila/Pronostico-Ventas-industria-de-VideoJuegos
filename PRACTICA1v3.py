import pandas as pd 
import numpy as np
import json
data_frame = pd.read_csv("E:/mineria/unclean_data1.csv")
data_frame #Impre las primeras 5 columNAS
dataMod=data_frame

data_frame.shape
data_frame.dtypes
data_frame.isnull().any()
data_frame.isnull().sum()

dataMod2=dataMod.rename(columns = {'gross':'Ingresos','movie_title':'Titulo','num_critic_for_reviews':'NumeroCriticas','duration':'Duracion','title_year':'Año'})
dataMod2 = dataMod2.fillna(0)
dataMod2.dtypes
Data=pd.DataFrame(dataMod2)
Data['Titulo']=Data['Titulo'].replace('\?ÿ','',regex=True).astype(str)
len(Data.Titulo.unique()) #saber numero d epeliculas
Data2=Data.drop(7,axis = 0 ) #Borro fila con registros repetida

Data2['Año']
#Data['Titulo'].astype("String")
#Data.dtype
#Data['Titulo'].replace(Data['Titulo'][-2:],"")
Data.replace

AÑOS= dataMod2.Año.unique()
#AÑOS
claseAÑO = Data2[Data2['Año']==2015]
claseAÑO
clase_1 = Data2[Data2['Nombre_columna']=='Clase_1']
clase_1_vs_fecha = Data2.loc[Data2.Nombre_columna == 'Clase_1'
].Fecha
m=min(Data2["Ingresos"])
M=max(Data2["Ingresos"])
I=(M-m)/3
Data3=Data2
Data3=Data3.drop(['DIRECTOR_facebook_likes','actor_3_facebook_likes', 'ACTOR_1_facebook_likes',
       'num_voted_users', 'Cast_Total_facebook_likes', 'facenumber_in_poster',
       'num_user_for_reviews', 'budget',  'ACTOR_2_facebook_likes', 'title_year.1'],axis=1)
len(Data3)
imdb_score=[0,0,0]
Count=[0,0,0]
for i in Data3.index:
    if (Data3['Ingresos'][i]<m+I):
        imdb_score[0]=Data3['imdb_score'][i]+imdb_score[0]
        Count[0]=Count[0]+1
    elif (Data3['Ingresos'][i]<m+2*I):
       imdb_score[1]=Data3['imdb_score'][i]+imdb_score[1]
       Count[1]=Count[1]+1
    else :
        imdb_score[2]=Data3['imdb_score'][i]+imdb_score[2]
        Count[2]=Count[2]+1

imdb_score=tuple(imdb_score)/Count


imdb_score


