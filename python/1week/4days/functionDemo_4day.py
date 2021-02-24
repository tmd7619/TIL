
# python function
'''
함수는 가독성을 높이기 위한 방법으로
하나 이상의 본문을 가지는 코드는 함수로 정의하는 것이 좋다.
함수는 내장함수 | 사용자 정의 함수로 나눠져 있음
함수를 정의할 때는 def 키워드를 이용해서 함수를 정의
'''

# user define function
'''
def functionName() :
    statement
    #return value(built-in Type)
'''

from digital.python import packageFunction_4day # R의 library와 똑같다고 생각하면 됨.
packageFunction_4day.printCoins() #이렇게 다른 패키지에 있는 함수를 불러올 수 있음

#from digital.python import packageFunction  # 가장 기본적인 방법 !
#packageFunction.printCoins()

#from digital.python import packageFunction as f # 가장 편리하게 사용할 수 있음
#f.printCoins()

#from digital.python.packageFunction import printCoins
#printCoins()

from digital.python import packageFunction_4day as f

rtn = f.returnFunc()
print('call returnFunc()- ', rtn)

echoMsg = f.sayEcho('윤승원')
print('call sayEcho()-',echoMsg)


domain = f.makeUrl('naver')
print('call makeUrl()-',domain)

f.badFunc('ysw') # 결과 x

tupRtn = f.tupleFunc(1,2,3,4,5,6,7,8,9)
print('call tupleFunc()-',tupRtn)

f.dictFunc(name='jslim',age = 49) # 두개 이상의 인자값 받을 수 있음

(oddSumf,evenSum) = f.cntSum(100,500)
print('홀수의 합{},짝수의 합{}'.format(oddSumf,evenSum))

# 인자로 넘겨받은 년도 사이의 윤년을 찾아 리턴시켜주는 함수를 작성한다면?
# list 타입
leapYearList = f.leapYearFunc(1900,2021)
print('leapYearList- ',leapYearList)

dictMsg = f.rtnDictFunc(10)
print('dictMsg - ', type(dictMsg),dictMsg)

for value in dictMsg.values() :
    print('dict_values - ',value)

# default parameter 사용
# worker Function
def defaultParam(x,y, z=True) :
    pass
    paramSum = x + y
    if paramSum > 10 and z :
        return paramSum
    else :
        return 0
 # caller function
result = defaultParam(10,20) # z와 True 값을 넣지 않아도, 2개의 인자만 넣어도 z와 True를 자동으로 입력되게 해줌
print('caller defaultParam() - ',result)

# 함수의 입력인자가 list, dict - mutable (가변 형식) call by reference
# 함수의 입력인자가 숫자, 문자열, tuple 일때, - immutable call by value
tmpList = [10]
tmpX = 10
def mutableFunc(argx, argList):    #인터프리터방식은, 변수가 할당되는 동시에 타입이 결정됨
    argx = argx + 100           # 100을 더해도, 결괏값은 10으로 동일함 (immutable한 성격)
    argList.append(100)

mutableFunc(tmpX,tmpList)
print('tmpList -', tmpList)
print('tmpx -', tmpX)

 # variable = 선언위치에 따라서 (local, global)
 # 함수 내에서는 로컬변수 > 글로벌변수 우위
tmp = 100 # global 변수

def myFunc(x) :
    tmp = 0     # local 변수
    tmp += x
    return tmp

print(myFunc(100))

tmp = 100 # global 변수

def myFunc(x) :
    global tmp  # 함수 외부에 있는 변수를 함수 내에서 사용하고 싶다면 global
    tmp += x
    return tmp

print(myFunc(100))

def personInfo(weight,height,**other) : # 단일인자와, 가변인자 같이 사용할 수도 있음
    print('weight - ', weight)
    print('height - ', height)
    print('extra - ', other,type(other)) # dict

personInfo(5,4, name='섭섭해',address='seoul') #dict형식은 = 형태로 만들어줘야함
# personInfo(5,4, {'name:'섭섭해'}) # type error

def overroll(args01 , args02 ,*args03, **args04,) :  # 단일 2개 가변 2개
    print(args01,args02,args03,args04)

overroll(10,20,'lee','kim','park','cho',age01=20,age02=30,arg03=40)
# 10,20 은 단일인자, lee,cho~ 는 *args03로 튜플형태

# nested function (중첩함수) 함수에 또 다른 함수를 정의할 수 있는 함수
def outerFunc(num) :
    def innerFunc(num) :  #중첩함수
        print('innerFunc - ', num)
    innerFunc(num + 100)


outerFunc(100) # >>> 200
# innerFunc(100 ) 실행불가 즉, 호출 불가합니다

'''
중첩함수 활용 예)
outer 함수 : 자료(data) 생성 , inner 함수 포함
inner 함수 : 자료 연산/처리(합계,평균 ...)
'''

def calcFunc(data) :
    dataset = data # outer함수에 있는 변수들을 inner끼리 공유할 수 있음
    def sumFunc() : # inner 함수1
        total = sum(dataset) #inner 함수 정의
        return total # 호출
    def avgFunc(total) : # inner 함수 2
        avg= total / len(dataset) # inner 함수2 정의
        return avg # 호출
    return sumFunc , avgFunc # closure # inner함수를 return함으로써, 외부함수로 사용 가능하게 함

'''
파이썬에서 함수는 일급 객체입니다. 
이는 우리가 평소에 숫자나 문자열, 클래스를 다루는 것처럼, 
함수도 다른 객체와 동일하게 취급할 수 있다는 말과 같습니다. 
즉, 함수를 매개변수로 넘기거나 다른 변수에 대입할 수 있으며, 
반환값으로도 사용이 가능합니다. 
심지어 리스트나 사전과 같은 자료구조에 저장할 수도 있습니다. 
https://blog.hexabrain.net/347 클로저 참조 url
'''

data = list(range(1,100))
print('range data - ', data)

(rtnSumFunc, rtnAvgFunc) = calcFunc(data) # return 을 2개이상 하게 되면 ,tuple형식으로 받을 수 있음
# 함수도 함수이기 전에 객체이기 때문에, inner함수 sumFunc와 avgFunc의 이름을 변경할 수 있음
tot = rtnSumFunc() # 함수 호출
print(tot)
avg = rtnAvgFunc(tot) # 함수 호출
print(avg)

'''
재귀함수(self - recursive function) 
- 함수 내부에서 자신의 함수를 반복 호출하는 기법
- 용도 : 반복적으로 변수를 변경해서 연산할 때(누적,팩토리얼)
- 재귀함수는 종료가 필수적이기에, 끝나는 조건을 해주어야함
'''
def countFunc(n) : # n = 5 -> 1,2,3,4,5
    if n == 0 :
        return 0
    else :
        countFunc(n-1) # stack [5,4,3,2,1] 후입선출방식
        print(n, end=" ")

countFunc(5) # >>>  1 2 3 4 5  #stack 의 후입선출 순서로 인해

# 누적 : (n) = 1+2+3+4.......+n
def addSum(n) :
    if n == 1 : # n이 1일때
        return 1 # 1을 반환하고 재귀호출을 끝냄
    else :
        result = n + addSum((n-1))
        print('debug - ', result)
        return  result
print ('n=5 -',addSum(5))
print ('n=100 -',addSum(100))

# https://dojang.io/mod/page/view.php?id=2353  참고

# 익명의 함수 (lambda 식)를 만드는 방법
# 람다식(가독성 향상, 코드가 간결해짐, 메모리 절약- 즉시 실행 함수이기 때문에)

def multiFunc(x,y) :
    return  x* y
print(multiFunc(10,50))

# syntax : lambda arg : body

lambdaVar = lambda x,y : x * y
print(lambdaVar(10,50))

def lambdaFunc(x,y,func) :
    print('lambdaFunc - ',x*y*func(100,100))

lambdaFunc(10,20,lambda x, y : x*y)
lambdaFunc(10,20,lambdaVar)

# hint
def totalLengthFunc(word : str, num : int) :
    return len(word) * num

print('hint - ',len('i love you'),totalLengthFunc('i love you',10))