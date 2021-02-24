#Numeric(숫자, 정수, 실수)

a = 123
b = 3.14
c = 3.41E10
e = 0o34 # 8진수
f = 0xAB # 16진수

# type()
print(type(a))
print(type(b))
print(type(c))

div = 3/4
print(div)

result = 3 **3
print(result)

resunt = 10 % 3 #나머지

result = 10 // 3 # 나머지 제거 후 몫


'''
Sequence - list
임의의 값을 순서대로 저장하는 집합 자료형 (index 부여 및 값 변경 가능한 형식)
함수를 이용하는 방법과 [] 를 이용하는 방법이 있다.
range() 이용하여) 리스트를 생성하는 방법이 있다.
'''

'''
a = []          #list를 생성하는 방법
print(type(a))

a = list()
print(type(a))

a = [1, 2 ,3]
print(a)
'''

# indexing
print(a[0])  # >>> 1 # 0이 첫번째
print(a[1])  # >>> 2
print(a[2])  # >>> 3
print(a[3])  # error out of range
print(a[-1]) # >>> 3 # 맨뒤에서부터 indexing

# slicing
print(a[0:2]) # >>> [1,2]
print(a[1:2]) # >>> [2]
print(a[2:3]) # >>> [2,3]
print(a[0:2]) # >>> [1,2]

a = [1,2,'hello',3.14] #리스트 안의 타입이 여러 종류여도 상관없음
a = [1,2,['show','me','the','money'],3.14]

print(a[2][2:]) # the money 만 슬라이싱

a = [1,2,3,]
b = [4,5,6,]
print(a+b)
print(a*3)

print(a)

print(a[0])
a[0] = 5
print(a)


year = 2021
month = 1
day = 4
print(year,month,day) # print는 ,를 통해 여러개의 변수값을 동시에 출력가능

str = 'python start!!'
print(type(str))

a = ()
print(type(a)) # >>> tuple
a = (1) # 튜플 x 뒤에 반드시 ,를 붙어야함

a = (1,2,3)
print(type(a))