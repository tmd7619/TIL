
# control statement
# if (조건문), for (반복문), while(반복문)

# 사용자 입력 함수
# input()

name = input("Enter your Name : ")
grade = input("Enter your Grade :")
company = input("Enter your Company :")
print(name,grade,company)

# if , if~ else , if ~ elif ~ esle
# bool True | False
'''
other)
if(조건식){
    true
}
else{
    false
}

python)
if True(not False) :
     
'''
# 입력되는 값이 짝수인지 홀수인지를 판별하여야 한다면? if구문
inputNumber = int(input("Enter your digit(1 ~ 100 : "))
print(inputNumber%2 == 0)

if inputNumber%2 == 0 :
    print('짝수입니다')
else :
    print("홀수입니다")

if True :                       # True문장에 아무것도 안넣을때 pass입력
    pass

number = 15
# 위 값이 3의 배수인지 5의 배수인지를 판별하고 싶다면
if (number%3==0 or number%5 == 0) : #if 뒤에 ()넣어도 상관 x
    print('{}은 3과 5의 배수입니다.'.format(number))
else :
    print('{}은 3과 5의 배수가 아닙니다.'.format(number))

# if ~ elif

if number%3==0 :
    print('{}은 3의 배수입니다'.format(number))
elif number % 5 ==0:
    print('{}은 5의 배수'. format(number))
else :
    print('{}은 3과 5의 배수가 아닙니다'.format(number))

year = 2020
# 윤년의 조건
# 4의 배수이고 100의 배수가 아니거나
# 400의 배수일 때를 윤년으로 본다면

if year%4 ==0 and year%100 !=0 or year%400 == 0 :
    print('{}는 윤년'.format(year))
else :
    print('{}는 윤년이 아니다.'.format(year))

#if 구문을 이용하여 년도와 월을 입력받아서 월의 마지막 일을 출력한다면?
year = int(input('년도를 입력하세요 : '))
month = int(input('달을 입력하세요 :'))

year_month = [31,28,31,30,31,30,31,31,30,31,30,31] #윤년
leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31] #윤년이 아닌 해

if year%4 == 0 and year%100 !=0 or year%400 == 0 :
    print('{}년{}월의 마지막 일은 {}입니다'.format(year,month,year_month[month-1])) # 0번째 인덱스를 1월로 맞추기 위함
else :
    print('{}년{}월의 마지막 일은 {}입니다'.format(year,month,leap_year_month[month-1]))


# dict을 이용한 방법 # 성공

year = int(input('년도를 입력하세요 : '))
month = int(input('달을 입력하세요 :'))
days = {1: '31',2: '28',3:'31',4:'30',5:'31',6:'30',
        7:'31',8:'31',9:'30',10:'31',11:'30',12:'31'
}


if year%4 == 0 and year%100 !=0 or year%400 == 0 :
    print('{}월의 마지막 일은 {} 입니다 '.format(month,days.get(month)))
elif month ==2 :
    print('2월의 마지막 일은 {} 입니다 '.format(29))
else :
    print('{}월의 마지막 일은 {} 입니다 '.format(month,days.get(month)))


#  if ~ in : 만약에 ~에 ~가 존재하냐?
area = ['서울','부산','제주','광주'] #lsit 를 이용함
region = '수원'
if '광주' in area :
    pass
else :
    print('{}지역은 포함되지 않습니다'.format(region))


areaKeyDict = {'서울' : 100, '광주' : 200} # dict를 이용함
region = '부산'
if region in areaKeyDict : #부산이라는 key 가 있니? #
    pass
else :
    print('{}값이 존재하지 않습니다'.format(region))

city = ''           #파이썬은 비어있는것을 False로 간주하기 때문에, 가능한 구문이 됨
if city :
    print(city)
else :
    print('please enter your city')

# 삼항 연산자
num = 9
result = 0

result =  num * 2  if num > 5  else num + 2
print('삼항 연산자 -', result, type(result))

# & == and 동일?
'''
and (논리연산자,True | False 연산)
-> x and y , x 가 False면 x 값을 반환하고
-> x가 True면 y의 값을 반환합니다.


&(비교,bitwise)

if 구문에서는 and 와 or를 쓰도록 권장.
'''