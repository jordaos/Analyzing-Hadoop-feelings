import sqlite3
import re
import sys

NUMBER_VERSION = 0
if len(sys.argv) > 1:
    NUMBER_VERSION = int(sys.argv[1])
else:
    print 'Give parameter'
    sys.exit()


# Change it!
conn = sqlite3.connect('../raw-data/%d_release_hadoop.sqlite' % NUMBER_VERSION)
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
file_name = "%d_release_hadoop_ss.txt" % (NUMBER_VERSION)
file = open("../raw-data/%s" % (file_name), "w")

for linha in cursor.fetchall():
    file.write(remove_URLs_informations(linha[2]) + '\n')
file.close()
conn.close()