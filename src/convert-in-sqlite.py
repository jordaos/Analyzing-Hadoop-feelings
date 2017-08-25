import sqlite3
import re

# File containing SentiStrength analysis
# 0: POS | 1: NEG | 2: TEXT | 3: Explanation
ss_analysis = '../raw-data/2_release_hadoop_ss_no_filter.txt'
arq = open(ss_analysis, 'r')
commit_analysis = arq.readline()

# Change it!
conn = sqlite3.connect('../raw-data/2_release_hadoop.sqlite')
# 0: Project | 1: sha | 2: message | 3: date | 4: author_name | 5: author_email
cursor = conn.cursor()
# lendo os dados
cursor.execute("""
SELECT * FROM commits;
""")

# database sentiments configuration
new_db_conn = sqlite3.connect('../data/ss-analysis-second-release-no-filter.sqlite3')
nwc = new_db_conn.cursor()
nwc.execute('''CREATE TABLE IF NOT EXISTS `sentiment` 
                ( `project` TEXT, 
                `sha` TEXT, 
                `Positive` INTEGER, 
                `Negative` INTEGER, 
                `Text` TEXT, 
                `Explanation` TEXT )''')

for linha in cursor.fetchall():
    commit_analysis = arq.readline()
    arr_analysis = re.split(r'\t+', commit_analysis)
    nwc.execute("""
    INSERT INTO sentiment (project, sha, Positive, Negative, Text, Explanation)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (linha[0], linha[1], arr_analysis[0], arr_analysis[1], linha[2], arr_analysis[3]))

new_db_conn.commit()
new_db_conn.close()
conn.close()