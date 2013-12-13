# module to manage art4apps resources

import json
import os

DATA_PATH = '/usr/share/art4apps/data/'
IMAGES_PATH = '/usr/share/art4apps/images/'


class Art4Apps:

    def __init__(self):
        self._words = None
        self._categories_words = None
        self._languages = None
        self._translations = {}

    def _init_words(self):
        if self._words is None:
            with open(os.path.join(DATA_PATH, 'words.json')) as json_file:
                self._words = json.load(json_file)

    def _init_categories_words(self):
        if self._categories_words is None:
            with open(os.path.join(
                    DATA_PATH, 'categories_words.json')) as json_file:
                self._categories_words = json.load(json_file)

    def _init_languages(self):
        if self._languages is None:
            self._languages = []
            for file_name in os.listdir(DATA_PATH):
                if file_name.startswith('words_'):
                    language = file_name[6:8]
                    self._languages.append(language)

    def _init_translation_language(self, language):
        if language not in self.get_languages():
            raise Exception('language no available')
        if language not in self._translations:
            translation_json_path = os.path.join(DATA_PATH,
                                                 'words_%s.json' % language)
            with open(translation_json_path) as json_file:
                self._translations[language] = json.load(json_file)

    def get_image_filename_by_word(self, word):
        self._init_words()
        try:
            return IMAGES_PATH + self._words[word]
        except:
            return None

    def get_categories(self):
        self._init_categories_words()
        return self._categories_words.keys()

    def get_words(self):
        self._init_words()
        return self._words.keys()

    def get_words_by_category(self, category):
        self._init_categories_words()
        return self._categories_words[category]

    def get_languages(self):
        self._init_languages()
        return self._languages

    def get_translation(self, language, word):
        self._init_translation_language(language)
        try:
            return self._translations[language][word]
        except:
            return None

    def get_english_for(self, language, word):
        self._init_translation_language(language)
        translations = self._translations[language]
        for key in translations.keys():
            if translations[key] == word:
                return key
        return None
