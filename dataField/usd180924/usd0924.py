'''

During his lifetime, Livermore gained and lost several multimillion-dollar fortunes.
He sometimes played hunches, famously selling Union Pacific railroad short
right before the 1906 San Francisco earthquake.

Most notably, he was worth $3 million and $100 million after the 1907 and 1929 market crashes, respectively.
Adjusted for inflation, $100 million in 1929, equals about $1.13 billion in 2016.

He subsequently lost both fortunes. Apart from his success as a securities speculator,
Livermore left traders a working philosophy for trading securities
that emphasizes increasing the size of one's position as it goes in the right direction
and cutting losses quickly.

https://en.wikipedia.org/wiki/Jesse_Lauriston_Livermore





미국의 트레이더였던 제시 리버모어는 큰 돈을 벌다가 결국 파산을 했는데,
거래 방법 자체가 잘못된 것이었을까요? 아니면 방법은 옳았지만 베팅비율 조절에 실패한 것일까요?

개골
베팅 실패는 운의 문제가 제일 크죠. 컨트롤할 수 없는 운 요소를 빼놓고 생각하면 결국 파산까지 이른 베팅 비율이 문제일듯요.

https://ask.fm/cfr0g/answers/150326757866

'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import os


class ToolBox:

    # rawX에서 targetValue의 인덱스 찾기
    def findIndexAtValue(self, rawX, targetValue):
        for i in range(len(rawX)):
            if rawX[i] == targetValue:
                return i

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


class Position:

    # 포지션 객체 생성
    def __init__(self):
        self.profitArr = []
        self.hasPosition = False

    # 포지션 시작
    def startPosition(self, positionStartPrice, firstDayPrice):
        self.hasPosition = True

        if (positionStartPrice >= firstDayPrice):
            self.direction = "Long"
        else:
            self.direction = "Short"

        self.positionStartPrice = positionStartPrice
        self.firstDayPrice = firstDayPrice
        self.curGainAndLoss = 0
        self.maxProfit = 0

    # 현재 시장가격에서의 손익 업데이트
    def updateProfitRecords(self, curMarketPrice):

        if (self.direction == "Long"):
            self.curGainAndLoss = (curMarketPrice - self.positionStartPrice)
        elif (self.direction == "Short"):
            self.curGainAndLoss = (self.curGainAndLoss - curMarketPrice)

        if (self.curGainAndLoss > self.maxProfit):
            self.maxProfit = self.curGainAndLoss

    # 청산
    def doLiquidation(self, curMarketPrice, curDateStr, curIndex):

        if (self.direction == "Long"):
            self.curGainAndLoss = (curMarketPrice - self.positionStartPrice)
        elif (self.direction == "Short"):
            self.curGainAndLoss = (self.positionStartPrice - curMarketPrice)

        self.profitArr.append(
            [curIndex, curDateStr, self.curGainAndLoss, self.curGainAndLoss / self.positionStartPrice])

        if (curDateStr == "2018-06-05"):
            print()
            print("direction : " + str(self.direction))
            print("curMarketPrice : " + str(curMarketPrice))
            print("positionStartPrice : " + str(self.positionStartPrice))
            print("curGainAndLoss : " + str(self.curGainAndLoss) + "\n")

        self.hasPosition = False
        self.direction = None
        self.positionStartPrice = None
        # self.firstDayPrice = None
        self.curGainAndLoss = None
        self.maxProfit = None

    # 청산 조건 검사
    def hasOptionToLiquidate(self, curMarketPrice, curDateStr, nextDateStr):

        # 시장가가 방향의 반대로 움직이면서 초일 가격을 넘었는지 검사.
        if (self.hasPosition and self.direction == "Long"):

            if (self.firstDayPrice > curMarketPrice):
                print("청산조건 1 : " + str(curDateStr))
                return True

        elif (self.hasPosition and self.direction == "Short"):

            if (self.firstDayPrice < curMarketPrice):
                print("청산조건 1 : " + str(curDateStr))
                return True

        # 현재 손익이 최대점에서 20% 감소 여부 검사.
        if (self.hasPosition and self.curGainAndLoss <= self.maxProfit * 0.8 and self.maxProfit != 0):
            print("청산조건 2 : " + str(curDateStr))
            return True

        # 매달 말일인지 검사.
        toolBoxInPosition = ToolBox()

        flag = toolBoxInPosition.isLastDayInMonth(curDateStr, nextDateStr)
        toolBoxInPosition.kill()
        if (self.hasPosition and flag):
            print("청산조건 3 : " + str(curDateStr))
            return True

        return False

    # 정보출력
    def toString(self):
        print()
        print("hasPosition : " + str(self.hasPosition))
        print("direction : " + str(self.direction))
        print("positionStartPrice : " + str(self.positionStartPrice))
        print("firstDayPrice : " + str(self.firstDayPrice))
        print("curGainAndLoss : " + str(self.curGainAndLoss))
        print("maxProfit : " + str(self.maxProfit) + "\n")


# csv 파일 읽기
rawDate = []
rawUsd = []
rawTotal = []

scriptDir = os.path.dirname(__file__)
relPath = "DEXKOUS180924.csv"
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

'''
print(toolBox.findIndexAtValue(rawTotal[0], '1981-04-13'))  # 0
print(toolBox.findIndexAtValue(rawTotal[0], '2018-09-14'))  # 9764
print("\n\n")
'''

# 데이터로 시뮬레이션
myPosition = Position()

for i in range(1, len(rawTotal[0]) - 1):

    # 현재 인덱스가 매달 첫째날이라면 다음날 포지션 시작
    if (toolBox.isFirstDayInMonth(rawTotal[0][i], rawTotal[0][i - 1])):
        myPosition.startPosition(rawTotal[1][i + 1], rawTotal[1][i])
        continue

    # 현재 포지션이 없고, 매달 마지막날이 아니라면 포지션 시작 가능 여부 검사
    if (not myPosition.hasPosition and toolBox.isLastDayInMonth(rawTotal[0][i], rawTotal[0][i + 1])):
        myPosition.startPosition(rawTotal[1][i + 1], rawTotal[1][i])
        continue

    # 현재 인덱스에서 청산조건 충족여부 검사
    if (myPosition.hasOptionToLiquidate(rawTotal[1][i], rawTotal[0][i], rawTotal[0][i + 1])):
        myPosition.doLiquidation(rawTotal[1][i], rawTotal[0][i], i)
        continue

    # if (i >= 9000 and i < 9764):
    #     print(rawTotal[0][i])
    #     myPosition.toString()

# for i in range(len(myPosition.profitArr)):
#     print(myPosition.profitArr[i])


# optimal allocation

f = 0
fList = []
maxList = []

while f < 15:
    elog1fx = 0
    for k in range(len(myPosition.profitArr)):
        elog1fx += ((1 / len(myPosition.profitArr)) * np.log2(1 + f * myPosition.profitArr[k][3]))
    fList.append(f)
    maxList.append(elog1fx)

    f += 0.01

plt.plot(fList, maxList, label="f1")
plt.legend()
plt.show()

# capital growth

seed = 100
seedList = []
for i in range(len(myPosition.profitArr)):
    seed *= (1 + 10 * myPosition.profitArr[i][3])
    seedList.append(seed)

plt.plot(seedList, label="capital growth")
plt.legend()
plt.show()
