# python sequence type - tuple
# 순서, 중복 o, 수정 x 삭제 x #읽기전용, 수정과 삭제가 안된다는 점에서 list와 구별

myTuple = ("반도",'강철비2','아이언맨')
oneTuple = (1,)

#사용자의 편의를 위해서 괄호없이 만들 수 있음
myTuple = 1,2,3,4,5

multiTuple = (100,1000,'Ace','Base','Captine')
print('tuple print -', multiTuple)

#indexcing  시퀀스 형식이기 때문에 가능함
print('index 1 - ', multiTuple[1])
print('slicing -',multiTuple[2:],type(multiTuple[2:]))

#casting (형 변환 함수)
multiList = list(multiTuple[2:])
castingMultiTuple = tuple(multiList)

#python sequence type - range
# 1 ~ 99까지의 정수 중 짝수만 저장된 튜플을 생성한다면?

range01 = range(10)
print(range01)

range02 = range(1,11,2)
print(range02)

print(7 in range02)
print(10 in range02)
print(range02.index(7))  # 7이라는 값을 가진 index(순서가) 머냐?
print(range02[2])   # >>> 5
print(range02[2:])   #>>> 5,7,9,11
print(range02[-1])

even = tuple(range(2,100,2))     # range(2부터,100까지,2step)
print(even)

#even[0] = 1 # >>> error 수정과 삭제가 불가능한 tuple이기 때문에

range01 = range(1,11,2)
print(range01[-1]) >>>9

data1 = [1,2,3,4,5,6]
print(data1[-1])

