#importamos las librerias requeridas
import pandas as pd
from fastapi import FastAPI 
import ast
import locale
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.utils.extmath import randomized_svd
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI(title='Proyecto Individual',
              description='Data 10',
            )


@app.get('/')
async def read_root():
    return {'Mi primer API'}



@app.get('/')
async def index():
    return{'API hecho por Juan Alfaro'}

@app.get('/about/')
async def about():
    return {'Proyecto Individual de la cohorte 10 de Data Science'}

df = pd.read_csv("./movies.csv",encoding='utf-8')

# El Vectorizador TfidfVectorizer con parámetros de reduccion procesamiento
df['genres'].fillna('', inplace=True)
vectorizar = TfidfVectorizer(min_df=10, max_df=0.5, ngram_range=(1,2))

# Vectorizamos, ajustamos y transformamos el texto de la columna "title" del DataFrame
X = vectorizar.fit_transform(df['genres'])

# Calcular la matriz de similitud de coseno con una matriz reducida de 7000
similarity_matrix = cosine_similarity(X[:1250,:])

# Obtenemos la descomposición en valores singulares aleatoria de la matriz de similitud de coseno con 10 componentes
n_components = 10
U, Sigma, VT = randomized_svd(similarity_matrix, n_components=n_components)

# Construir la matriz reducida de similitud de coseno
reduced_similarity_matrix = U.dot(np.diag(Sigma)).dot(VT)



@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    mes = mes.lower().strip()
    cantidad = len(df.loc[df['month'] == mes, 'title'])
    return {'mes':mes,'cantidad':cantidad}

@app.get('/peliculas_dis/{dia}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    dia = dia.lower().strip()
    cantidad = len(df.loc[df['day'] == dia, 'title'])
    return {'dia':dia, 'cantidad':cantidad}

@app.get('/franquicia/{franquiciax}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    franquicia = franquicia.lower().strip()
    cantidad = len(df.loc[df["belongs_to_collection"] == franquicia])
    ganancia_total = df["revenue"].loc[df["belongs_to_collection"] == franquicia].sum()
    ganancia_promedio = ganancia_total/cantidad
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str): 
    pais = pais.title()
    cantidad = 0
    lista = df["production_countries"]
    for i in range(len(lista)):
        if lista[i] is None:
            continue
        if type(lista[i]) is not list and lista[i] == pais:
            cantidad += 1
        if pais in lista[i]:
            cantidad += 1
    return {'pais':pais, 'cantidad':cantidad}

@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    productora = productora.title()
    ganancia_total = 0
    cantidad = 0
    lista = df["production_companies"]
    for i in range(len(lista)):
        if lista[i] is None:
            continue
        if type(lista[i]) is not list and lista[i] == productora:
            cantidad += 1
            ganancia = df["revenue"][i]
            ganancia_total += ganancia
        if productora in lista[i]:
            cantidad += 1
            ganancia = df["revenue"][i]
            ganancia_total += ganancia
    
    
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    pelicula = pelicula.title()
    inversion = sum(df["budget"][df["title"] == pelicula])
    ganancia = sum(df["revenue"][df["title"] == pelicula])
    retorno_dos = sum(df["return"][df["title"] == pelicula])
    year = df["release_year"][df["title"] == pelicula].item()
    return {'pelicula':pelicula,'inversion':inversion,'ganancia':ganancia,'retorno':retorno_dos,'anio':year}

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    titulo = titulo.title()
    #Ubicamos el indice del titulo pasado como parametro en la columna 'title' del dts user_item
    indice = np.where(df['title'] == titulo)[0][0]
    #Vemos los indices de aquellas puntuaciones y caracteristicas similares hacia el titulo 
    puntuaciones_similitud = reduced_similarity_matrix[indice,:]
    # Se ordena los indicies de menor a mayor
    puntuacion_ordenada = np.argsort(puntuaciones_similitud)[::-1]
    # Que solo 5 nos indique 
    top_indices = puntuacion_ordenada[:5]
    
    return df.loc[top_indices, 'title'].tolist()
   