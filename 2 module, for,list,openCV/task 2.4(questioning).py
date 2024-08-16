#initialization
films_genre = {
    'Harry Potter':['fantasy'],
    'How to get away with murder':['drama','detective'],
    'Legend of the seaker':['fantasy'],
    'Sherlok':['detective'],
    'Scum\'s Wish':['drama']
    }

#describe types
#хотел бы вместо этого блока использовать что-то вроде genre_films = {[],[]}, но не знаю как это правильно сделать.
genre_films = {}
for j in films_genre.values():
    for k in j:
        genre_films[k]=[]

#initialization
for i, j in films_genre.items():
    for k in j:
        genre_films[k].append(i)
print(genre_films)

#main
print("We have these genres:")
for i in genre_films.keys():
    print(i)
choice=input("What genre do you prefer?\n")
print("I'd recommend you to watch", genre_films[choice])

