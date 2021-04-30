def correct_number_format(number: str):
    if number == 'N/A':
        return 0
    number = number.lstrip('$')
    numbers = number.split(',')
    new_number = ''.join(numbers)
    return int(new_number)

def list_title(movies):
    print("List of titles of the saved movies: ")
    print()
    for movie in movies:
        print(movie)

def show_best_rated(movies):
    best_rated_movie = movies[0]
    best_rating = float(movies[0]['imdbRating'])
    for movie in movies:
        if float(movie['imdbRating']) > best_rating:
            best_rated_movie = movie
            best_rating = float(movies[0]['imdbRating'])
    print("\nThe best rated movie:\n")
    print(best_rated_movie['Title'])

def show_highest_gross(movies):
    highest_gross_movie = movies[0]
    highest_gross = correct_number_format(movies[0]['BoxOffice'])
    for movie in movies:
        temp_gross = correct_number_format(movie['BoxOffice'])
        if temp_gross > highest_gross:
            highest_gross_movie = movie
            highest_gross = temp_gross
    print("\nThe highest gross movie:\n")
    print(highest_gross_movie['Title'])
    print(f"Gross: {highest_gross} $")

def show_average_rating(movies):
    n = 0
    suma = 0.0
    for movie in movies:
        print(movie['Title'], float(movie['imdbRating']))
        suma += float(movie['imdbRating'])
        n += 1
    print(suma)
    print("\nThe average rating of movies: \n")   
    print(suma/n)

def show_menu():
    print()
    print("(1) Display list of titles of the saved movies.")
    print("(2) Display the best rated IMDB movie.")
    print("(3) Display the highest-grossing movie.")
    print("(4) Display the average rating.")
    print("(5) Exit")
    print()
    return int(input())
