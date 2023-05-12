from fastapi import FastAPI
import pandas as pd
import numpy as np
import ast
import locale
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
        if lista[i] is not list and list[i] == productora:
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

# @app.get('/recomendacion/{titulo}')
# def recomendacion(titulo:str):
#     '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
#     return {'lista recomendada': respuesta}