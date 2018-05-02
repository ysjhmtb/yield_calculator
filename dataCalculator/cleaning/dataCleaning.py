

# rawX에서 targetValue의 인덱스 찾
def findIndexAtValue(rawX, targetValue):
    for i in range(len(rawX)):
        if rawX[i] == targetValue:
            return i

# rawX의 문자열을 실수로. 비정형 문자열에 대한 예외처리 필요.
def strToFloat(rawX, exceptionStr):
    floatX = []
    for i in range(len(rawX)):
        if rawX[i] != exceptionStr:
            floatX.append(float(rawX[i]))
        elif rawX[i] == exceptionStr:
            # 예외처리 문자열의 경우 0이 아니라 이전 인덱스의 값으로 대체.
            if i > 0:
                floatX.append(float(rawX[i - 1]))
            else:
                floatX.append(0)

    return floatX

