#!/usr/bin/env python
# Copyright 2013 Gonzalo Odiard <gonzalo@laptop.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import sys
import json

from gi.repository import Gtk
from art4apps import Art4Apps


class Art4AppsTranslator:

    def __init__(self, language):
        self._language = language
        self.window = Gtk.Window()

        self.window.set_title("Art4Apps Translator")

        self.window.set_size_request(400, 400)

        self.window.connect("delete_event", self.delete_event)

        self.hbox = Gtk.HBox()
        self.window.add(self.hbox)

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.hbox.pack_start(self.scrolledwindow, True, True, 0)

        vbox = Gtk.VBox()
        self.checkbutton = Gtk.CheckButton('Only untranslated')
        self.checkbutton.connect('toggled', self._change_word_list)
        vbox.pack_start(self.checkbutton, False, False, 0)
        self.image = Gtk.Image()
        vbox.pack_start(self.image, True, True, 0)
        self.entry = Gtk.Entry()
        self.entry.set_icon_from_stock(Gtk.EntryIconPosition.SECONDARY,
                                       Gtk.STOCK_OK)
        vbox.pack_start(self.entry, False, False, 0)
        self.hbox.pack_start(vbox, True, True, 0)
        self.entry.connect('icon-press', self.__icon_press_cb)
        self.entry.connect('activate', self.__activate_cb)

        self._new_translations = {}
        self.liststore = Gtk.ListStore(str, str)
        self.aa = Art4Apps()
        if self._language not in self.aa.get_languages():
            # trick aa to allow the translation
            self.aa._languages.append(self._language)

        self._load_words()

        self.treeview = Gtk.TreeView(self.liststore)
        self.scrolledwindow.add(self.treeview)

        self.cell = Gtk.CellRendererText()

        self.word_column = Gtk.TreeViewColumn('Word', self.cell, text=0)
        self.treeview.append_column(self.word_column)

        self.trans_column = Gtk.TreeViewColumn('Translation', self.cell,
                                               text=1)
        self.treeview.append_column(self.trans_column)

        self.treeview.set_search_column(0)
        self.word_column.set_sort_column_id(0)

        self.window.show_all()

        self.treeview.connect('cursor-changed', self._word_selected)

    def _change_word_list(self, checkbutton):
        self._load_words(checkbutton.get_active())

    def _load_words(self, only_untranslated=False):
        self.liststore.clear()
        for word in sorted(self.aa.get_words()):
            translation = self.aa.get_translation(word, self._language)
            if translation is None:
                translation = ''
            else:
                if only_untranslated:
                    continue
            self.liststore.append([word, translation])

        for word in sorted(self.aa.get_categories()):
            translation = self.aa.get_translation(word, self._language)
            if translation is None:
                translation = ''
            else:
                if only_untranslated:
                    continue
            self.liststore.append([word, translation])

        posi = self.liststore.get_iter_first()
        while posi:
            word = self.liststore.get_value(posi, 0)
            if word in self._new_translations.keys():
                self.liststore.set_value(posi, 1,
                                         self._new_translations[word])
            posi = self.liststore.iter_next(posi)

    def _word_selected(self, treeview):
        selection = treeview.get_selection()
        if selection is None:
            return
        treestore, posi = selection.get_selected()
        if posi is not None:
            word = treestore.get_value(posi, 0)
            image_filename = self.aa.get_image_filename(word)
            if image_filename:
                self.image.set_from_file(image_filename)
            self.entry.set_text(treestore.get_value(posi, 1))

    def __activate_cb(self, entry):
        self._confirm_translation()

    def __icon_press_cb(self, entry, position, event):
        self._confirm_translation()

    def _confirm_translation(self):
        selection = self.treeview.get_selection()
        if selection is None:
            return
        treestore, posi = selection.get_selected()
        if posi is not None:
            word = treestore.get_value(posi, 0)
            translation = self.entry.get_text()
            treestore.set_value(posi, 1, translation)
            self._new_translations[word] = translation

    def delete_event(self, widget, event, data=None):
        # generate a json dump of the translations
        if self._new_translations:

            translations = {}
            
            for word in sorted(self.aa.get_words()):
                translation = self.aa.get_translation(word, self._language)
                if translation is not None:
                    translations[word] = translation

            for word in sorted(self.aa.get_categories()):
                translation = self.aa.get_translation(word, self._language)
                if translation is not None:
                    translations[word] = translation

            # add the new translations
            for updated_word in self._new_translations.keys():
                translations[updated_word] = self._new_translations[
                    updated_word]

            # save a json file
            # TODO:save sorted
            translated_words_path = 'words_%s.json' % self._language
            with open(translated_words_path, 'w') as json_file:
                json.dump(translations, json_file, indent=4,
                          separators=(',', ': '))

            print "##########################################################"
            print "#A file %s was created with your translations #" % \
                translated_words_path
            print "#you can use it if you copy it in your './data' directory#"
            print "#If you want share it, please send to gonzalo@laptop.org #"
            print "##########################################################"

        Gtk.main_quit()
        return False


def main():
    Gtk.main()

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Select the language to translate using %s lang" % sys.argv[0]
        exit()

    Art4AppsTranslator(sys.argv[1])
    main()
