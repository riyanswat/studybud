# # from pathlib import Path

# # BASE_DIR = Path(__file__).resolve().parent.parent
# # print("BASE_DIR:", BASE_DIR)
# # print("BASE_DIR / 'templates':", BASE_DIR / 'templates')


# import sqlite3
# conn = sqlite3.connect("db.sqlite3")
# c = conn.cursor()

# c.execute("SELECT * from auth_group")
# rows = c.fetchall()

# print(rows)


# import random

# names = ["Roman Reigns", "Seth Rollins", "Dean Ambrose", "John Cena",
#          "Kane", "The Undertaker", "Triple H", "Shawn Michaels", "C M Punk"]

# for n in range(len(names)):
#     name = random.choice(names)
#     names.pop(names.index(name))
#     print(name)


# class Matrix:
#     def __init__(self, data):
#         self.data = data

#     def __and__(self, other):
#         # Implement matrix multiplication
#         return f"{self.data} {other}"


# mat = Matrix("Riyan")
# result_matrix = mat & "khan"

# print(result_matrix)
