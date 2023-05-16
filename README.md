# P101_DTS10

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1**</h1>

## **Machine Learning Operations (MLOps)** 
## **Henry's Labs**
### *Por Juanfrank Alfaro (DTS-10)*

## **ESTRUCTURA DEL PROYECTO** :white_circle:

Los principales archivos desarrollados (que en el apartado siguiente se describirán en forma detallada y precisa su contenido, son:
- ETL.ipynb
- EDA.ipynb
- APIS.ipynb
- main.py
## **DESARROLLO DE LA SOLUCIÓN (PROYECTO)** :white_circle:

### **1. Etapa del proceso ETL** :arrow_right:

- Cargamos el archivos csv con la libereria pandas.
- Luego hacemos todo el trabajo ETL(Extract,Transform,Load)
- Pasamos los valores nulos o vacios de 'revenue' con 0 y igualmente lo hacemos con la columna 'budget'.
- Reordenamos el orden de fecha como nos piden al formato '%Y-%m-%d'.
- Separamos el año a una nueva columna que la llamaremos release_year.
- Desanidamos por el valor que queremos necesarios de las columnas 'genres', 'belongs_to_collection', 'production_companies' 'production_countries', 'spoken_languages'
- En una nueva columna que la llamaremos return sacar el resultado de la division entre las columnas revenue y budget.
- Eliminamos las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.
- En una nueva columna tengo que sacar el nombre del mes que tengo en la columna release_date, que lo pondremos en la columna month y igualmente hacemos con los dias de la semana que la pondremos en la columna que llamaremos day.
- En la columna 'day' tengo miércoles y sábado con tildes, le quitaremos las tildes para que nos pueda funcionar.
- En la columna de belongs_to_collection lo pasaremos a todo con minusculas con lower.
- Y por ultimo lo exportamos para hacer las APIS.

### **2. Etapa de desarrollo API** :arrow_right:

- def peliculas_mes(mes): '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente''' return {'mes':mes, 'cantidad':respuesta}

- def peliculas_dia(dia): '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente''' return {'dia':dia, 'cantidad':respuesta}

- def franquicia(franquicia): '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

- def peliculas_pais(pais): '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}

- def productoras(productora): '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron''' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

- def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}

### **3. Etapa del proceso EDA** :arrow_right:

- Ya con la data limpia, se hace si existen outliers con un boxplot.
- Analizar cuantos valores nulos hay por cada columna, lo visualizamos con un gráfico que elaboré.
- Vemos si existe alguna correlación.
. Se aprecia el Top 10 años con mas popularidad, igualmente con Películas con mayor ganancia.
- La relacion entre revenue y budget con un scatter.

### **4. Etapa del Sistema de Recomendación** :arrow_right:
. def recomendacion('titulo'): '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores''' return {'lista recomendada': respuesta}
