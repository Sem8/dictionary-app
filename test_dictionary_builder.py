import unittest

from dict_application import *


class TestDictionaryApp(unittest.TestCase):
    def lookingUpWordDefinition(self):
        word_definition = get_word_def('chilly')        
        self.assertTrue(word_definition == 'chilly:uncomfortably cool or cold')

        word_definition = get_word_def('word1')        
        self.assertTrue(word_definition == 'word1:def1')

    def lookingUpWordSynonym(self):
        word_synonyms = get_word_synonyms('chilly')        
        self.assertTrue(word_synonyms == "chilly:['cold', 'cool', 'crisp', 'fresh', 'brisk', 'bleak', 'wintry', 'snowy']")

        word_synonyms = get_word_def('word1')        
        self.assertTrue(word_synonyms == "word1:['synonym1', 'synonym2', 'synonym4']")

    def addingWordDefinition(self):
        add_word_definition('word3', 'word3 definition')
        word_definition = get_word_def('word3')        
        self.assertTrue(word_definition == 'word3:word3 definition')

        add_word_definition('hot', 'having a high degree of heat or a high temperature')
        word_definition = get_word_def('hot')        
        self.assertTrue(word_definition == 'hot:having a high degree of heat or a high temperature')

    def addingWordSynonym(self):
        add_word_synonyms('word3', 'wordSynonym1')
        add_word_synonyms('word3', 'wordSynonym2')
        word_synonyms = get_word_synonyms('word3')        
        self.assertTrue(word_synonyms == "word3:['wordSynonym1', 'wordSynonym2']")

        add_word_synonyms('hot', 'very warm')
        add_word_synonyms('hot', 'balmy')
        add_word_synonyms('hot', 'boiling')
        add_word_synonyms('hot', 'tropical')
        word_synonyms = get_word_synonyms('hot')        
        self.assertTrue(word_synonyms == "hot:['very warm', 'balmy', 'boiling', 'tropical']")

if __name__ == '__main__':
    unittest.main()