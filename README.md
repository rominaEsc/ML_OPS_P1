# PI_01_MLOps_Henry

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">

## Rol a desarrollar:
El rol a desarrollar es el de un Data Scientist que comenzo a trabajar en una start-up que provee servicios de agregación de plataformas de streaming.  
 
## Objetivos:
Realizar un MVP que cumpla con las siguientes etapas:

### Transformaciones
- A partir deLos dataset que se encuentran en https://drive.google.com/drive/folders/1q61TCXfbav8owsnG8ugasCN6GDkinTEm?usp=sharing.
 realizar las siguientes transformaciones:

- Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

- Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

- Los valores nulos del campo release date deben eliminarse.

- De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

- Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

- Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,poster_path y homepage.


_Estas transformaciones y otras se realizaron los archivos 1_etl_movies.ipynb, 2_etl_credits.ipynb, 3_etl_ML.ipynb. Estos crean, en la carpeta data, los datasets a partir del archivo movies_dataset.csv y credists.csv que se encuentran en este drive: _ 

### Desarrollo API:
Crear 6 funciones para los endpoints que se consumirán en la API, que deben tener un decorador por cada una (@app.get(‘/’)).

- def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X

- def cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
                    Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X

- def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
                    Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X

- def votos_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
                    Ejemplo de retorno: La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X

- def get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
                    Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha conseguido un retorno de X con un promedio de X por filmación

- def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.


_Estas funciones se realizaron y probaron en el archivo 6_funciones.ipynb_

### Deployment
Realizar el deployment para poder consumir la API

_Las consultas a la API pueden realizarse en el siguiente link: https://ml-ops-p1.onrender.com/_

### Análisis exploratorio de los datos
Se realizo un analisis de las palabras que se presentaban con mayor frecuencia en el dataset. 
  _Esto puede verse en el archivo 4_eda.ipynb_


### Sistema de recomendación
El sistema consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:
def recomendacion( titulo ): Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.
_ver 5_ML.ipynb_

## Video: 
Realizar un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

El video se encuentra en: https://drive.google.com/drive/folders/1q61TCXfbav8owsnG8ugasCN6GDkinTEm?usp=sharing
 
