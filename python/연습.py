from datetime import date, datetime

today = date.today()  # 오늘 날짜를 today란 변수에 저장
print(today.year,today.month,today.day,)
print(today)


todaytime = datetime.today() #시간까지 출력( 몇시 몇분 몇초)
print(todaytime)

area = ['서울','부산','제주','광주']
region = '수원'

if '광주' in area :
    pass
else :
    print('{}지역은 포함되지 않습니다'.format(region))

userSum = 0
for temp in range(1,11) :
    print(temp)
    userSum += userSum + temp
print('누적 값은 : {}입니다'.format(userSum))

userList = [(1,2),(3,4),(5,6)]
userSum = 0
print(type(userList))

for tem01, tem02 in userList : #2개씩 넣어줄 수 있음
    print(tem01,tem02,end=" ")
    userSum += tem01 + tem02
print('누적값은{}입니다.'.format(userSum))

userDict = {'name' : 'jslim','gender':'m'}
for key, value in userDict.items() : #items 함수는 키벨류 값을 호출
    print("{},{}".format(key,value))

class Employee :

    raiseRate = 1,1

    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

    def __repr__(self):
        return self.name + self.salary

    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다.'.format(self.name,self.salary)

    def updateRate(self,rate):
        self.raiseRate = rate
        print('인상률이 {}로 변경되었습니다.'.format(rate))

    def applyRaise(self):
        self.salary = int((self.salary * self.raiseRate))
emp01 = Employee('임정섭',1000)
print('인상 전 급여 - ', emp01.getSalary())

emp01.updateRate(1.5)
emp01.applyRaise()

print('인상 후 급여 - ', emp01.getSalary())