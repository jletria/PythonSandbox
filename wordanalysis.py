__author__ = 'Jorge Letria'
import operator


class WordAnalysis:
        Text = None
        WordList = None
        WordCount = None
        CommonWords = None
        WordListSyncedToText = False
        WordCountInSync = False

        @property
        def FileIsLoaded(self): return self.Text is not None
        @property
        def WordListIsLoaded(self): return self.WordList is not None

        def __init__(self, textFilePath=None):
            if(textFilePath is not None):
                self.Initialize(textFilePath)

        def Initialize(self, textFilePath):
            self.TextFilePath = textFilePath
            self.LoadText()
            self.LoadCommonWords()
            self.ProcessTextToList()
            self.ProcessWordCount()

        def FileToStr(self, filePath):
            with open (filePath, "r") as textFile:
                return textFile.read()

        def LoadText(self):
            self.Text=self.FileToStr(self.TextFilePath)
            self.WordListSyncedToText = False

        def LoadCommonWords(self):
            self.CommonWords=self.FileToStr('commonwords.txt').lower().split('\n')

        def PrintFileContent(self):
            print(self.Text)

        def ProcessTextToList(self):
            if not self.FileIsLoaded or self.WordListSyncedToText: return;
            localText = self.Text.lower()
            undesirableCharacters = ['\n', '.', ',', '?', '!', ';', '-', '"', "'s", ':', "'"]
            for ch in undesirableCharacters: localText = localText.replace(ch, ' ')
            localWordList = localText.split(' ')
            self.WordList = []
            for x in localWordList:
                if (not x.isspace()) and (x != '') and (x not in self.CommonWords) :
                    self.WordList.append(x.strip(' '))
            self.WordListSyncedToText = True
            self.WordCountInSync = False

        def ProcessWordCount(self):
            if not self.WordListIsLoaded or self.WordCountInSync: return
            wc = self.WordCount = {}
            for x in self.WordList:
                if not x in wc: wc[x] = 1
                else: wc[x] += 1
            self.WordCountInSync = True

        def ListWordCount(self):
            sorted_x = sorted(self.WordCount.items(), key=operator.itemgetter(1), reverse=True)
            ret = ''
            for x in sorted_x: ret += x[0] + ': ' + str(x[1]) + '\n'
            return ret

        def ListWords(self):
            ret = ''
            for x in self.WordList: ret += x + '\n'
            return ret
