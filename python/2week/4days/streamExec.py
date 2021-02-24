
'''
binary 형식의 입출력
- 바이너리 파일은 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로
인코딩된 파일을 가리킵니다.
프로그램이 이 파일의 데이터를 읽거나 쓸 때는
데이터의 어떠한 변환도 일어나지 않습니다.
텍스트 파일은 사람이 알아볼 수 있는 문자열로 이루어진 파일을 가리킵니다.

- 객체직렬화(Serializable) -> 파일저장

- pickle -객체직렬화를 도와주는 모듈
'''

scores = {'kor' : 90 , 'eng' : 95, 'math' : 70, 'scien' : 82 }
print(type(scores))

# scores 객체 정보를 xxxx.txt 파일로 저장
def pickleWriter() :
    with open(file='dict.txt',mode='w',encoding='utf-8') as file :
        for (key,value) in scores.items() :
            file.write('{} - {} \n'.format(key,value))
    print('저장완료')

pickleWriter()


# 파이썬 객체를 파일에 저장하는 피클링
# 객체를 text형식으로 저장 및 불러드릴 수 없기 때문에, 바이너리 형식으로 해야함
import pickle
def pickleWriter02() :
    with open(file='dictPickle.txt', mode='wb') as file:
        pickle.dump(scores,file) # scores를 file로 저장하겠다
    print('객체 직렬화를 통한 파일 저장')

pickleWriter02()

# 파일에서 파이썬 객체를 읽어오는 언피클링

def pickleReader():
    with open(file='dictPickle.txt', mode='rb') as file:
       dictScores =  pickle.load(file)
       print('파일 로딩 - ',dictScores,type(dictScores))
    print('객체 직렬화를 통한 파일 저장')

pickleReader()

''' 
<실습 1>

#단어가 줄단위로 저장된 cnt_words.txt 파일에서 10자이하인 
단어의 갯수를 카운트하는 함수를 구현하고 호출한다면?
'''
#file.readlines() 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소로 들어간다
#file.readline()  파일 내용을 처음부터 주루룩~ 읽어나가다가 '\n'이 나타나면 종료 ( 한줄만 나옴)
#file.read() 파일 전체의 내용을 하나의 문자열로 읽어온다. (str형식)

def cnt01() :
    count = []
    with open(file='./word/cnt_words.txt',mode='r',encoding='utf-8') as file :
        fileName = file.readlines()
        print(type(fileName))
        for word in fileName: # 이때 word는 str 형식 why? fileName은 리스트형식인데, 리스트 안에 str로 되있기 때문
            print(type(word))
            if len(word.strip('\n')) <= 10 : # strip함수는 문자열(str)일때 사용 가능
                count.append(word)
    print('{}'.format(len(count)))
cnt01()

def wordCntFunc() :
    wordList = []
    with open(file='./word/cnt_words.txt',mode='r',encoding='utf-8') as file :
        for word in file.readlines() :
            word= word.strip('\n')
            print('word - ',word)
            if len(word) <= 10 :
                wordList.append(word)
    print('10자 이하의 단어의 갯수는 {}개입니다'.format(len(wordList)))
wordCntFunc()

'''
<실습 2>
special.words.txt 파일에서
'c'가 포함된 단어를 출력하는 함수를 만들어서 호출한다면?
주의) 단어를 출력할 때는 등장한 순서대로 출력하며 ,.은 출력하지 않는다
'''

def specialWord() :
    with open(file='./word/special_words.txt',mode='r',encoding='utf-8') as file :
        words = file.read().split() # split 함수로 인해 나누어진 값들은 리스트의 요소로 저장
        print(words)
        for word in words :
            if 'c' in word :
                print(word.strip(',.'))
specialWord()

'''
실습 3 
zipcode.txt
input()을 이용해서 동 이름을 입력받아
입력예시) 개포
해당하는 동의 주소를 출력하는 함수를 정의하고 호출한다면 ?
-startswith(),endwith()
'''

def searchAddFunc() :
    dong = input('찾는 동을 입력하시용 :')
    # print('debug - ', dong
    with open(file='./word/zipcode.txt',mode='r',encoding='utf-8') as file :
        line = file.readline() # split 함수를 쓰기위해, str로 저장
        while line  :
            address = line.split('\t')
            print('debug - ',type(address)) # list형식
            if address[3].startswith(dong) and address[3].endswith('동') :
                print('['+address[0]+']',address[1],address[2],address[3],address[4],address[5])
            line = file.readline() # Question ??

searchAddFunc()

'''
csv, excel 파일은 -> pandas lib 사용
- pip install pandas
- conda install pandas
- service_bmi.csv
- DataFrame 

'''
'''
from 모듈 import 함수 
import 모듈 as 별칭 
# 모듈(module)은 각종 변수, 함수, 클래스를 담고 있는 파일이고,
# 패키지(package)는 여러 모듈을 묶은 것입니다.

모듈: 특정 기능을 .py 파일 단위로 작성한 것입니다.

패키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다. 
패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공합니다.

파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서 
파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.
'''

import pandas as pd # pandas 패키지 설치하고, pandas 모듈 불러서 pd로 지정
bmiDataset = pd.read_csv('./word/service_bmi.csv' , encoding='utf-8')
print(bmiDataset.info())
print(bmiDataset.head()) # 상위 5개 데이터 불러들임
print(bmiDataset.tail()) # 가장 마지막 5개 데이터 불러들임

#속성에 대한 접근 - Series
print(bmiDataset.height,type(bmiDataset.height)) #type은 series, R의 vector라고 생각하면 됨
print(bmiDataset['weight'])
print(bmiDataset['label'])

print('키 avg{}, 몸무게 avg{}'.format( sum(bmiDataset.height)/len(bmiDataset.height),
      sum(bmiDataset['weight'])/len(bmiDataset['weight'])))

# 키 최대 / 몸무게 최대
print('max - ' , max(bmiDataset.height))
print('max - ' , max(bmiDataset.weight))

# label의 빈도수를 구한다면?

labelCnt = {}
for label in bmiDataset.label :
    # print(label)
    labelCnt[label] = labelCnt.get(label,0) + 1 # Question ??
print(labelCnt)

'''
spam_data.csv
'''
spamDataset = pd.read_csv('./word/spam_data.csv' , encoding='utf-8')
print(spamDataset) # UnicodeDecodeError: 인코딩이 달라서 나는 오류

spamDataset = pd.read_csv('./word/spam_data.csv' ,encoding='ms949')
spamDataset = pd.read_csv('./word/spam_data.csv',header=None,encoding='ms949')
print(spamDataset.info())
print(spamDataset.head())
target = spamDataset[0] # 0번째 컬럼을 불러와 target에 저장
print('target - ',target,type(target))
text = spamDataset[1]
print('text - ',text,type(text))

# spam = 1 , ham = 0 새로운 타켓을 만들고 싶다면?
target = [1  if t == 'spam' else 0  for t in target ] # else를 줄 경우, 순서가 바뀜
print(target)

# - 코드클린 - 문자열에 대한 정규표현식을 이용해서 문자를 제거하는 작업
# 정규표현식
# import re
'''
1. 메타문자
. ^ * $ + ? {} [] \ | () 
. -> 무엇이든 한 글자를 의미
^ -> 시작문자 지정
* -> 0 or more
+ -> 1 or more
? -> 0 or 1
예)
[abc] -> a, b, c 중 한문자와 매치
[^0-5] -> not 
^[0-5] -> 반드시 시작하는 문자가 0,1,2,3,4,5 중 하나
문자클래스
\d -> 숫자의 자릿수
\D -> 숫자가 아닌 문자매칭의 자리수  
\w -> 문자+숫자
\W -> 문자+숫자 아닌 문자와 매치
\s -> 공백
ex)
010-0000-0000
^\d{3}-\d{4}-\d{4}   # 반드시 숫자 세자리로 시작하는 ~

- sub() # 찾아서 대체
- match() match 함수는 문자열의 처음부터 시작하여 패턴이 일치하는지 확인
- search() match와 비슷, but 반드시 문자열의 처음부터 일치해야 하는 것은 아니다.
- findall() findall 함수는 문자열 중 패턴과 일치되는 모든 부분을 찾는다.
- finditer()

'''
import re
p = re.compile('[a-z]+')  #  a-z 범위에서 1 or more
match = p.match('python')   # match()는 매치여부 확인
match = p.match('PHTHON') # 범위가 소문자 a~z이기때문에 None 출력
print(match)

# 텍스트 전처리 -
def cleanText(str):
    str = re.sub('[,.?!:;]' , ' ' , str)
    print(str)
    str = re.sub('[@!#!~#] | [0-9a-zA-z]',' ', str) # |으로 한꺼번에 작업 가능
    print(str)
    str = ' '.join(str.split())  # 공백제거 # Question ??
    return str
cleanText('비아그라 500GRAM 정력 최고!')

# 텍스트 전처리 - (특수문자,숫자,공백,영문제거) => 한글 단어만 추출
#내 답안)
text = spamDataset[1]
print(text,type(text))
def cleanText01(str):
    str = re.sub('[,.!]',' ',str)
    str = re.sub('[0-9a-zA-Z]',' ',str)
    str = ' '.join(str.split())
    print(str)
cleanText01(str(text))

# 강사님 답안
def cleanText(str):
    str = re.sub('[,.?!:;]' , ' ' , str)
    str = re.sub('[@!#!~#] | [0-9a-zA-z]',' ', str) # |으로 한꺼번에 작업 가능
    str = ' '.join(str.split())  # 공백제거
    return str

cleanData = [ cleanText(t) for t in text] # comprehension # Question ??
print(cleanData)

# xls, xlsx  파일 # openpyxl lib 설치
import openpyxl

kospiDataset = pd.ExcelFile('./word/sam_kospi.xlsx')
kospi = kospiDataset.parse('sam_kospi')   # Question ??
print(kospi.info())

from statistics import * # 통계 관련 함수 불러오기
print('high mean - ', mean(kospi.High),type(kospiDataset))

# json 파일 입출력
'''
json file : 네트워크 상에서 표준으로 사용되는 파일형식 
구성 : {key : value , key : value}
encoding : python(dict,list) -> json 문자열(json file) : dumps()
decoding : json 문자열(json file) -> python(dict,list) : loads()
import json 
'''
import json #모듈가져오기

# encoding
# python -> json
user = {'id' : 1234, 'name' : '섭섭해'}
print(type(user))
jsonStr = json.dumps(user) # object -> json str
print(jsonStr,type(jsonStr))

# decoding
pyObj = json.loads(jsonStr)
print(pyObj,type(pyObj))
print(pyObj['name']) # name의 value값 출력

'''
usagov_bitly.txy # json화 되어있는 text file
'''
with open(file='./word/usagov_bitly.txt',mode='r',encoding='utf-8') as file :
    lines = file.readlines() # list 형식
    # print(type(lines),len(lines))
    # print(lines[:5]) # 5개만 slicing
    rows = [ json.loads(line) for line in lines ] # line에 dict를 담기, row라는 list 안에 line의 dict이 담김
    # print( type(rows)) # >>> class list
    print( type(rows[0]),rows[0]) #  >>> class dict
    for row in rows : # rows에서 dict을 꺼내, row에 넣기 때문에 row는 dict
        print(type(row))
        for key, value in row.items() :
            print('key - {} , value - {}'.format(key,value))
    # rows -> pd.DataFrame (행렬로 만들기)
    rowsDF = pd.DataFrame(rows) # 행렬로 변환
print(rowsDF.head)