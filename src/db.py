import sqlite3


def create_db():

    cursor = connection.cursor()

    cursor.execute("create table if not exists ToDos (id integer primary key, text varchar(200))")

    cursor.execute("create table if not exists Music (id integer primary key, name varchar(200), yt_link varchar(100))")

def execute_smth():

    cursor = connection.cursor()
    
    cursor.execute("insert into ToDos (text) values (\"test smth\")")

    connection.commit()


def fill_db():
    
    with open("Db/ToDos_text.txt") as file:
        data = file.read().split("\n")



    cursor = connection.cursor()
    
    query_values = ", ".join([f"(\"{i[0].upper()+i[1:]}\")" for i in data])

    cursor.execute(f"insert into ToDos (text) values {query_values}")

    with open("Db/SongNames.txt") as file:
        song_names = file.read().split("\n")
    
    with open("Db/SongLinks.txt") as file:
        song_links = file.read().split("\n")

    query_values = ", ".join([f"(\"{song_name}\", \"{song_link}\")" for song_name, song_link in zip(song_names, song_links)])

    cursor.execute(f"insert into Music (name, yt_link) values {query_values}")

    connection.commit()

def get_random_todos_text():
    return sqlite3.connect("Db/tg_new_year.db").cursor().execute("select text from ToDos order by random() limit 1").fetchone()[0]

def get_random_music():
    return sqlite3.connect("Db/tg_new_year.db").cursor().execute("select name, yt_link from Music order by random() limit 1").fetchone()

if __name__ == "__main__":
    ...
    # connection = sqlite3.connect("Db/tg_new_year.db")
    # create_db()
    # fill_db()
    # connection.close()

