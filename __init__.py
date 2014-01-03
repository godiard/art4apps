#!/usr/local/bin/python
# coding: utf-8
# module to manage art4apps resources

import json
import os

DATA_PATH = '/usr/share/art4apps/data/'
IMAGES_PATH = '/usr/share/art4apps/images/'
AUDIO_PATH = '/usr/share/art4apps/audio/'


class Art4Apps:

    def __init__(self):
        self._words = None
        self._categories_words = None
        self._languages = None
        self._translations = {}
        self._language_names = {'en': 'English',
                                'fr': 'Français',
                                'es': 'Español'}
    def _init_words(self):
        if self._words is None:
            if os.path.exists('./data/words.json'):
                json_path = './data/words.json'
            else:
                json_path = os.path.join(DATA_PATH, 'words.json')

            with open(json_path) as json_file:
                self._words = json.load(json_file)

    def _init_categories_words(self):
        if self._categories_words is None:
            if os.path.exists('./data/categories_words.json'):
                json_path = './data/categories_words.json'
            else:
                json_path = os.path.join(DATA_PATH, 'categories_words.json')

            with open(json_path) as json_file:
                self._categories_words = json.load(json_file)

    def _init_languages(self):
        if self._languages is None:
            self._languages = ['en']
            data_path_list = ['./data/', DATA_PATH]
            for data_path in data_path_list:
                for file_name in os.listdir(DATA_PATH):
                    if file_name.startswith('words_'):
                        language = file_name[6:8]
                        if not language in self._languages:
                            self._languages.append(language)

    def _init_translation_language(self, language):
        if language not in self.get_languages():
            raise Exception('language no available')
        if language not in self._translations:
            if os.path.exists('./data/words_%s.json' % language):
                json_path = './data/words_%s.json' % language
            else:
                json_path = os.path.join(DATA_PATH,
                                         'words_%s.json' % language)

            with open(json_path) as json_file:
                self._translations[language] = json.load(json_file)

    def get_image_filename(self, word):
        self._init_words()
        try:
            return os.path.join(IMAGES_PATH, self._words[word])
        except:
            return None

    def get_audio_filename(self, word, language='en'):
        self._init_words()
        audio_file_path = os.path.join(AUDIO_PATH, language, "%s.ogg" % word)
        if os.path.exists(audio_file_path):
            return audio_file_path
        else:
            return None

    def get_language_name(self, language_code):
        if language_code in self._language_names:
            return self._language_names[language_code]
        else:
            return None

    def get_categories(self):
        self._init_categories_words()
        return self._categories_words.keys()

    def get_words(self, language='en'):
        self._init_words()
        self._init_languages()
        if language == 'en':
            return self._words.keys()
        else:
            return self._translations[language].values()

    def get_words_by_category(self, category):
        self._init_categories_words()
        return self._categories_words[category]

    def get_languages(self):
        self._init_languages()
        return self._languages

    def get_translation(self, word, language):
        self._init_translation_language(language)
        try:
            return self._translations[language][word]
        except:
            return None

    def get_english_for(self, word, language):
        self._init_translation_language(language)
        translations = self._translations[language]
        for key in translations.keys():
            if translations[key] == word:
                return key
        return None
