from art4apps import Art4Apps

aa = Art4Apps()

words = aa.get_words()

print "*" * 10  + "ALL THE WORDS IN ENGLISH" + "*" * 10 
print words

categories = aa.get_categories()
print "*" * 10  + "ALL THE CATEGORIES IN ENGLISH" + "*" * 10 
print categories

print "*" * 10  + "TEST TRANSLATION TO ALL THE LANGUAGES" + "*" * 10 

languages = aa.get_languages()
for language in languages:
    print "Language %s" % language
    word = words[4]
    print "Word %s = %s" % (word, aa.get_translation(word, language))

print "*" * 10  + "WORDS BY CATEGORY %s" % categories[2] + "*" * 10 
print aa.get_words_by_category(categories[2])

print "*" * 10  + "ALL THE WORDS IN %s" % languages[1] + "*" * 10 
print aa.get_words(languages[1])

print "*" * 10  + "IMAGE FILE NAME FOR %s" % words[5] + "*" * 10 
print aa.get_image_filename(words[5])

print "*" * 10  + "AUDIO FILE NAME FOR %s" % words[5] + "*" * 10 
print aa.get_audio_filename(words[5])

print "*" * 10  + "AUDIO FILE NAME FOR %s lang %s" % (words[2], 'fr') + "*" * 10 
print aa.get_audio_filename(words[2], 'fr')

