from datetime import datetime

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

    def __str__(self):
        return "" + self.title

def Hash(key):
    return Hash1(key)
def Hash1(key):
    return len(key)
def Hash2(key):
    pass
def Hash3(key):
    pass
def Hash4(key):
    pass
def Hash5(key):
    pass

def linear_probe_add(key,hash_table,value):
    hv = Hash(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos] == None:
            hash_table[pos] = [key,value]
            break
        else:
            stats[1] += 1

def linear_probe_view(key,hash_table):
    hv = Hash(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos][0] == key:
                return [hash_table[pos][1], pos]
                break
        else:
            pass
def linked_List_add(key,hash_table,hash_size):
    pass

title_hash_table_lp = []
quote_hash_table_lp = []
hash_table_ll = []
stats = [0,0,0] #index 0 is wasted space, index 1 is total collsions, index 2 is time

def main():

    movies = []
    with open('MOCK_DATA.csv', 'r',encoding="utf-8") as file:
        file.readline()
        temp_movies = file.readlines()
    #print(temp_movies)
    for movie in temp_movies:
        movie = movie.split(",")
        movies.append(Film(movie[0],movie[1],movie[2],movie[3],movie[4],movie[5],movie[6],movie[7],movie[8])) 



    for i in range(len(movies)):
        #print(movies[i])
        title_hash_table_lp.append(None)
        quote_hash_table_lp.append(None)
        hash_table_ll.append([])


    for i in range(len(movies)):
        #print(Hash1(movies[i].title))
        start = datetime.now()
        linear_probe_add(movies[i].title,title_hash_table_lp,movies[i].quote)
        end = datetime.now()
    stats[2] = end-start
   
    print("title as key")
    print(f"wasted space = {stats[0]}, collisons = {stats[1]}, time taken = {stats[2]}")
    stats[0] = 0
    stats[1] = 0
    stats[2] = 0
    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linear_probe_add(movies[i].quote,quote_hash_table_lp,movies[i].title)
            end = datetime.now()
    stats[2] = end-start
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisons = {stats[1]}, time taken = {stats[2]}")
    #print(hash_table_lp)
    #print(linear_probe_view('Conspiracy',hash_table_lp))
    #print(hash_table_lp[13199])

    

    
main()