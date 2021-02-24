
# python set type - set(집합)
# 순서x 중복x 그렇기에, 인덱싱,슬라이싱 불가 -> casting을 통해 list,tuple로 변환하여 가능하게 할 수  있음
# {}
# set([]) set은 dict와 다르게 value 값으로만 이루어져있음 !

temp = {'jslim','teacher'}
print('set - ',temp,type(temp))

temp = set([1,2,3,4,5,5,5,5])
print('set -',temp,type(temp)) # 중복이 안됨

temp = set([1,3.14,'pen',False])
print('set -',temp,type(temp)) # 결과에 순서가 없음 # 파이썬 내 정해진 순서로 결괏값 출력됨
casting = tuple(temp)
print('casting -', casting, casting[1:3])

set01 = set([1,2,3,4,5])
set02 = set([3,4,5,6,7])

# 교집합 & == intersection, 합집합 | == union(), 차집합 - == difference()
#  set type만 가능 !
# 객체(변수, 함수)
# 객체.변수, 객체.함수() 형식으로 접근

print('교집합 &-', set01&set02)
print('교집합 intersection -',set01.intersection(set02))

print('합집합 |-', set01|set02)
print('합집합 union -', set01.union(set02)) # set은 중복을 허용하지 않기 때문에 중복 없이 결괏값이 나옴

print('차집합 - - ',set01-set02)
print('차집합 differnece - ', set01.difference(set02))

# 요소 추가 삭제(remove(), discard())
set01.add(7)
print('set add-', set01)

# set01.remove(9) #remove는 존재하지 않는 요소를 없애려고하면 오류가 생김
set01.discard(9) #discard는 오류를 무시하기 때문에, remove가 더 안정적

# set01  = [1,2,3,4] list도 remove 함수 가능
set01.remove(4)
print('set remove - ',set01)

# 중복제거용으로 활용할 수 있음
gender = ['홀','짝','짝','짝','홀','홀','짝','홀','짝'] #list 형식
setGender = set(gender) # set으로 변환, 중복을 없애기 위해
print('remove - ',setGender,type(setGender))
listsetGender = list(setGender) # 슬라이싱, 인덱싱 하기 위해 다시변환
print('list casting - ',listsetGender,type(listsetGender))
print('list casting - ',listsetGender[0])

