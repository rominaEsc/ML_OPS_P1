from fastapi import FastAPI
import pandas as pd

app = FastAPI()

estrenos_por_mes = pd.read_csv("data/estrenos_por_mes.csv", sep=",")
estrenos_por_dia = pd.read_csv("data/estrenos_por_dia.csv", sep=",")
movies = pd.read_csv("data/movies_etl.csv", sep=",")
actors = pd.read_csv("data/actors.csv", sep=",")
directors = pd.read_csv("data/directors.csv", sep=",")

# Funciones

# 1

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes( mes ): 
    '''
    Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
    Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X
    '''
    mes = mes.lower()

    if mes == 'setiembre':
        mes = 'septiembre'
    if mes in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']:
        respuesta = estrenos_por_mes[estrenos_por_mes.mes == mes].iloc[0,1]

    else:
        respuesta = 'Ud. ingreso: ' + mes + '. Por favor, ingrese el nombre del mes que desea consultar en español'
    return {'mes':mes, 'cantidad':respuesta}

#2
@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia( dia ): 
    '''
    Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
    Ejemplo de retorno: X cantidad de películas fueron estrenadas en los días X
    '''
    # ver como hacer poara que solo admita strings
    dia = dia.lower()

    if dia in ['miercoles','mièrcoles']:
        dia = 'miércoles'
    
    if dia in ['sabado','sàbado']:
         dia = 'sábado'
    
    if dia in ['lunes','martes','miércoles','jueves', 'viernes', 'sábado', 'domingo']:
        respuesta  = estrenos_por_dia[estrenos_por_dia.dia == dia].iloc[0,1]

    else:
        respuesta = 'Ud. ingreso: ' + dia + '. Por favor, ingrese el nombre del dia que desea consultar en español'
        
    return {'dia':dia, 'cantidad':respuesta}

#3
@app.get('/score_titulo/{titulo}')
def score_titulo( titulo_de_la_filmación ): 

    # REVISAR .str.contains !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    '''
    Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.
    Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X
    '''
    pelis = (
        movies[movies['title']
        .str.contains(titulo_de_la_filmación, case=False)]
        [['title','release_year','popularity']]
        )

    titulos = pelis['title'].tolist()
    anios = pelis['release_year'].tolist()
    popularidad = pelis['popularity'].tolist()


    return {'titulo':titulos, 'anio':anios, 'popularidad':popularidad}

#4
@app.get('/votos_titulo/{titulo}')
def votos_titulo( titulo_de_la_filmación ): 

    # REVISAR .str.contains!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    ''' Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
    Ejemplo de retorno: La película X fue estrenada en el año X. La misma cuenta con un total de X valoraciones, con un promedio de X
    '''
    pelis = (
        movies[movies['title']
        .str.contains(titulo_de_la_filmación, case=False)]
        [['title','release_year','vote_count','vote_average']]
        )

    out = []
    
    for index, row in pelis.iterrows():
        title = row['title']
        release_year = row['release_year']
        vote_count = row['vote_count']
        vote_average = row['vote_average']

        if vote_count < 2000:
            message = "La película {} fue estrenada en {}. La misma no cuenta con las valoraciones suficientes para calcular el valor promedio de las votaciones".format(title, release_year)
        else:    
            message = "La película {} fue estrenada en {}. La misma cuenta con un total de {} valoraciones, con un promedio de {}".format(title, release_year, vote_count,vote_average)
        
        out.append(message)
    
    out= tuple(out)  

    return {out}  


#5
@app.get('/get_actor/{nombre_actor}')
def get_actor( nombre_actor ): 
    '''
    Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno. La definición no deberá considerar directores.
    Ejemplo de retorno: El actor X ha participado de X cantidad de filmaciones, el mismo ha conseguido un retorno de X con un promedio de X por filmación
    '''
    
    id_actor = actors[actors.name == nombre_actor].iloc[0,0]

    df = (
        pd.merge(
            actors[actors['id_actor'] == id_actor],
            movies[['id_movie','title','revenue']],
            on='id_movie', 
            how='inner')
        )
    
    cantidad = df.shape[0] 

    ganancia_total = df.revenue.sum()

    promedio = df.revenue.mean().round(2)

    return {'actor':nombre_actor, 'cantidad_filmaciones':cantidad, 'retorno_total':ganancia_total, 'retorno_promedio':promedio}


#6
@app.get('/get_director/{nombre_director}')
def get_director( nombre_director ): 
    ''' 
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
    '''
    id_director = directors[directors.name == nombre_director].iloc[0,0]

    df = (
        pd.merge(
            directors[directors['id_director'] == id_director],
            movies[['id_movie','title','release_year','revenue','budget','return']],
            on='id_movie', 
            how='inner')
    )
    
    retorno_total_director = df['return'].sum()
    peliculas = df['title'].tolist()
    anios = df['release_year'].tolist()
    retorno_peliculas = df['return'].tolist()
    budget_peliculas = df['budget'].tolist()
    revenue_peliculas = df['revenue'].tolist()

    data = {
        'director':nombre_director, 
        'retorno_total_director':retorno_total_director, 
        'peliculas':peliculas, 
        'anio':anios, 
        'retorno_pelicula':retorno_peliculas, 
        'budget_pelicula':budget_peliculas, 
        'revenue_pelicula':revenue_peliculas}

    return data