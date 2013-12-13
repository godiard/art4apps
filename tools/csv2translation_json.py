#!/usr/bin/env python

# convert a csv file to a json structured data
# with information about the translation to a specific language
# the csv have the following format:
# english_word,category,translated_word,image

import os
import sys
import codecs
import json

if len(sys.argv) < 3:
    print "Use %s file_name.csv lang_code" % sys.argv[0]
    exit()
else:
    csv_file_name = sys.argv[1]
    lang_code = sys.argv[2]

print "Processing %s, language %s" % (csv_file_name, lang_code)

# create a list of categories and words related

translated_words = {}

with codecs.open(csv_file_name, encoding='utf-8', mode='r') as _file:
    line = _file.readline()
    while line:
        parts = line.split(',')

        word = parts[0]
        translated_word = parts[2]

        translated_words[word] = translated_word

        line = _file.readline()

# create json files

translated_words_path = 'words_%s.json' % lang_code
if os.path.exists(translated_words_path):
    print "ERROR: a file %s already exists. Move it and reintent" % \
        translated_words_path
    exit()

with open(translated_words_path, 'w') as json_file:
    json.dump(translated_words, json_file)
