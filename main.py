from file_stream import read_movies, read_movies_json
from api_handler import connect_api_movies
from consts import FILENAME_READ, FILENAME_DATA
import display
import os
    
def clear_console():
    clear = lambda: os.system('cls')
    clear()

def init_menu():
    print()
    movies = read_movies_json(FILENAME_DATA)
    list_of_titles = read_movies(FILENAME_READ)
    
    while(1):
        option = display.show_menu()
        clear_console()
        if option == 1:
            display.list_title(list_of_titles)
        elif option == 2:
            display.show_best_rated(movies)
        elif option == 3:
            display.show_highest_gross(movies)
        elif option == 4:
            display.show_average_rating(movies)
        elif option == 5:
            break
            
def gather_data():
    movies = read_movies(FILENAME_READ)
    connect_api_movies(movies)


if __name__ == "__main__":
    gather_data()
    init_menu()