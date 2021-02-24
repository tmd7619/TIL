# 변수 정의 및 생성
#블럭단위 실행 단축키 쉬프트 알트 E



intValue = 123
floatValue = 3.14
boolValue = True
strValue = 'jslim'
print()
print(type(intValue), type(floatValue), type(boolValue),type(strValue))

# type casting
numStr = "720"
numNum = 100
print(numStr + numNum) # >>> TypeError #같은 Vaulue끼리만 연산이 가능
print(int(numStr) + numNum) # >>> 820
print((numStr) + str(numNum)) # >>> 720100

# list
listAry = ['python','anacaonda']
print(type(listAry))

# dict {} # 키벨류로 이루어진 {} 키 + 벨류
dictValue = {
    "name" : "machine Learning",
    'version' : 2.0
}
print(type(dictValue))

# tuple ()  요소의 값이 하나일 경우 int형으로 나오기 때문에, 반드시 뒤에 ,찍음

tupleValue = (3,)

# set {} key값만 존재한다는 점에서, dict와 차이
setValue = {3,5,7}
print(type(setValue))

# keyboard input
#function syntax
'''
보통 함수 정의 문법은,
접근지정자 리턴타입 함수명(매개변수){

}

python funcion은 
def sum() : 
    statement
'''
# input() 기본적으로 입력되는 값을 str로 지정함

inputNumber = input('숫자를 입력하세요 : ')
print(inputNumber)

# 문자형(str)

str01 = 'I am Python'
str02 = "python"
str03 = """this is a
multiline
sample text"""

#데이터의 종류 : 정형, 비정형 ,반정형

seqText = 'Talk is cheap. Shhow me the code'

print(seqText)

# dir()
print(dir(seqText))

# slicing
print(seqText[3])  # 0번쨰 T부터 해서, 3번째 단어 k print
print(seqText[-1]) # 맨뒷자리
print(seqText[0:4]) # >>> Talk
print(seqText[-6: ]) # 뒤에서 6번쨰 코드를 start로 잡고, 콜론뒤에 공백은 맨 끝까지
print(seqText[ : : 2]) #step
print(seqText[ : : -1])

string = '홀짝홀짝홀짝홀짝홀짝' # '홀'만 출력해라
print(string[::2])
# console 오류시, stop console 후 rerun 실행

#문자열 조작을 위한 많은 내장 함수를 제공하고 있다.
string1 = 'python' # 앞 문자를 대문자로 출력해라
print("Capitalize : ", string1.capitalize())

# 문자치환 replace(oldchar, newchar)
phoneNumber = '010-3231-3232'

replacepho = phoneNumber.replace('-',"")

string = 'abcdef234asf2'
print(string.replace('a','A'))

# 문자열을 쪼개는 함수 : split()

url = "http://www.naver.com"
urlSplit = url.split('.') # .을 기준으로 쪼개짐
print(urlSplit,type(urlSplit)) # list 형식
print('domain : ' , urlSplit[-1])

# 문자열에서 공백 제거 함수 : strip()양쪽 공백 제거 , rstrip(), lstrip()
# 대문자, 소문자 변환 함수 : upper(), lower()
comname = '    samsung    '
print(comname.strip() , len(comname.strip())) # len()는 변수의 길이를 알려줌
print(comname.rstrip() , len(comname.rstrip())) #right쪽의 공백 제거
print(comname.lstrip() , len(comname.lstrip())) #left쪽의 공백 제거
print(comname.upper()) # 모든 글자 대문자로 변환

# endswith(), startwith() #문자열 확인하기
fileName = 'report.xls'
isExits = fileName.endswith(('xls','xlsx','csv')) # xls xlsx csv로 끝나는 문자열 있는지 확인

print(isExits,type(isExits)) # >>> True

# in, not in -> True | False #해당 문자열에 ~문자가 있냐 없냐
myStr = 'this is a sample Text'
print("sample" in myStr)
print("text" not in myStr) #대소문자를 구분하기 때문에, 결과는 True

print('this' in myStr.lower()) #myStr를 lower()를 이용해 소문자로 변환뒤, 문자열 판별

#문자의 빈도 count(), 문자 찾기 find(), 문자의 인덱스 index()

brandname = 'cocacola'
print(len(brandname),brandname.find('a')) #>>> 최초로 만나는 index 값을 리턴해줌
print(len(brandname),brandname.index('a'))  ?
