
# python 객체지향 프로그래밍 (oop)

'''
패키지 (pacakge) > 모듈(module) > 클래스(class) > 함수(function)
object oriented programming (OOP)

Real Word            추상화              P/G
Object ------------- class------------- >instance
- 명사적 특징 -------변수
- 동사적 특징 -------함수

instance는 class를 통해 생성되는데, 실제 메모리상에 저장되는 것을 말함.

'''

# 학생의 정보를 저장하려고 할때
stuName = 'ㅇㅇㅇ'
stuMajor = '컴공'
stuId = '1992'
stuGrade = 4.5

# 다수의 학생의 정보를 저장하려 한다면? ->list,dict활용  # 시간이 너무 많이 소요되고, 비효율적임

# 따라서 class를 이용해, 한 학생의 데이터를 논리적인 하나의 단위로 묶어 사용
'''
class vs instance
namespace : 객체를 인스턴스화 할때 저장된 공간
class variable : 직접 접근가능 및 공유
instance variable : 객체소유로 별도 존재

self - class의 소유가 아닌 instance 소유의 멤버라는 걸 명시한다

class
- 함수의 모임
- 역할 : 여러개의 함수와 데이터를 묶어서 객체 생성할 수 있는 템플릿
- 구성 : 멤버 = 변수(데이터) + 메서드(함수), 생성자(초기화)
- 형식 : class 클래스이름 : 
            변수             - 자료 저장
            초기화           - 객체생성시 호출되는 함수
            def 함수이름() : - 자료처리
'''
# class의 첫번째 letter는 대문자로 정의해주는 것이 좋다 !
class Calc :
    x = 0
    y = 0

    def __init__(self):
        print('객체 생성시 호출되는 함수이고 난 초기화라고 불리죠^_^')
    def plus(self):
        print('사용자 정의 함수이고 전 인스턴스의 소유가 됩니다')

# class의 instance를 생성하는 문법
obj = Calc()
obj.plus()

'''
user define function
- setXXXX
- getXXXX
- isXXXX

'''
class Student :
    def __init__(self,name,major,num,grade) : # 초기화함수 설정 #self는 인자가 아님!
        self.name = name # 변수에 self가 붙게 되면, instance 소유가 됨
        self.major = major
        self.grade = grade
        self.num = num
    def __repr__(self): # 문자열로 보여주기 위해 내장함수인 repr 사용
        return self.name + "\t" + self.major + "\t" +self.num + "\t"+ self.grade
    def getInfo(self):
        return '이름 : {} \t 전공 : {}'.format(self.name,self.major) #이름과 전공만 출력
stu01 = Student('윤승원','경영','1995','4.5') # stu01이란 변수에 Student 클래스 호출
print('stu01 address - ', stu01)
print(stu01.name)
print(stu01.grade)
print(stu01.major)
print(stu01.num)

stuList = []
stu01 = stuList.append(Student('임정섭','철학','1992','4.5'))
stu02 =stuList.append(Student('윤승원','경영','1992','4.5'))
stu03 =stuList.append(Student('섭섭해','영어','1992','4.5'))
for stu in stuList :
    print(stu.getInfo())

print(id(stu01),id(stu02),id(stu03))


# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수
# namespace ( instance -> class -> super class )
class Student :
    schlarshipRate = 3.5 # class variable(클래스 소유)#self 가 없기때문에 inst 소유 x
    def __init__(self,name,major,num,grade) : # 초기화함수 설정 #self는 인자가 아님!
        self.name = name # 변수에 self가 붙게 되면, instance 소유가 됨
        self.major = major
        self.grade = grade
        self.num = num
    def __repr__(self): # repr : 문자열로 나타내주는 내장함수
        return self.name + "\t" + self.major + "\t" +self.num + "\t"+ str(self.grade)
    def getInfo(self):
        return '이름 : {} \t 전공 : {}'.format(self.name,self.major)
    def isSchoarShip(self):
        if self.grade >= Student.schlarshipRate :  #클래스의 소유는 클래스.~ 로 접근해야함
            return True
        else :
            return False
#test
stu01 = Student('이중현','기계공학','2010',4.0)
print('장학금 여부 -',stu01.isSchoarShip(),Student.schlarshipRate)

#  인스턴스 소유가 아닌 class method
'''
self x
클래스 함수는 cls인 인자를 받고 모든 인스턴스가 공유하는 클래스 변수와
같은 데이터를 생성, 변경 또는 참조하기 위해서 사용됩니다.
'''
#test 인상 전 급여 -> 인상률 변경 -> 인상 후 급여 print

#
class Employee :

    raiseRate = 1.1 # 급여인상률 # class variable

    def __init__(self,name,salary) :
        self.name = name   # 인스턴스에 담지 않으면 메모리 저장력이 약함
        self.salary = salary
    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다.'.format(self.name,self.salary)

    @classmethod # 이부분을 입력을해야, class 메서드가 올바르게 작동할 수 있음
    def updateRate(cls,rate):   # self 소유가 아닌 class 소유이기에, cls 입력
        cls.raiseRate = rate
        print('인상률이 {}로 변경되었습니다.'.format(rate))

    def applyRaise(self):
        self.salary = int(self.salary * Employee.raiseRate) # 실수형으로 값이 나와 오류가 날 수 있기 때문에, int형으로 변환

    # static 함수 : cls, self를 갖지 않는 일반적인 함수
    @staticmethod # 스태틱함수라고 명시를 해줘야함.
    def isValid(salary):
        if salary < 0 :
            print('음수가 될 수 없습니다')

emp01 = Employee('임정섭',1000)  # inst 소유
print('인상 전 급여 - ', emp01.getSalary())

Employee.updateRate(1.5) # class 소유
emp01.applyRaise() # 함수 호출

print('인상 후 급여 - ', emp01.getSalary())

Employee.isValid() # 스태틱함수 호출

# 스태틱과 클래스 함수 다른점?
# 다를게 거의 없지만, namespace가 다름