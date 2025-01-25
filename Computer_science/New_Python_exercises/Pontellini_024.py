from datetime import date

class Film:
    def __init__(self, title: str, director: str, year_of_release: date, genre: str, duration: int, rating: float):
        self.title = title
        self.director = director
        self.year_of_release = year_of_release
        self.genre = genre
        self.duration = duration
        self.rating = rating
    
    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Year of Release: {self.year_of_release}, Genre: {self.genre}, Duration: {self.duration} min, Rating: {self.rating}/10"

class MovieLibrary:
    def __init__(self, list_of_movies: list [Film]):
        self.list_of_movies = list_of_movies

    def add_new_movies(self, movie: 'Film'):
        title = str(input("Enter the title of the movie: "))
        director = str(input("Enter the director of the movie: "))
        year = int(input("Enter the year of release: "))
        month = int(input("Enter the month of release: "))
        day = int(input("Enter the day of release: "))
        year_of_release = date(year, month, day)
        genre = str(input("Enter the genre of the movie: "))
        duration = int(input("Enter the duration of the movie: "))
        rating = float(input("Enter the rating of the movie: "))
        movie = Film(title, director, year_of_release, genre, duration, rating)
        self.list_of_movies.append(movie)

    def search_films_by_title(self):
        if len(self.list_of_movies) == 0:
            print("No movies in the library")
            return
        title = input("\nEnter the title of the movie you are looking for: ")
        for movie in self.list_of_movies:
            if movie.title == title:
                print(movie)
                return
        print("Movie not found")

    def view_all_movies(self):
        if len(self.list_of_movies) == 0:
            print("No movies in the library")
            return
        for movie in self.list_of_movies:
            print(movie)

    def calculate_average(self):
        total = 0
        for movie in self.list_of_movies:
            total += movie.rating
        return total / len(self.list_of_movies)

def main():

    movie_library = MovieLibrary([])

    while True:
        print("\n1. Add new movie")
        print("2. Search movie by title")
        print("3. View all movies")
        print("4. Calculate average rating")
        print("5. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            movie_library.add_new_movies(Film)
        elif choice == 2:
            movie_library.search_films_by_title()
        elif choice == 3:
            movie_library.view_all_movies()
        elif choice == 4:
            print(f"\nThe average rating of the movies is: {movie_library.calculate_average()}")
        elif choice == 5:
            break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()