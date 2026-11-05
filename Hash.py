#Xander Reardon
#11/05/26
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

def Hash1(key): #simply returns length, not great
    return len(key)

def Hash2(key):#sums up values given to each vowel and non vowels add 7
    hv = 0
    for char in key:
        if char.lower == "a":
            hv += 1
        elif char.lower == "e":
            hv += 2
        elif char.lower == "i":
            hv += 3
        elif char.lower == "o":
            hv += 4
        elif char.lower == "u":
            hv += 5
        elif char.lower == "y":
            hv += 6
        else:
            hv += 7
    return hv



def linked_List_addREV2(key,hash_table,value): #same as orginal linked list function but when I call it I had a smaller hash table to reduce wasted space
    hv = Hash1(key)
    id = hv % len(hash_table) 
    if hash_table[id] ==  None:
        hash_table[id] = [[key,value]]
    elif hash_table[id] in  [key,value]:
        return
    else:
        stats[1] += 1
        hash_table[id].append([key,value])
        

def linked_List_viewREV2(key,hash_table):
    hv = Hash1(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table[id])):
        if hash_table[id][i][0] == key:
            return [hash_table[id][i][1], f"id = {id}, i = {i}"]





def linear_probe_addREV(key,hash_table,value):#same as prevoius linear probe but using improved hash function
    hv = Hash2(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos] == None:
            hash_table[pos] = [key,value]
            break
        elif hash_table[pos][0] == key:
            hash_table[pos] = [key,value]
            break
        else:
            stats[1] += 1

def linear_probe_viewREV(key,hash_table):
    hv = Hash2(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos][0] == key:
                return [hash_table[pos][1], pos]
        else:
            pass
    return "not in there"









def linked_List_addREV(key,hash_table,value): # same as previous linked list method but with improved hash function
    hv = Hash2(key)
    id = hv % len(hash_table) 
    if hash_table[id] ==  None:
        hash_table[id] = [[key,value]]
    elif hash_table[id] in  [key,value]:
        return
    else:
        stats[1] += 1
        hash_table[id].append([key,value])
        

def linked_List_viewREV(key,hash_table):
    hv = Hash2(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table[id])):
        if hash_table[id][i][0] == key:
            return [hash_table[id][i][1], f"id = {id}, i = {i}"  ]


def linear_probe_add(key,hash_table,value): #if you can`t put the value in its hash value place check next until you can 
    hv = Hash1(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos] == None:
            hash_table[pos] = [key,value]
            break
        elif hash_table[pos][0] == key:
            hash_table[pos] = [key,value]
            break
        else:
            stats[1] += 1

def linear_probe_view(key,hash_table):
    hv = Hash1(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table)):
        pos = (id + i) % len(hash_table)
        if hash_table[pos][0] == key:
                return [hash_table[pos][1], pos]
        else:
            pass
    return "not in there"

def linked_List_add(key,hash_table,value): #if you can`t place the its proper hash value place add to a list in that slot
    hv = Hash1(key)
    id = hv % len(hash_table) 
    if hash_table[id] ==  None:
        hash_table[id] = [[key,value]]
    elif hash_table[id] in  [key,value]:
        return
    else:
        stats[1] += 1
        hash_table[id].append([key,value])
        

def linked_List_view(key,hash_table):
    hv = Hash1(key)
    id = hv % len(hash_table)
    for i in range(len(hash_table[id])):
        if hash_table[id][i][0] == key:
            return [hash_table[id][i][1], f"id = {id}, i = {i}"  ]


stats = [0,0,0] #index 0 is wasted space, index 1 is total collsions, index 2 is time

def main():
    title_hash_table_lp = []
    quote_hash_table_lp = []
    title_hash_table_ll = []
    quote_hash_table_ll = []
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
        title_hash_table_ll.append(None)
        quote_hash_table_ll.append(None)


    for i in range(len(movies)):
        #print(Hash1(movies[i].title))
        start = datetime.now()
        linear_probe_add(movies[i].title,title_hash_table_lp,movies[i])
        end = datetime.now()
    stats[2] = end-start
    for i in range(len(title_hash_table_lp)):
        if title_hash_table_lp[i] == None:
            stats[0] += 1
    print("First Hash table")

    print("title as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")
    stats[0] = 0
    stats[1] = 0
    stats[2] = 0
    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linear_probe_add(movies[i].quote,quote_hash_table_lp,movies[i])
            end = datetime.now()
    for i in range(len(quote_hash_table_lp)):
        if quote_hash_table_lp[i] == None:
            stats[0] += 1
    stats[2] = end-start
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")
    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_add(movies[i].title,title_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    print("Second Hash Table")
    for i in range(len(title_hash_table_ll)):
        if title_hash_table_ll[i] == None:
            stats[0] += 1
    print("title as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_add(movies[i].quote,quote_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    for i in range(len(quote_hash_table_ll)):
        if quote_hash_table_ll[i] == None:
            stats[0] += 1
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    title_hash_table_lp = []
    quote_hash_table_lp = []
    title_hash_table_ll = []
    quote_hash_table_ll = []

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
        title_hash_table_lp.append(None)
        quote_hash_table_lp.append(None)
        title_hash_table_ll.append(None)
        quote_hash_table_ll.append(None)

    for i in range(len(movies)):
        #print(Hash1(movies[i].title))
        start = datetime.now()
        linear_probe_addREV(movies[i].title,title_hash_table_lp,movies[i])
        end = datetime.now()
    stats[2] = end-start
    for i in range(len(title_hash_table_lp)):
        if title_hash_table_lp[i] == None:
            stats[0] += 1
    print("Third Hash table")

    print("title as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")
    stats[0] = 0
    stats[1] = 0
    stats[2] = 0
    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linear_probe_addREV(movies[i].quote,quote_hash_table_lp,movies[i])
            end = datetime.now()
    for i in range(len(quote_hash_table_lp)):
        if quote_hash_table_lp[i] == None:
            stats[0] += 1
    stats[2] = end-start
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")
    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_addREV(movies[i].title,title_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    print("Fourth Hash Table")
    for i in range(len(title_hash_table_ll)):
        if title_hash_table_ll[i] == None:
            stats[0] += 1
    print("title as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_addREV(movies[i].quote,quote_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    for i in range(len(quote_hash_table_ll)):
        if quote_hash_table_ll[i] == None:
            stats[0] += 1
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    title_hash_table_lp = []
    quote_hash_table_lp = []
    title_hash_table_ll = []
    quote_hash_table_ll = []

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)//4):

        title_hash_table_ll.append(None)
        quote_hash_table_ll.append(None)

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_addREV2(movies[i].title,title_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    print("Fifth Hash Table")
    for i in range(len(title_hash_table_ll)):
        if title_hash_table_ll[i] == None:
            stats[0] += 1
    print("title as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0

    for i in range(len(movies)):
            #print(Hash1(movies[i].title))
            start = datetime.now()
            linked_List_addREV2(movies[i].quote,quote_hash_table_ll,movies[i])
            end = datetime.now()
    stats[2] = end-start
    for i in range(len(quote_hash_table_ll)):
        if quote_hash_table_ll[i] == None:
            stats[0] += 1
    print("quote as key")
    print(f"wasted space = {stats[0]}, collisions = {stats[1]}, time taken = {stats[2]}")

    title_hash_table_lp = []
    quote_hash_table_lp = []
    title_hash_table_ll = []
    quote_hash_table_ll = []

    stats[0] = 0
    stats[1] = 0
    stats[2] = 0





    

    
main()
