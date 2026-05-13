# task 8-6 city names
def city_country(city, country):
    return (city + ", " + country).title()


print(city_country("kyiv", "ukraine"))
print(city_country(city="tokyo", country="japan"))


# task 8-7 album
def make_album(musician_name, album_name):
    album_info = {"musician_name": musician_name, "album_name": album_name}
    return album_info


print(make_album("The Beatles", "Abbey Road"))
print(make_album(musician_name="Queen", album_name="A Night at the Opera"))


def make_album(musician_name, album_name, songs_count=None):
    album_info = {"musician_name": musician_name, "album_name": album_name}
    if songs_count:
        album_info["songs_count"] = songs_count
    return album_info


print(make_album("Coldplay", "A Rush of Blood to the Head", 11))

# task 8-8
while True:
    print("\nEnter the name of the artist or band and the album title:")
    print('(enter "q" at any time to quit)')
    artist_name = input("Artist/Band: ")
    if artist_name == "q":
        break
    album_title = input("Album Title: ")
    if album_title == "q":
        break

    album_info = make_album(artist_name, album_title)
    print(album_info)
