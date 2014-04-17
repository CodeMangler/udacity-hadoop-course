#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prevQuestion = None
    currentQuestion = None
    type = None
    length = questionLength = answerCount = totalAnswerLength = 0

    for line in reader:
        if(len(line) == 3):
            currentQuestion, type, length = line

            if(type == 'Q'):
                questionLength = length
            else:
                answerCount = answerCount + 1
                totalAnswerLength = totalAnswerLength + int(length)

        if prevQuestion and prevQuestion != currentQuestion:
            if answerCount > 0:
                averageAnswerLength = totalAnswerLength / answerCount
            else:
                averageAnswerLength = 0

            print "{0}\t{1}\t{2}".format(prevQuestion, questionLength, averageAnswerLength)
            questionLength = answerCount = totalAnswerLength = 0

        prevQuestion = currentQuestion

    if prevQuestion != None:
            if answerCount > 0:
                averageAnswerLength = totalAnswerLength / answerCount
            else:
                averageAnswerLength = 0

            print "{0}\t{1}\t{2}".format(prevQuestion, questionLength, averageAnswerLength)

if __name__ == "__main__":
    reducer()
