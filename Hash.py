
class Film():
    def __init__(self,title,genre,release_date,director,box_office_revenue,rating,duration_minutes,production_company,quote):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.director = director
        self.box_office_revenue = box_office_revenue
        self.rating = rating
        self.duration_minutes = duration_minutes
        self.production_company = production_company
        self.quote = quote



def main():
    movies = []
    with open('MOCK_DATA.csv', 'r',encoding="utf-8") as file:
        file.readline()
        temp_movies = file.readlines()
    print(temp_movies)
    for movie in temp_movies:
        movie = movie.split(",")
        movies.append(Film(movie[0],movie[1],movie[2],movie[3],movie[4],movie[5],movie[6],movie[7],movie[8])) 


    for i in range(len(movies)):
        print(movies[i].title)

    
main()