
'''
Unit (Marine,Medic,DropShip)
Marine - 4명
Medic - 2명
DropShip -6명을 태워서 특정 지점을 공격하러 가는 시나리오
'''

class Unit(object) :
    def __init__(self,damage,life):
        self.utype = self.__class__.__name__ # 문자열로 템플릿의 type 확인할 수 있음
        self.damage = damage
        self.life = life
    def unitInfo(self):
        print('타입{}'.format(self.utype))
        print('공격력{}'.format(self.damage))
        print('생명력{}'.format(self.life))
    def attack(self):
        pass
class Marine(Unit) :
    def __init__(self,damage,life,offenseUpgrade,defenseUpgrade):
        super().__init__(damage,life) # 부모의 damage,life를 참조하겠다
        self.offenseUpgrade = offenseUpgrade
        self.defenseUpgrade = defenseUpgrade
    def unitInfo(self): # 다형성 부모꺼를 가져오되, 수정가능
        super().unitInfo()
        print('공격력 업그레이드{}'.format(self.offenseUpgrade))
        print('방어력 업그레이드{}'.format(self.defenseUpgrade))
    def attack(self):
        print('마린이 공격한다...')
    def stimpack(self):
        if self.life > 50 :
            self.damage += 1.5
            self.life -= 10
            print('스팀팩 사용')

        else :
            print('체력이 낮아 stimpack 사용 불가!')

class Medic(Unit) :
    def __init__(self,damage,life,defenseUpgrade):
        super().__init__(damage,life)
        self.defenseUpgrade = defenseUpgrade
    def unitInfo(self):
        super().unitInfo()
        print('방어력 업그레이드{}'.format(self.defenseUpgrade))
    def attack(self):
        print('메딕이 마린을 치료합니다다')
class DrpShip(Unit) :
    def __init__(self, damage, life, defenseUpgrade):
        super().__init__(damage, life)
        self.defenseUpgrade = defenseUpgrade

    def attack(self):
        print('목표지점으로 이동합니다')
    def board(self,unitType):
        self.unitType = unitType
        print('부대원을 태웠씁니다.')
    def drop(self):
        print('모든 부대원을 Drop하겠습니다')
        return self.unitType