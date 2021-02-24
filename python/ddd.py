class Person(object):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address =address
    def perInfo(self):
        return self.name + "\t" + str(self.age) + "\t" + self.address
    # 전체를 문자열로 넘길때는, 그 안에 있는 전체 요소가 문자열이여야 오류가 안남

# super() : 부모의 인자들을 호출하는 함수
class StudentV0(Person):
    def __init__(self,name,age,address,stuId): # stuID는 StudentV0만의 고유 인자 요소 생성
        super().__init__(name,age,address) # 부모의 생성자 호출
        self.stuId = stuId
    def stuInfo(self):
        return super().perInfo()+ "\t" + self.stuId

class TeacherV0(Person) :
    def __init__(self,name,age,address,subject):
        super().__init__(name,age,address)
        self.subject = subject
    def teaInfo(self):
        return super().perInfo() + "\t" + self.subject

def typeChecker(func) :
    def wrapper(digit01,digit02) :
        if type(digit01) != int or type(digit02) != int :
            print('only integer support')
        else :
            pass
    func()
    return wrapper

@typeChecker
def div(digit01,digit02) :
    return div
div()


div(1,1)


# class - 데코레이터 적용

def tagH1(func) : # 장식자 함수 생성
    def wrapper(*args,**kwargs) :
        return '<h1>{}</h1>'.format(func(*args,**kwargs))
    return wrapper

class Per (object) : # 부모 함수 생성
    def __init__(self,name):
        self.name = name
    @tagH1 # 데코레이터 활용
    def getName(self):
        return self.name

per = Per('jslim')
print('per - ',per.getName())

class Calc01(object)  :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return  self.x + self.y
    def substract(self):
        return  self.x - self.y
class Calc02(object)  :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return  self.x + self.y
    def multiply(self):
        return  self.x * self.y

class UserCalc :
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cal02 = Calc02(x,y)
    def add(self):
        pass

def userKeyIn() :
    try :
        age = int(input('본인의 나이를 입력하세요'))
        print('예외 발생 직후 code')
    except Exception as e :
        print('error ', e)
    print('함수 실행 종료')

nameList = ['kim','lee','park','lim']
nameList.index('park')

try :
    name = str(input('이름을 입력하세요'))
    idx = nameList.index(name)
except Exception as e :
    print('{} Not found '.format(name))
else :
    print('{} found it, {}번쨰 index'.format(name),idx)
finally:
    print('함수 실행이 종료되엇습니당')

class InsufficientError(Exception) :
    def __init__(self,msg):
        self.msg = msg

class Account :
    def __init__(self,account,balance,interestRate):
        self.Account = Account
        self.balance = balance
        self.interestRate = interestRate

    def withDraw(self,amount):
        try:
            if self.balance < amount :
                raise InsufficientError('잔액이 부족합니당')
        except Exception as e :
            print('error msg - ',str(e))
        else:
            self.balance -= amount

    def withDraw2(self,amount):
        if self.balance < amount :
            raise InsufficientError('잔액이 부족합니다')
        else :
            self.balance -= amount

account = Account('100',100000,0.23)
account.withDraw(200000)


def fileStream(fileName, mode ) :
    if mode == 'w' :
        pass
    elif mode == 'r' :
        with open(file=fileName, mode=mode) as file :
            line = file.read()
            print('result read - ', line)
    elif mode == 'a' :
        pass

    else :
            raise Exception('모드를 확인하세요')

fileStream('hello.txt','asdf')

scores = {'kor' : 90 , 'eng' : 95, 'math' : 70, 'scien' : 82 }

def pickleWriter() :
    with open(file = 'dict.txt',mode = 'w', encoding='utf-8') as file :
        for key,value in scores.items()  :
            file.write('{} - {} '.format(key,value))
    print('저장완료')
pickleWriter()

import pickle
def pickleWriter02() :
    with open(file='dictPickle.txt',mode='wb') as file :
        pickle.dump(scores,file)
    print()

def pickleReader() :
    with open(file='dictPickle.txt',mode='rb') as file :
        dictScores = pickle.load(file)
        print('파일ㄹ됭 - ',dictScores,type(dictScores))

def cnt01() :
    count = []
    with open(file='./word/cnt_words.txt',mode='r',encoding='utf-8') as file :
        fileName = file.readlines()
        for word in fileName :
            if len(word.strip('\n')) <= 10 :
                count.append(len(word))
                print(count)
    print('{}'.format(len(count)))


cnt01()

def searchAddFunc() :
    dong = input('찾는 동을 입력하세요 : ')
    with open(file='./word/zipcode.txt',mode='r',encoding='utf-8') as file:
        line = file.readline()
        while line :
            address = line.split('\t')
            print('debug - ',address,type(address))
            if address[3].startswith(dong) and address[3].endswith('동'):
                print('[' + address[0] + ']', address[1], address[2], address[3], address[4], address[5])
            line = file.readline()

searchAddFunc()

a = ['this', 'is' ,'python' ,'that', 'let', 'you',' hard study']
print(a[0:2])
print(a[:])
print(a[0:2])

b = 'hifsa dfa asfasfaf jlfjak !'
print(b.replace('df',''))

from datetime import *

today = date.today()
print('date - ',type(today),today.year,today.month,today.day)

inputNumber = int(input('Enter your digit(1 ~ 100 '))

def numFx() :
    inputNumber = int(input('Enter your digit(1 ~ 100 '))
    if inputNumber%2 == 0 :
        print('짝수')
    else : print('홀수 잆니다')
numFx()
number = 15
if number%3== 0 or number%5==0 :
    print('%d' % number)


year = int(input('년도를 입력하세요'))
if year%4== 0 and year%100 != 0 or year%400 ==0 :
    print(' %s ' % '윤년입니다')

else :
    print('not 윤년')

year = int(input('년도를 입력하세요 : '))
month = int(input('달을 입력하세요 :'))

year_month = [31,28,31,30,31,30,31,31,30,31,30,31] #윤년
leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31] #윤년이 아닌 해

year = int(input('년도를 입력하세요 : '))
month = int(input('달을 입력하세요 :'))
if year%4== 0 and year%100 != 0 or year%400 ==0 :
    print(year_month[month-1])
else :
    print(leap_year_month[month-1])

cnt = 0

for year in range(2020,2051,4) :
    cnt += 1
    print(year,end= ' ')
    if cnt%5 ==0:
        print()
# 아래 리스트에서 세 글자 이상의 단어만 출력해라
wordList = ['I','am','study','python','language','PYTHON','IF','for']

for word in wordList :
    if len(word) >=3 :
        print(word)
fileList = ['greeting.py','bool.py','intro.hwp','bigdata.doc','ai.doc']

cnt = []
for fileword in fileList :
    fileword = fileword.split('.')
    cnt.append(fileword[0])
print(cnt)
import random
ranNum = random.randint(1,10)

while True :
    guessNum = int(input("숫자를 입력하세요"))
    if ranNum == guessNum :
        print('맞추셨습니다')
        break
    elif ranNum > guessNum :
        print("더큰 숫자를 입력하세요")
    else :
        print('더 작은 수를 입력하세요')

def addSum(n) :
    if  n ==1 :
        return 1
    else :
        result = n + addSum((n-1))
        print('debug - ', result)
        return   result
print( 'n=5 -', addSum(5))
print(' n=100 -', addSum(100))


