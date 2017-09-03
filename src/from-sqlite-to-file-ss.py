import sqlite3
import re
import sys

MODE = 'filter'
if len(sys.argv) > 1:
    MODE = sys.argv[1]

if MODE not in ['filter', 'no-filter']:
    print 'Mode not found'
    sys.exit()

# Change it!
conn = sqlite3.connect('../raw-data/2_release_hadoop.sqlite')
cursor = conn.cursor()
# lendo os dados
cursor.execute("""
SELECT * FROM commits;
""")

def remove_URLs_informations(sentence):
    # Remove URL
    sentence = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', sentence)
    #Remove break lines
    sentence = sentence.replace('\n', ' ')
    #Remove "13f79535-47bb-0310-9956-ffa450edef68" and "git-svn-id"
    to_remove = ['13f79535-47bb-0310-9956-ffa450edef68', 'git-svn-id:']
    phrase = ''
    for word in sentence.split(' '):
        if word not in to_remove:
            phrase += word + ' '
    return phrase

# Change it!
file_name = "2_release_hadoop_ss.txt"
file = open("../raw-data/%s" % (file_name), "w")

for linha in cursor.fetchall():
    if MODE == 'filter':
        file.write(remove_URLs_informations(linha[2]) + '\n')
    elif MODE == 'no-filer':
        file.write(linha[2] + '\n')
file.close()
conn.close()