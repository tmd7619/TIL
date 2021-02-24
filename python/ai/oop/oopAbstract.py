
'''
*** 학습목표 ***
다중상속 : 부모가 한명 이상~
추상화
데코레이션
제너레이터
이터레이터
'''

class Animal(object) :
    def cry(self):  # 추상함수
        pass

class Tiger(Animal) :
    def jump(self):
        print('호랑이가 점프를 한다')
    def cry(self):
        print('어흥')
class Lion(Animal) :
    def bite(self):
        print('한 입에 꿀꺽한다')
    def cry(self):
        print('그르렁')
class Liger(Tiger,Lion) : # 다중상속 # Tiger가 Lion보다 함수 실행시 우선적을 출력됨
    def play(self):
        print('라이거와 사육사가 재미있게 놀고 있다.')

# 추상클래스
'''
https://dojang.io/mod/page/view.php?id=2389 참조
추상 클래스는 메서드의 목록만 가진 클래스이며, 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용합니다.
먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 합니다( abc는 abstract base class의 약자입니다). 
그리고 클래스의 ( )(괄호) 안에 metaclass=ABCMeta를 지정하고, 
메서드를 만들 때 위에 @abstractmethod를 붙여서 추상 메서드로 지정합니다.
'''
'''
- 클래스를 만드는 이유 -> 객체생성
- 추상클래스는 객체 생성 x
- 추상메서드(함수)를 하나라도 가지면 추상클래스
- 함수 구현을 강제하기 위해 사용
- 추상 클래스를 상속받았다면, @abstractmethod가 붙은 추상 메서드를 모두 구현해야 합니다.
'''

# 추상 메서드 생성
from abc import * #추상메서드를 만들기 위해 불러옴
class Base(metaclass=ABCMeta) : # 추상화 class인 'Base '생성
    @abstractmethod # 추상화메서드로 적용하기
    def study(self):
        pass

    def goToSchool(self): # @ ~ 없으니 , 이 함수는 추상화 메서드가 아님. 따라서 강제 구현할 필요가 없음
        print('hard study')

class Student(Base) :
    def study(self):
        print('공부하자')

# study01 = Base()  # type error . 추상 클래스는 인스턴스로 만들 수가 없음
# 그래서 지금까지 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만든 것. 호출할 일이 없기 때문

study01 = Student() # 추상 클래스의 추상 메서드를 모두 구현했는지 확인하는 시점 모두 구현이 안되면, TypeError
study01.study()

# 특수문법 - 데코레이션
# 데코레이션을 사용하려면 클로저와 중첩함수에 대한 이해를 해야함 !!
'''
Decorator는 함수의 인자로 다른 함수를 전달하는 과정에서 적용할 수 있는 기법
'''

def outerFunc(func) : # 호출할 함수를 매개변수로 받음
    def innerFunc() : # 호출할 함수를 감싸는 함수
        func()        # 매개변수로 받은 함수를 호출
    return innerFunc  #감싸는 함수 반환

def userFunc() :
    print('userFunc 함수가 수행되었습니다')

myFunc = userFunc()
myFunc()
# userFunc()

decoratorFunc = outerFunc(userFunc)

import time
def userOuterFunc(func) : # func는 임의적으로 설정가능, 함수를 인자로 받겠다는 의미
    def userInnerFunc() :
        print('{}함수수행 시간을 계산합니다.'.format(func.__name__)) #  __name__ 함수의 이름을 return시켜주는 속성 #debug 코드라고 생각하면 됨
        start = time.time()
        func()  # userInnerFunc() 함수를 실행시키기 위해 입력된 코드
        end = time.time() - start
        print('{} 함수수행 시간은 {}입니다'.format(func.__name__, end))
    return userInnerFunc

decoratorUserFunc = userOuterFunc(userFunc) #데코레이터
decoratorUserFunc()

import datetime
def loggerLoginseop() :     # 코드 중첩으로, 효율성이 떨어짐
    # print(datetime.datetime.now()) # 코드 중첩으로 삭제
    print("seop's login ")
    # print(datetime.datetime.now()) # 코드 중첩으로 삭제

def loggerLoginKing() :
    # print(datetime.datetime.now()) # 코드 중첩으로 삭제
    print("king's login")
    # print(datetime.datetime.now()) # 코드 중첩으로 삭제

def datetimeDecorator(func) :    # 데코레이터 패턴 만들기
    def wrapper() :
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return wrapper

seop = datetimeDecorator(loggerLoginseop) #데코레이터 적용
seop()

king = datetimeDecorator(loggerLoginKing)
king()


@datetimeDecorator # datetimeDecorator라는 함수를 호출하는 효과를 불러옴
def dumpFunc() :
    print('함수 실행~~')
dumpFunc()

# 데코레이터 [실습]
'''
1. typeChecker Decorator 만들기(인자의 유효성 검증)
- digit01, digit02 를 곱한 값을 출력하는 함수 
- typeChecker Decorator로 digit01,digit02가 정수가 아니면
- 'only integer support' 출력
'''

def typeChecker(func): # 데코레이터 함수로 만들기
    def wrapper(digit01,digit02) :
        if type(digit01) != int or type(digit02) != int :
            print('only integer support')
            return # return지정을 안해주면, 다음 function으로 진행하기 때문에 stop, #return 뒤에 아무 값도 지정 안해주면 종료의 의미
        return func(digit01,digit02) #인자가 두개이상일떄,
    return wrapper
# 사용
@typeChecker
def div(digit01,digit02) :
    return digit01 * digit02

div(1,1) # 유효성 체크가 되는지 체크
div(12,32.32)

# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들고 싶다면?
# *args, **args # 가변인자는 변수들의 가장 맨 마지막에 넣어줘야 오류가 안남.
# ex) fx(인자1,인자2,*args)


def generalDeco(func) :
    def wrapper(*args, **kwargs) :
        print('this is decorated ')
        return func(*args,**kwargs)
    return wrapper

@generalDeco
def userSquare(digit) : # 인자 1개
    return digit * digit
print(userSquare(2))

@generalDeco
def userPlus(digit01,digit02) : #인자 2개
    return digit01 + digit02
print(userPlus(2,3))

@generalDeco
def userQuad(digit01,digit02,digit03,digit04) : #인자 4개
    return digit01* digit02 * digit04 * digit03
print(userQuad(2,3,4,5))


# 2개 이상의 데코레이터 활용
def makeBold(func) :
    def wrapper(string) :
        return '<b>' + func(string) + '</b>'
    return wrapper

def makeFont(func) :
    def wrapper(string) :
        return '<i>' + func(string) + '</i>'
    return wrapper

@makeFont # 두개이상의 데코레이터 사용
@makeBold
def makeBoldFont(string) :
    return string

print(makeBoldFont('두개의 데코레이터를 활용하고 있습니다'))
# 실행 순서 @makeBold -> @makeFont
# 가장 가까운 데코레이터부터 실행됨 .


# class - function 데코레이터 적용이 가능 할까요?

def tagH1(func) :   # 장식자 함수 생성
    def wrapper (self,*args,**kwargs) : # 여기서 왜 self 라는 인자를 추가한건지 ?
        return '<h1>{}</h1>'.format(func(self,*args,**kwargs))
    return wrapper

class Per (object) :
    def __init__(self,name):
        self.name= name
    @tagH1
    def getName(self):
        return self.name

per = Per('jslim')
print('per - ',per.getName())

# Iterator
'''
- iterable 객체(iterable Object)
list, set, dict - (collection)
Text Sequence
for ~ in collection :
    pass 
- iterator - > 파이썬 모듈이 가지고 있는 내장함수 iter()
-> 순차적으로 다음 데이터를 리턴할 수 있는 객체
-> 내장함수 next() 사용해서, 순환하는 다음 값을 반환함
 만약 연속된 숫자를 미리 만들면 숫자가 적을 때는 상관없지만 
 숫자가 아주 많을 때는 메모리를 많이 사용하게 되므로 성능에도 불리합니다. 
 그래서 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 
 값을 만드는 방식을 사용합니다. 
 즉, 데이터 생성을 뒤로 미루는 것인데 
 이런 방식을 지연 평가(lazy evaluation)라고 합니다.
'''
# iterable 객체
for num in [1,2,3,4,5] :
    print(num)
# dir([1,2,3,4]) # dir 함수를 이용하여 객체 내에 __iter__ 메소드가 있으면 iterable 객체
for char in 'text sequence ' : # Text Sequence 또한 순서가 있기 때문에 looping 가능
    print(char)

# Iterator

userList = [1,2,3,4,5]
print(next(userList)) # TypeError: 'list' object is not an iterator

# 따라서 iter()를 통해 이터레이터로 변환시켜야함

userIterator = iter(userList)
print(type(userIterator),type(userList)) # <class 'list_iterator'>
print(next(userIterator)) #순환하는 다음 값을 반환함

# 다른방법으로는,

userList01 = [1,2,3,4,5].__iter__()
userList01.__next__()

# 사용자 정의 iterator 클래스 만들어 보자
# https://dojang.io/mod/page/view.php?id=2406 참조
class Counter : # iterable 작업
    def __init__(self,stop):
        self.stop = stop
    def __iter__(self): # 이터레이터로 구현시키기 위한 매직함수
        return CounterIterator(self.stop)  # 현재 인스턴스를 반환


class CounterIterator : # iterator 작업
    def __init__(self,stop):
        self.current = 0
        self.stop = stop
    def __next__(self):
        if self.current < self.stop :
            rtnValue = self.current # 반환할 숫자를 변수에 저장
            self.current += 1
            return rtnValue    # 숫자를 반환
        else :
            pass

cntIterator = iter(Counter(10))
print(next(cntIterator))

# Comprehension 복습
'''
list 형식 - [ 출력표현식(연산식 가능) for 요소 in sequence [if 조건식] ] 파이썬 ~ 2.0버전
set 형식 - { 출력표현식(연산식 가능) for 요소 in sequence [if 조건식] } 파이썬 3.0버전 ~
dict 형식 - { key : value  for 요소 in sequence [if 조건식] } 파이썬 3.0버전 ~

'''
dataset = [4,True,'jslim',3.1,10]
# 위 데이터 셋에서 정수값만 출력을 원한다면 ?

intType = [value for value in dataset if type(value) == int ]
print(' int type - ', type(intType),intType)

intType = [value **2  for value in dataset if type(value) == int ] #연산식도 가능
print(' int type - ', type(intType),intType)

dataset = [1,1,2,2,3,3,4,4]
setType = {value * value for value in dataset } # set 중복 허용 x , 순서존재 x
print(' set type - ', type(setType),setType)

dataset = { 1: 'jslim',  2 : 'parksu ', 3 : 'multicampus'}
print('dict keys - ', dataset.keys())
print('dict keys - ', dataset.values())
print('dict keys - ', dataset.items())

# key 값이 1 이상인 데이터를 값:키 형식으로 새로운 set 만들다면 ?
dict01 = {value : key  for key, value in dataset.items() if key > 1 }
print('dict comprehension - ', type(dict01),dict01)

# key 값을 10단위로 한번에 바꿔본다면?
dict01 = {key*10 : value for key, value in dataset.items() if key > 1 }
print('dict comprehension - ', type(dict01),dict01)

# python generator
'''
제너레이터는 제너레이터 객체에서 __next__ 메서드를 호출할 때마다 
함수 안의 yield까지 코드를 실행하며 yield에서 값을 발생시킵니다(generate). 
그래서 이름이 제너레이터(generator)입니다.
iterator 를 만들어주는 기능
yiled 키워드 이해 
메모리 성능 때문에 루프를 컨트롤하기 위해 쓰여지는 루틴..
'''
def textSequenceFunc() :
    msg = 'hi python'
    for txt in msg :
        #print(txt)
        #return txt # return을 입력하면, 순환 종료 됨
        yield txt
# print(textSequenceFunc)
textSequenceFunc()

charIte = iter(textSequenceFunc())
print(type(charIte))
print(next(charIte))

'''
yield - 잠시 함수의 실행을 멈추고 호출한 곳에 값을 전달
- 현재 실행된 상태를 계속 유지
- 그러므로, 다시 해당 함수를 호출하면 현재 실행된 상태를 기반으로 다음 코드 실행
'''
print(textSequenceFunc())
charIte = iter(textSequenceFunc())
next(charIte)

# 일반 iterable
def userGeneratorFunc(data) :
    result = []
    for tmp in data :
        result.append(tmp*2)
    return result

twiceList = userGeneratorFunc([1,2,3,4,5])
print('처리된 결과 - {}'.format(twiceList))

# generate 변경
def userGeneratorFunc(data) :
    result = []
    for tmp in data :
        yield tmp * 2


twiceList = userGeneratorFunc([1,2,3,4,5])
print(type(twiceList))
print('next - {} '.format(next(twiceList)))

# Genrator Comprehension
# lazy
'''
syntax)
(출력형식 for 요소 in collection)
'''
squareData = ( num ** 2 for num in range(5))
print(type(squareData))
# print(squareData)
print(sum(squareData))
for data in squareData :
    print(sum(squareData))