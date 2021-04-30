import json

def read_movies(filename):
    movies = []
    with open(filename, 'r') as f:
        temp = f.readlines()
        for movie in temp:
            movies.append(movie.rstrip('\n'))
    return movies

def read_movies_json(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        for d in data:
            d = d.replace("'", '"')     
    return json.loads(data[0])

def save_data(data):
    with open('data.json', 'w') as f:
            f.writelines(json.dumps(data))