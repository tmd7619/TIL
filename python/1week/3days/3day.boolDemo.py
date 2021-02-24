
# python bool 타입의 특징
# bool
# True(T), False(F)
# not, and, or -> 논리 연산
# &, |, ~ -> 비교연산

# False로 간주 되는 경우
# <비어있는 "", [],(),{}> ,숫자(0 이외의 숫자는 모두 True), None

#십진수의 값을 이진수로 바꾸는 과정
xvalue = 5 # 2진수 0101
yvalue = 0 # 2진수 0000

print(xvalue | yvalue) # 논리 합, 둘중 하나만 ture이면 true
print(xvalue & yvalue) # 논리 곱, 둘다 true일때 true라고 보는 것
#0101 & 0000 -> 0000 -> 0
print(bool(xvalue | yvalue))
print(bool(xvalue & yvalue))
print(bool(xvalue | yvalue))

trueValue = True
falseValue = False
print(int(trueValue))
print(int(falseValue))

print(trueValue & falseValue)
print(trueValue | falseValue)

print('and - ',trueValue and falseValue) # 논리 곱
print('or - ', trueValue or falseValue) # 논리 합
print('not - ', not trueValue) # 