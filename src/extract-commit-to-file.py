import sqlite3

# Change it!
conn = sqlite3.connect('../raw-data/2_release_hadoop.sqlite')
cursor = conn.cursor()
# lendo os dados
cursor.execute("""
SELECT * FROM commits;
""")

# Change it!
folder_name = "2_release_hadoop"

for linha in cursor.fetchall():
    file = open("../raw-data/%s/%s.txt" % (folder_name, linha[1]), "w")
    file.write(linha[2])
    file.close()
conn.close()