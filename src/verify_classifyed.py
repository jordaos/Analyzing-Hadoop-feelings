import sys
import os
import os.path

PRIMARY_CLASSIFICATION_PATH = sys.argv[1]
SECOND_CLASSIFICATION_PATH = sys.argv[2]

def has_in(filename):
    classifications = ['pos', 'neu', 'neg']
    for classification in classifications:
        file_path = "%s%s/%s" % (PRIMARY_CLASSIFICATION_PATH, classification, filename)
        if os.path.exists(file_path):
            os.rename("%s%s" % (SECOND_CLASSIFICATION_PATH, filename), "%s%s/%s" % (SECOND_CLASSIFICATION_PATH, classification, filename))
            break

for filename in os.listdir(SECOND_CLASSIFICATION_PATH):
    has_in(filename)