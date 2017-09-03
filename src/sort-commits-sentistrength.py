import math
import sqlite3

# Change it!
dir = '../raw-data/2_release_hadoop_classified_ss'
conn = sqlite3.connect('../data/2_release_analysis_ss_filter.sqlite')
# 0: project | 1: sha | 2: positive | 3: negative | 4: text | 5: Explanation
cursor = conn.cursor()
# lendo os dados
cursor.execute("""
SELECT * FROM sentiment;
""")

for linha in cursor.fetchall():
    message = linha[4]
    sha = linha[1]
    pos = math.fabs(linha[2])
    neg = math.fabs(linha[3])
    # print (message + ' | ' + sha + ' | ' + pos + ' ' + neg)

    if pos == neg:
        with open("%s/neu/%s.txt" % (dir, sha), "a") as arq:
            arq.write(message)
            arq.close()
    elif pos > neg:
        with open("%s/pos/%s.txt" % (dir, sha), "a") as arq:
            arq.write(message)
            arq.close()
    else:
        with open("%s/neg/%s.txt" % (dir, sha), "a") as arq:
            arq.write(message)
            arq.close()

