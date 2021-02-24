
'''
oop의 특성
- 상속( is ~ a ) : 코드의 재사용성을 높일 수 있다.
- 다형성
- 은닉화
- 추상화
lib - has ~ a , is ~ a

__함수__ : 매직함수 background에서 실행됨.



'''



class Car :
    def __init__(self,name,door,cc):
        self.name = name
        self.door = door
        self.cc = cc
    def carInfo(self):
        print('%s 는 %d cc이고,문짝은 %d개입니다' % (self.name,self.cc,self.door))

# car01 = Car('GV70',4,2400)
# car01.carInfo()
# car01.함수
# car01.변수

# class Sup(object) :  # Sub가 object를 상속받는 형식
#     pass
# class Sub(Sup)
# object(최상위 class) - Sup - Sub
# Sub가 가장 많은 요소를 포함하고 있음, 부모의 기능을 확장,물려받을 수 있음

# Test
# class Parent(object) :
#     # 초기화 함수(=생성자)
#     def __init__(self,name,job):
#         self.name = name
#         self.job = job
#     def display(self):
#         return ('당신의 이름은 {} 이고 직업은 {] 입니다'.format(self.name,self.jop))
#
# class Child01(Parent) :
#     def __init__(self,name,job,age):
#         self.name = name
#         self.job = job
#         self.age = age
#     def childInpo(self):
#         return('당신의 이름은 {} 이고 직업은 {]이고 나이는 {}'.format(self.name, self.jop,self.age))
#
# class Child02(Parent) :
#     pass


# 상속 생성

class Person(object) :
    def __init__(self, name, age, address):
        self.name = name
        self.age  = age
        self.address = address

    def perInfo(self):
        return self.name + "\t" + str(self.age) + "\t" + self.address
         # 문자열 중간에 int 형 즉, 형(type)이 다른게 있으면 Error 발생한다.
                                                               # 따라서 casting 필요하다.
# super() - 부모의 생성자를 호출하는 작업
class StudentVO(Person) :
    def __init__(self, name, age, address, stuID): # 4개 중 3개는 부모에서 가져옴
        super().__init__(name, age, address) # 부모의 __init__ 생성자를 호출하는 행위, 자식에게 들어온 인자를 부모에게 assign 하는 행위
        self.stuId = stuID
    def stuInfo(self) :
        return super().perInfo() + "\t" + self.stuId # 부모의 함수인 perInfo를 가져오고 자식의 것인 stuID를 합친 것!
    def perInfo(self) : # 부모의 함수를 무시하고 나만의 함수를 재정의 하는 것
        return super().perInfo() + "\t" + self.stuId
class TeacherVO(Person) :
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject
    def teaInfo(self) :
        return super().perInfo() + "\t" + self.subject
    def perInfo(self) : # 부모 함수와 이름은 동일하나, 다른 기능을 하는 것
        return super().perInfo() + "\t" + self.subject
class ManagerV0(Person) :
    def __init__(self,name,age,address,dept):
        super().__init__(name,age,address)
        self.dept = dept
    def empInfo(self):
        return super().perInfo() + "\t" + self.dept
    def perInfo(self): # 다형성 : 같은코드지만, 다른기능을 하는 것
        return super().perInfo() + "\t" + self.dept

# encapsulation(은닉화)
# information hiding(정보 은닉)  __ (캡슐화)

# 사용자 정의 함수

class MyDate(object) :
    def setYear(self,year):
        if year < 0 :
            self.__year = 2021 #이 inst는 외부에서 접근이 불가함
        else :                  # 따라서 set Year 함수를 통해 간접적으로 접근이 가능
            self.__year = year
    def getYear(self):
        return self.__year

'''
public vs private
instance variable - public 변경 private ? __instance variable
instance function - public 변경 private ? __instance function
'''

class HidingClass(object) :
    def __init__(self,name,dept,num):
        self.utype = self.__class__.__name__ # __name__ : 해당클래스의 타입을 확인할 수 있음
        self.name = name
        self.__dept = dept #private으로 설정된 변수는, return만가능함
        self.num  = num
    def getDept(self):
        return self.__dept
    def __getInfo(self):
        return "__로 시작했기 때문에 해당 함수는 외부에서 접근이 되지 않는다"

'''
다형성
상위 클래스에 정의된 함수를 하위클래스에서 해당 함수를 재정의(method overriding)
'''
# [실습]
# 1. Account class 작성 - account, balance, interestRate
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

class Account(object) :
    def __init__(self,account,balance,interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def accountInfo(self):
        return '{} 계좌번호의 현재 잔액은 {}원, 이자율은{}입니다'.format(self.account,self.balance,self.interestRate)

    def deposit(self,X) :
        self.balance += X
    def withDraw(self,Y):
        if self.balance > Y :
            self.balance -= Y
        else :
            print('잔액이 부족하여 출금을 할 수 없습니다.')
    def printInteressRate(self):
        print('%.2f' % str(self.balance + (self.balance * self.interestRate)))
# [실습]
# 1. Account class 작성 - account, balance, interestRate,
# 1-1. SavingAccount , FundAccount 추가 type(계좌종류 S | F
# 1-2.  |                       |
# 1.3.  -- printInterestRate()  -- printInterestRate()
# 1.4  SavingAccount - printInterestRate()
#      기본 이자율에 만기시 이자율을(0.1) 복리로 계산
# 1.5  FundAccount - printInterestRate()
#      기본 이자율에 잔액 10만원 이상이며 10%
#      기본 이자율에 잔액 50만원 이상이며 15%
#      기본 이자율에 잔액 100만원 이상이며 20%
class SavingAccount(Account) :
    def __init__(self, account, balance, interstRate, type):
        super().__init__(account, balance, interstRate)  # check
        # super()를 통해 instance값을 다시 입력안해도 됨#부모의 것을 가져오기 때문
        self.type = type
    def printInterestRate(self) :
            self.balance += self.interestRate * 0.1
            print(self.balance)



class FundAccount(Account) :
    def __init__(self, account, balance, interstRate,type):
        super().__init__(account,balance,interstRate) # check
        self.type = type

    def printInterestRate(self) :
        if 0 < self.balance < 100000 :
            self.balance += self.interestRate
            print(self.balance)
        elif self.balance < 500000 :
            self.balance += self.interestRate * 0.1
            print((self.balance))
        elif self.balance < 1000000 :
            self.balance += self.interestRate *0.15
            print((self.balance))
        else :
            self.balance += self.interestRate *0.2
            print((self.balance))



