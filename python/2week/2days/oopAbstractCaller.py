
from ai.oop.oopAbstract import *

liger = Liger() # 인스턴스 생성
liger.play()
liger.cry() # 어흥이 출력, Tiger가 우선 실행

obj = Base() #추상클래스 이기에 인스턴스를 생성할 수 없음 error
obj.goToSchool()

stu =  Student() # 부모에 추상메서드가 있기때문에, error 인스턴스 생성 x
stu.study()