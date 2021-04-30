import requests
from file_stream import save_data

def connect_api(movie):
    r = requests.get('http://www.omdbapi.com/',
            params = {
                'apikey': '44a04946',
                't': movie
            }
    )
    return r.json()

def connect_api_movies(movies):
    movie_data = []
    for movie in movies:
        r = connect_api(movie)
        movie_data.append(r)
        
    save_data(movie_data)
    
    