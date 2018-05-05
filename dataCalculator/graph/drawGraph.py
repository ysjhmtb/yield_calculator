
import matplotlib.pyplot as plt

# 이동평균선 그래프
def drawAvgLine(rawX, rawValue, startIndex, endIndex, averageDay):
    avgLine = []
    for i in range(len(rawX)):
        # 60일선이라면 인덱스 58까지는 0, 인덱스 59부터 충족.
        if i < averageDay - 1:
            avgLine.append(0)
        else:
            tempSum = 0
            for j in range(i - averageDay - 1, i):
                tempSum += rawValue[j]
            tempResult = tempSum / averageDay
            avgLine.append(tempResult)

    plt.plot(rawX[startIndex:endIndex], avgLine[startIndex:endIndex], label='average line')
    plt.plot(rawX[startIndex:endIndex], rawValue[startIndex:endIndex], label='market price')
    plt.legend()
    plt.show()


# 이격도 disparity 구하기
# 현재의 가격이 이동평균선에서 얼만큼 떨어져있는가?
def getDisparity(rawX, rawValue, averageDay):
    disparity = []
    avgLine = []

    for i in range(len(rawX)):
        if i < averageDay - 1:
            avgLine.append(0)
        else:
            tempSum = 0
            for j in range(i - averageDay - 1, i):
                tempSum += rawValue[j]
            tempResult = tempSum / averageDay
            avgLine.append(tempResult)

    for i in range(len(rawValue)):
        if avgLine[i] == 0:
            disparity.append(0)
        else:
            temp = rawValue[i] - avgLine[i]
            disparity.append(temp)

    return disparity



def drawDisparityAndAvgLine(rawX, rawValue, startIndex, endIndex, averageDay):
    disparity = []
    avgLine = []

    for i in range(len(rawX)):
        if i < averageDay - 1:
            avgLine.append(0)
        else:
            tempSum = 0
            for j in range(i - averageDay - 1, i):
                tempSum += rawValue[j]
            tempResult = tempSum / averageDay
            avgLine.append(tempResult)

    for i in range(len(rawValue)):
        if avgLine[i] == 0:
            disparity.append(0)
        else:
            temp = rawValue[i] - avgLine[i]
            disparity.append(temp)

    plt.plot(rawX[startIndex:endIndex], avgLine[startIndex:endIndex], label='average line')
    plt.plot(rawX[startIndex:endIndex], rawValue[startIndex:endIndex], label='market price')
    plt.plot(rawX[startIndex:endIndex], disparity[startIndex:endIndex], label='disparity')
    plt.legend()
    plt.show()