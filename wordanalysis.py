__author__ = 'Jorge Letria'
import re


class WordAnalysis:
        Text = None
        WordList = None

        @property
        def FileIsLoaded(self):
            return (self.Text != None)

        def __init__(self, textFilePath = None):
            if(textFilePath != None):
                self.LoadTextFile(textFilePath)

        def LoadTextFile(self, textFilePath):
            self.TextFilePath = textFilePath
            self.LoadText()
            self.ProcessTextToList()

        def LoadText(self):
            with open (self.TextFilePath, "r") as textFile:
                self.Text=textFile.read()

        def PrintFileContent(self):
            print(self.Text)

        def ProcessTextToList(self):
            localWordList = self.Text\
                .replace('\n', ' ')\
                .replace('.', ' ')\
                .replace(',', ' ')\
                .replace('?', ' ')\
                .replace('!', ' ')\
                .replace(';', ' ')\
                .replace('-', ' ')\
                .replace('"', ' ')\
                .replace("'s", ' ')\
                .replace(':', ' ')\
                .replace("'", ' ')\
                .split(' ')
            self.WordList = []
            for x in localWordList:
                if not x.isspace() and x != '' :
                    self.WordList.append(x.strip(' ').lower())

        def ListWords(self):
            for x in self.WordList: print(x)
