
'''
학습목표
- Composition : == aggregation
상속을 피하면서, 클래스의 일부 기능을 그대로 활용하고 싶을때
상속관계가 복잡할 경우, 코드 이해가 어려운 경우가 많다.
컴포지션은 명시적 선언 , 상속은 암시적 선언

- Exception
- file 입출력
'''

# Composition

class Calc01(object) : # == class Calc01 :
    def __init__(self,x,y):
        self.x = x # 인스턴스 변수 생성
        self.y = y
    def add(self):
        return self.x + self. y
    def substract(self):
        return  self.x - self.y


class Calc02(object):  # 다른 클래스 생성
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self): # 함수이름은 동일하지만, 다른 add
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

# Class Calc02의 multiply함수만 활용하기 (상속관계가 아니라 )
class UserCalc :
    def __init__(self,x,y ):
        self.x = x
        self.y = y
        self.cal02 = Calc02(x,y)  # 해당 클래스의 객체를 명시적으로 생성
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.x - self.y
    def multiply(self):
        return self.cal02.multiply() # Calc02의 multiply함수의 기능만 가져다 쓰겠다
                                     # 상속의 overiding이랑 다름
calc = UserCalc(4,5)
print('calc multiply - ',calc.multiply())

'''
- 예외(Exception) - ex) SyntaxError,TypeError,NameError,KeyError.... 
- 처리할 수 있는 구문
예외가 발생하면 해당 줄에서 코드 실행을 중단하고 
바로 except로 가서 코드를 실행합니다.
try     :
    에러가 발생할 가능성이 있는 코드 - 1 
    정상코드 - 2 
    에러가 발생할 가능성이 있는 코드 - 3 
    정상코드 - 4 
except  xxxxError: 
    발생된 에러를 잡기 위한 객체를 정의하는 영역 - 1 
    1. 프로그램의 흐름을 정상적으로 컨트롤
    2. 예외발생의 디버깅 
    3. 로그파일을 만들어서 예외정보를 저장 
except  xxxxError:
    발생된 에러를 잡기 위한 객체를 정의하는 영역 - 3
else    : 
    에러가 발생되지 않을때 실행되는 영역 - 2,- 4
finally : 
    에러발생 유무와 상관 없이 무조건 실행되는 영역

참조 https://dojang.io/mod/page/view.php?id=2400
'''

#print('error)
# a = 20
# b = 30
# # print(c)
# # print(100/0)
# x = [1,2,3]
# print(x[3])
# dict = {'name':'jslim','age':49,'city':'busan'}
# print(dict['hobby'])
# print(dict.get('name'))

# 예외가 없는것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외 처리 권장
# import time
# print(time.time2())
# 모든 에러들은 exception을 상속받고 ,exception은 object를 상속 받음

def userKeyIn() :
    try :   #예외가 발생할 수 있는 코드를 try에 기입
        age = int(input('본인의 나이를 입력하세요')) # input은 기본적으로 문자열로 입력됨
        # print('예외 발생 이후 code') #실행 안됨.  age~에서 에러 발생으로, except구문으로 바로 넘어가기 때문
    except ValueError as e : # as는 별칭을 주는것
           #IndexError as e :  # 에러가 다르면 정상적으로 예외를 잡을 수가 없음
           #Exception as e : # 다중 except를 안하고 Exception으로 한꺼번에 잡을 수 있다
        print('error = ',e)
    print('함수 실행 종료')

userKeyIn()

def userKeyIn() :
    try :
        age = int(input('본인의 나이를 입력하세요')) # input은 기본적으로 문자열로 입력됨
    except ValueError as e :
        print('etrror = ' ,e)
        # print('문자열이 아닌 정수를 입력해주세요')
        # userKeyIn()
    else :
        print('age - ',age)
        print('함수 실행 종료')
    finally:
        print('넌 너무 지조가 없다....항상 실행되니까 !!')
userKeyIn() # 비정상적 데이터를 넣으면, except와 finally 실행이 됨
            # 정상적 데이터를 넣으면, else와 finally가 실행이 됨

#test

nameList = ['kim','lee','park','lim']
try :
    name = 'jslim'
    idx = nameList.index(name) # .index 는 몇번째 index인지 찾는 함수
except ValueError as e :
    print('{} Not Found it !! '.format(name))
else :
    print('{} Found it !! {}'.format(name,idx+1))
finally:
    print('예외 여부와 상관없이 항상 실행되는 블럭')

print('프로그램 종료')

# 사용자 정의 예외 클래스를 작성
#raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고
#바로 except로 넘어갑니다.
class InsufficientError(Exception) : # 내가 원하는 exception 메세지를 지정해줄 수 있음
    def __init__(self,msg):
        self.msg = msg

# 클래스에 정의된 함수에 예외처리 적용 및 강제 예외 발생
class Account :
    def __init__(self,account,balance,interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def withDraw(self,amount):
       try:
           if self.balance < amount :
                raise InsufficientError('잔액이 부족합니다~!')     #에러를 일부로 발생시킨다는 뜻
       except Exception as e :
           print('error msg - ', str(e))
       else:
           self.balance -= amount

    def withDraw02(self,amount):
           if self.balance < amount :
               raise InsufficientError('잔액이 부족합니다~!')
           else:
              self.balance -= amount

account = Account('100',100000,0.073)
account.withDraw(200000)
print('프로그램종료 ')


account = Account('100',100000,0.073)
try :
    account.withDraw02(200000)
except InsufficientError as e :
    print(str(e))
print('프로그램종료 ')

'''
객체생성? - 클래스를 생성해야함
But, 
클래스 없이 객체를 생성하는 방법(변수)
usage)
collections.namedtuple( '클래스 이름' , (변수) [변수]  )

'''
import collections

Person = collections.namedtuple('Person', ['name','id']) # Person 클래스 생성 리스트 형식
Person = collections.namedtuple('Person', 'name id') # 튜플 #name id 사이에 공백
Person = collections.namedtuple('Person', 'name, id') # string형식 # name id 사이에 콤마
Emp = collections.namedtuple('Person', 'name, id') # string형식 # name id 사이에 콤마
# Emp는 클래스의 별칭, 'Person'이 문법상 실제 class이름에 들어가게 됨

per = Emp('jslim','100') # 인스턴스 생성
print(per)

# 각각의 속성에 접근?
print(' idx 0 - ', per[0])
print(' idx 1 - ', per[1])

# for in ?
for idx in range(len(per)) :
    print('idx {} - {}'.format(idx,per[idx]))

# 속성에 접근 2
print(per.name)
print(per.id)

# 속성에 접근 3
(name,id ) = per
name,id = per

print(name,id)

'''
1. 직장인 이름, 나이 ,부서를 속성으로 갖는 클래스 
2. 직장인 이름, 나이 ,부서를 속성으로 갖는 클래스를 namedtuple 만들어보자
'''

class Data01 :
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department

Emp = collections.namedtuple('Emp' , 'name, age ,department')

data03 = Emp('ysw','27','market')
print( data03)
