__author__ = 'Jorge Letria'

import wordanalysis
WordAnalysis = wordanalysis.WordAnalysis

def main():
    BOOK = r'X:\Home\Documents\PythonTexts\animalfarm.txt'
    wa = WordAnalysis(BOOK)
    wa.ListWords()

main()
