__author__ = 'Jorge Letria'

import wordanalysis
WordAnalysis = wordanalysis.WordAnalysis

def main():
    BOOK = r'animalfarm.txt'
    wa = WordAnalysis(BOOK)
    wordCount = wa.ListWordCount()
    with open (BOOK.rstrip('.txt') + '_wordcount.txt', "w") as textFile:
        textFile.write(wordCount)

main()
