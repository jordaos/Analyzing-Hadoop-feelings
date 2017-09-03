#coding: utf-8

from os import listdir
from os.path import isfile, join


def is_in(dir, file, cat):
    dir_cat = dir + cat + "/"
    for f in listdir(dir_cat):
        if isfile(join(dir_cat, f)):
            if(f == file):
                return True
    return False


def verify_is(dir, cat, dir2):
    log = open('../data/LOG1.md', 'a')
    texto = ""
    link = "https://github.com/jordaos/Analyzing-Hadoop-feelings/tree/master/raw-data/1_release_hadoop_classified_sentistrength1"
    dir_cat = dir + cat + "/"
    for f in listdir(dir_cat):
        if isfile(join(dir_cat, f)):
            if(is_in(dir2, f, cat) != True):
                categories = ["pos", "neg", "neu"]
                categories.remove(cat)
                for categ in categories:
                    if (is_in(dir2, f, categ) == True):
                        texto += "\n <a href=\"%s/%s/%s\">%s</a> deveria ser \"%s\", mas está em \"%s\"" % (link, cat, f, f, categ, cat)
    log.write(texto)
    log.close()



dir_ver1 = '../raw-data/1_release_hadoop_classified_sentistrength1/'
dir_ver2 = '../raw-data/1_release_hadoop_classified_manual/'

verify_is(dir_ver1, "pos", dir_ver2) # Verificar os positivos
verify_is(dir_ver1, "neg", dir_ver2) # Verificar os negativos
verify_is(dir_ver1, "neu", dir_ver2) # Verificar os neutros