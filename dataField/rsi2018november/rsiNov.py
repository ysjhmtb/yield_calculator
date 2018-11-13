'''
Relative Strength Index

RS(Relative Strength) = N일간의 종가 상승분 평균 / N일간의 종가 하락분 평균

RSI = 100 - { 100 / (1 + RS) }

'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import os


class ToolBox:

    # csv 파일 읽기
    def readCsv(self, filename):
        '''

        :param filename: "DEXKOUS180924.csv"
        :return:
        '''
        rawDate = []
        rawUsd = []
        rawTotal = []

        scriptDir = os.path.dirname(__file__)
        relPath = filename
        absFilePath = os.path.join(scriptDir, relPath)

        f = open(absFilePath, 'r', encoding='utf-8')
        rdr = csv.reader(f)

        for line in rdr:
            rawDate.append(line[0])
            rawUsd.append(line[1])
        f.close()

        if rawDate[0] == 'DATE':
            del rawDate[0]
        if rawUsd[0] == 'DEXKOUS':
            del rawUsd[0]

        # rawTotal
        rawTotal.append(rawDate)
        rawTotal.append(rawUsd)

        # rawTotal에서 rawUsd의 문자열을 실수로. '.' 예외처리.
        toolBox = ToolBox()
        rawTotal[1] = toolBox.strToFloat(rawTotal[1])


    # rawX의 문자열을 실수로.
    def strToFloat(self, rawX):

        floatX = []

        for i in range(len(rawX)):
            if rawX[i] != '.':
                floatX.append(float(rawX[i]))

            # 숫자가 아니라면 이전 인덱스의 값으로 대체.
            elif rawX[i] == '.':
                if i > 0:
                    if rawX[i - 1] == '.':

                        j = i - 2
                        previousWithNumber = -1
                        while j >= 0:
                            if (rawX[j] != '.'):
                                previousWithNumber = j
                                break
                            j -= 1

                        floatX.append(float(rawX[previousWithNumber]))

                    else:
                        floatX.append(float(rawX[i - 1]))
                else:
                    floatX.append(0)

        return floatX

