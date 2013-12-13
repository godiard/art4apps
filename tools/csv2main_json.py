#!/usr/bin/env python

# convert a csv file to a json structured data
# with general information about the Art4Apps images
# the csv have the following format:
# english_word,category,translated_word,image
# this script ignores the translated word,
# other script will take of that

import os
import sys
import codecs
import json

if len(sys.argv) < 2:
    print "Use %s file_name.csv" % sys.argv[0]
    exit()
else:
    csv_file_name = sys.argv[1]

print "Processing %s" % csv_file_name

# create a list of categories and words related

categories_words = {}

words = {}

with codecs.open(csv_file_name, encoding='utf-8', mode='r') as _file:
    line = _file.readline()
    while line:
        parts = line.split(',')

        word = parts[0]
        category = parts[1]
        image_link = parts[3]

        original_path = 'http://laske.fr/abecedarium/images/database/'
        new_path = '/usr/share/art4apps/images/'
        words[word] = image_link[image_link.rfind('/') + 1:]

        if category != '':
            if category not in categories_words:
                categories_words[category] = []

            categories_words[category].append(word)

        line = _file.readline()

# create json files

categories_words_path = 'categories_words.json'
if os.path.exists(categories_words_path):
    print "ERROR: a file %s already exists. Move it and reintent" % \
        categories_words_path
    exit()

with open(categories_words_path, 'w') as json_file:
    json.dump(categories_words, json_file)

words_path = 'words.json'
if os.path.exists(words_path):
    print "ERROR: a file %s already exists. Move it and reintent" % \
        words_path
    exit()

with open(words_path, 'w') as json_file:
    json.dump(words, json_file)
