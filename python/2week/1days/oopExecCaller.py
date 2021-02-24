
from ai.oop.oopExec import *

unit = Unit(10, 100)
unit.unitInfo()

if unit.utype == 'Unit' : # type 체크
    print(True)

else :
    print(False)

# Marin 생성
marine01 = Marine(10,100,0,0)
marine02 = Marine(10,100,0,0)
marine03 = Marine(10,100,0,0)
marine04 = Marine(10,100,0,0)

# Medic 생성
medic01 = Medic(0,100,0)
medic02 = Medic(0,100,0)

# 병력을 list 에 담기
troopList = []
troopList.append(marine01)
troopList.append(marine02)
troopList.append(marine03)
troopList.append(marine04)
troopList.append(medic01)
troopList.append(medic02)

# 기본 정보 출력

for obj in troopList :
    obj.unitInfo()
    #print(obj.unitInfo())# return타입이 아닌 함수를 run 하게 되면, none이라는 값이 나오게 됨
    print("*"*50)

# DropShip 생성
ship = DrpShip(0,50,0)

# 부대원을 태운다면?
ship.board(troopList)

# 공격 목표지점으로 이동?
ship.attack()

# 부대원을 내린다면?
troopAttackList = ship.drop()
# 공격
for unit in troopAttackList :
    if isinstance(unit,Marine) : #주어진 인스턴스가 특정 클래스/데이터 타입인지 검사해주는 함수
        unit.stimpack()
    unit.attack()