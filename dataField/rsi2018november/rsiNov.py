'''
Relative Strength Index

RS(Relative Strength) = N일간의 종가 상승분 평균 / N일간의 종가 하락분 평균

RSI = 100 - { 100 / (1 + RS) }

'''

'''

15. 주식시장의 수익률 분포에 대해 알아봅시다

https://youtu.be/l-_-Et7PZ0I


--------------------------------------------------------------------------------


그는 저점은 함부로 예단할 수 없다고 말한다. 자신의 여러번 경험도 얘기해준다. 
2008년에도 극단적인 위험 회피가 나타났는데, 분할매수 했었다고 한다. 그건 이전에 낙관론이 많을때 
미리 상대적 성과부진을 감수하면서까지 현금화를 해놨기 떄문에 가능했을거다.


지금은 비관론이 우세한가? 낙관론이 우세한가? 사람들은 아직도 상승할꺼라는 미련이 많지 않나? 
비관론이 우세하다면 얼마나 더 우세할까?


http://blog.naver.com/econophysics/221402865184


--------------------------------------------------------------------------------


Yuan Exposed to Vanishing U.S.-China Yield Gap as Much as Trade

https://www.bloomberg.com/news/articles/2018-11-19/yuan-exposed-to-vanishing-u-s-china-yield-gap-as-much-as-trade


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
        rawTotal[1] = self.strToFloat(rawTotal[1])

        return rawTotal

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

    # rawX에서 targetValue의 인덱스 찾기
    def findIndexAtValue(self, rawX, targetValue):
        for i in range(len(rawX)):
            if rawX[i] == targetValue:
                return i

    # 입력받은 날짜가 매달 첫째날인지 확인
    def isFirstDayInMonth(self, curDateStr, preDateStr):

        # 오늘 날짜의 월과 이전 날짜의 월이 다르면 오늘 날짜가 이번 달의 첫째날
        # 1981-04-13    인덱스 5가 시작.

        from operator import eq

        curMon = curDateStr[5:7]
        preMon = preDateStr[5:7]

        if (eq(curMon, preMon)):
            return False
        else:
            return True

    # 입력받은 날짜가 매달 마지막 날인지 확인
    def isLastDayInMonth(self, curDateStr, nextDateStr):

        from operator import eq

        curMon = curDateStr[5:7]
        nextMon = nextDateStr[5:7]

        if (eq(curMon, nextMon)):
            return False
        else:
            return True

    # 툴박스 객체 삭제
    def kill(self):
        del self


tool = ToolBox()
rawTotal = tool.readCsv("DEXKOUS180924.csv")

# 매달 최대값과 최소값을 구하고, 변동 구하기

monStartPrice = 1
monMax = 1
monMin = 1
vol = []

for i in range(1, len(rawTotal[0]) - 1):

    # 매월 첫번째 거래일 가격 기록
    if (tool.isFirstDayInMonth(rawTotal[0][i], rawTotal[0][i - 1])):
        monStartPrice = rawTotal[1][i]
        monMax = rawTotal[1][i]
        monMin = rawTotal[1][i]

    # 최대값
    if (monMax <= rawTotal[1][i]):
        monMax = rawTotal[1][i]

    # 최소값
    if (monMin >= rawTotal[1][i]):
        monMin = rawTotal[1][i]

    # 마지막날 변동 계산
    if (tool.isLastDayInMonth(rawTotal[0][i], rawTotal[0][i + 1])):
        vol.append(((monMax - monMin) / monMin))

del(vol[0])
print(sum(vol) / len(vol))

plt.plot(vol, label = "vol")
plt.legend()
plt.show()


