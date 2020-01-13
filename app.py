import sqlite3
import json
from pathlib import Path
import requests
from waypdf import pdf2text

pdf2text.convert()


# response = requests.get("http://google.com")

# print(response)

# movies = json.loads(Path("movies.json").read_text())

# print(movies)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "insert into Movies values (?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "select * from Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)
