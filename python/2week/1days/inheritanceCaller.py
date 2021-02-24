# car01 = Car('GV70',4,2400)
# car01.carInfo()

from ai.oop.oop_inher import * #* : 패키지 내에 모든 모듈을 불러오겠다


parent = Person('부모','공무원','seoul')
print('parent - ',parent.perInfo())

stu01 = StudentVO('윤승원',49,'seoul','2014')
print('stu info - ',stu01.stuInfo())
print('perinfo - ',stu01.perInfo())


tea01 = TeacherVO('섭섭해',49,'seoul','python')
print('tea info - ',tea01.teaInfo())

emp01 = ManagerV0('장호연',29,'seoul','HRD')
print('emp info - ',emp01.empInfo())

userDate = MyDate()
userDate.setYear(-2021)  # 연도는 - 값이 나올 수 없기 때문에, year이란 변수를 중요하게 생각하고
print(userDate.getYear()) # 외부에서 직접적인 접근이 불가능 할 수 있게 hiding을 함


hiding = HidingClass('홍길동','교육팅',100)
print('utype - ', hiding.utype)
print('name - ', hiding.name)
# print('dept - ', hiding.__dept)
print('num - ', hiding.num)
print('call getDept - ',hiding.getDept())
# print('call getInfo - ',hiding.__getInfo()) # private 때문에 오류

# 다형성
stu01 = StudentVO('윤승원',49,'seoul','2014')
tea01 = TeacherVO('섭섭해',49,'seoul','python')
emp01 = ManagerV0('장호연',29,'seoul','HRD')
perList = []
perList.append(stu01)
perList.append(emp01)
perList.append(tea01)
print(perList)  # information 확인

for obj in perList :
    # if isinstance(obj,StudentVO) : # 다형성을 적용하지 x을때
    #     print(obj.stuInfo())
    # elif isinstance(obj,TeacherVO) :
    #     print(obj.teaInfo())
    # else :
    #     print(obj.empInfo())
    print(obj.perInfo()) # 다형성 적용 더욱 간결한 coding이 가능해짐

# Account Caller
from ai.oop.oop_inher import *
account = Account('441-2131-231',500000,0.073)
account.accountInfo()
account.withDraw(300000)

account.deposit(200000)
account.accountInfo()
print(account.withDraw(600000))
account.accountInfo()
print('현재 잔액의 이자를 포함한 금액')
account.printInteressRate()

account = SavingAccount('441-2131-231',500000,0.073,'S')
account.printInterestRate()


account = FundAccount('441-2131-231',500000,0.073,'F')
account.printInterestRate()



