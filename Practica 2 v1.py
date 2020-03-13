import seaborn as sns
import pandas as pd
import matplotlib as plt
%matplotlib inline

reviews = pd.read_csv("C:/Users/iryok/Desktop/mineria/winemag-data_first150k.csv", index_col=0)
reviews.head(3)
Data=pd.DataFrame(reviews)
Data.dtypes
Data['province'].value_counts().head(10).plot.bar()
print(Data)
Data2=Data.rename(columns = {'country':'Pais','points':'Puntaje','price':'Precio','province':'Ciudad'})
Data3=Data2
Data3=Data3.drop(['description', 'designation','region_1', 'region_2', 'variety', 'winery'],axis=1)
Data3.columns
Data3.isnull().any()
Data3.isnull().sum()
Data4 = Data3.dropna(axis=0) #Eliminamos los 5 filas que no contienen pais

Data4['Puntaje'].mean() # El puntaje promedio de todos los vinos es
Data4['Puntaje'].describe()
(Data4['Pais'].value_counts().head(10) / len(Data4)).plot.bar()
Data4['Puntaje'].value_counts().sort_index().plot.bar()

#Pregunta 1. Que representan los datos de la grafica de arriba.

sns.countplot(Data4['Puntaje'])
df = Data4[Data4.Pais.isin(Data4.Pais.value_counts().head(5).index)]

sns.boxplot(
    x='Pais',
    y='Puntaje',
    data=df
)
Data2['province'].value_counts()