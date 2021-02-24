
# python control statement for looping
# for ~ in range()
# for ~ in list, dict
# for ~ in enumerate(List)


userSum = 0
for temp in range(1,11) : # loop의 범위를 정하고 싶을떄 range
    print(temp,type(temp))     #temp에 어떤 range가 있는지 출력해보기
    userSum +=  temp

print('누적 값은 : {}입니다'.format(userSum))


userList = [(1,2),(3,4),(5,6)]
# userList = [1,2,3,4,5,6] # error


for tmp01,tmp02 in userList :
    print(tmp01,type(tmp01)) # tmp01에는 1, 3, 5 가 담기고 02에는 2 4 6
    userSum += tmp01 + tmp02

print('누적 값은 : {}입니다'.format(userSum))

userDict = {'name' : 'jslim','gender':'m'}
for (key,value) in userDict.items() :
    print("{},{}".format(key,value))

scores = [100,50,80,90,70,60]
print(len(scores))
userSum = 0
for idx in range(len(scores)) : # in 뒤의 범위를 순서대로 하나씩 꺼내어, idx에 대입
    print(type(idx))
    userSum += scores[idx]

print('scores 합 %d ' % userSum) # %을 이용한 포맷 방법 %d %s %f

# List Comprehension
'''
[ for 구문을 통한 반복적인 표현식을 이용할 수 있다 if ]
'''
userList = [1,2,3,4,5,6,7,8,9]

userList02 = [tmp ** 2 for tmp in userList] # userList에서 하나씩 꺼내어, tmp에 넣는데 tmp**2한 것을 넣겠다.
print(userList02)
userList03 = [tmp **2 for tmp in userList if tmp %2==0 ] # tmp가 2의 배수일때만 넣겠다.
print(userList03)

# dict에서도 사용 가능
userDict = {str(tmp):tmp ** 2 for tmp in range(1,10)}
print(userDict)

# 단어의 빈도수 구하기
wordVec = ['love','word','cat','love','love','word']
print(len(wordVec))

'''
딕셔너리[키] = 값 을 통해서 키,값 쌍을 추가할 수 있습니다.

딕셔너리[키] 를 통해서 값에 접근할 수 있습니다.

딕셔너리[키] = 값 을 통해서 값을 변경할 수 있습니다.
(사실 이건 키 중복으로 덮어씌우는것)
출처: https://blockdmask.tistory.com/450 [개발자 지망생]
'''
wordCnt = {}
for word in wordVec :
    print(word)

    wordCnt[word] = wordCnt.get(word,0) + 1 # 왼쪽에는 key 생성, 오른쪽은 value 생성
print(wordCnt)    # .get(word의 value값 불러오기, 값이 없으면 0을 넣겠다 ), +1은 for 구문이기 떄문에 +1씩 더해짐

#get() : 해당 key의 value 값을 호출하는 함수

wordCnt02 = {} # 빈 dct 변수 생성
for word in wordVec :
    if word in wordCnt02 :        # wordCnt02에 word 가 있냐?
        wordCnt02[word] += 1
    else :
        wordCnt02[word] = 1
print(wordCnt02)

# 1~ 1000 합
rangeSum = 0
for value in range(1,1001) :
    rangeSum += value
print('1 ~ 1000 합은 {}입니다'.format(rangeSum))

# 2000~ 2050년 까지 올림픽이 개최되는 년도를 출력하라,,
#단 , 한줄에 5개의 년도를 출력하고 개행

cnt = 0
for year in range(2000,2051,4) :
    cnt +=1
    print(year,end=' ')
    if cnt%5==0 :
        print()

# 아래 리스트에서 세 글자 이상의 단어만 출력해라
wordList = ['I','am','study','python','language','PYTHON','IF','for']

for word in wordList :
    if len(word) >= 3 :
        print(word)
# 대문자만 출력하기
wordList = ['I','am','study','python','language','PYTHON','IF','for']
for word in wordList :
    if word.isupper() : # is 가 앞에 붙는 함수들은 논리값 산출하는 함수
        print(word)

wordList = ['dog','cat','pig','carrot','house','PYTHON','IF','for']
for word in wordList:
    print(word.capitalize()) # .caplitalize 함수는 모든 문자의 앞글자 대문자로 변환

#해당 파일의 확장자를 제거하고 파일 이름만 출력한다면?
# hint - split('.') 문자열을 쪼개는 함수 .기준으로 쪼개짐
fileList = ['greeting.py','bool.py','intro.hwp','bigdata.doc','ai.doc']
for file in fileList :
    print(file,file.split('.'),file.split('.')[0])

word = 'HandSome Boy'
for w in word :
    if w.isupper() : #대문자만 출력
        print(w,end=',')

# 주어진 문장에서 모든 문자를 대문자로 출력한다면?
dumySen = 'FasdfsAsdfasfFsSFsfSDFWER'

for a in dumySen :  # text 시퀀스도 루핑이 가능함
    print(a.upper(),end=' ')

for a in dumySen :
    if a.isupper() :
        print(a,end="")
    else :
        print(a.upper(),end="")

# 리스트 안에 있는 요소들의 순서를 거꾸로 바꾸기
wordList = ['가','나','다','라']
for word in wordList[::-1] : # -1 의 자리는 step
    print(word)

# break, continue
search = 17
numbers = [14,2,34,5,22,566,26,17,43,62,53,4,5,235,63]
for num in numbers :
    if num == search :
        print('found - ',num)
    else :
        print('Not Found -',num) # 17를 찾았는데, 계속 looping을 하기에, 이때 break를 사용

for num in numbers :
    if num == search :
        print('found - ',num)
        break               # break 입력으로 17을 찾은뒤, 수행 중지함
    else :
        print('Not Found -',num)
#  이때,  for ~ else 라는 구문이 존재 !!
search = 5
numbers = [14,2,34,22,566,26,17,43,62,53,4,235,63]
for num in numbers :
    if num == search :
        print('found - ',num)
        break        # 지금까지 찾았는데 없으면, else 구문을 실행
else :
        print('Not Found -',search)

#continue
for num in numbers :
    if num == search :
        continue # 특정 조건을 만족시켰을때, 그 조건을 skip하고 계속 looping
        print('found - ',num)

    else :
        print('Not Found -',num)

# table 만들기  # i가 1일때, j가 3번 돈다
for i in range(1, 6) :
    for j in range(1,4) :
        print('i - {}, j - {}'.format(i,j))

for i in range(2,10) : # 2에서 ~9까지 loop가 도는데, 2-1 2-2 2-3..~
    for j in range(1,10) :
        print('{}*{} = {} '.format(i,j,(i*j)),end="\t")
    print() #라인이 끝날때, 다시 앞줄부터 개행하게 해줌

for i in range(2,10) : # 2에서 ~9까지 loop가 도는데, 2-1 2-2 2-3..~
    for j in range(1,10) :
        print('{}*{} = {} '.format(i,j,(i*j)),end="\t")
    print()
    if i == 5 :
        break # looping 을 빠져나가기, 5단일때
#파이선에서 \는 개행을 하겠다 라는 의미
string ='''저는 여러분과 함꼐 파이썬 강의중에 있는 섭섭해 님입니다 
어려운 시기에 함께하게 되어서 반갑습니다.
나이는 숫자에 불과하지만 성인병이 있네요~
'''
sentences = []
words = []

# append()->last index의 요소를 뽑아서 ~
# insert()-> 특정 index번째의 ~
# extend()

for s in string.split('\n') :
    sentences.append(s) #리스트에 추가하는 작업 #문장을
    # print(sentences)
    for w in s.split(): #문장을 공백(띄워쓰기) 단위로 쪼갬 -> 단어단위로
        words.append(w)
print(sentences,len(sentences))
print(words,len(words))

# 분류정확도
answer = [1,0,2,1,0]
predict = [1,0,2,0,0]
acc = 0 #정확도
for idx in range(len(answer)) :
    fit = answer[idx] == predict[idx]
    print(int(fit),end='\t') # T/F의 기준은 1과 0 임
    print(fit, end='\t')
    acc += int(fit) *20 # 1(정답)인 것에 20%의 가중치를 줌
print('정확도는{}%입니다'.format(acc))

'''
enumerate # value 뿐만 아니라, index 까지 불러올 수 있는 함수
반복문 사용시 몇 번째 반복문인지 확인이 필요하다면
인덱스 번호와 컬렉션 요소(리스트,튜플...)를 확인할 수 있다. 
'''
bookList = ['SQL','r','text-mining','nlp','data-mining','python','django']
for idx, book in enumerate(bookList) : #두가지(index, value)를 받을 수 있음
    print('index - {}, value = {}'.format(idx,book))

'''
syntax)
while <expression> :
    statement
    증감식 # 증감식으로 하지 않으면, 무한loop에 빠지게됨 
'''

cnt = 5
while cnt > 0 :
    print(cnt) # 이렇게 만들면 무한루프에 빠지게 됨 따라서 False가 되게 끔 만들어줘야함
    cnt = cnt -1
    print('cnt - ',cnt)

# List - pop() - last index 에서 하나씩 꺼낸뒤 , 제거시키는 함수
whileList = ['foo','bar','baz']
while whileList :
    print(whileList.pop())
    print('whileList - ',whileList) # 비어있기 때문에, False 만들어줌줌print('while - end')

# 난수를 발생시켜서 횟수내에 맞추는 게임
import random # random 이란 module를 가져옴 # 모듈 = 변수,클래스,함수 등을 포함하는 것

ran = random.random() # 0 ~ 1 사이의 난수를 발생시키는데(실수형)
print('random - ',ran,type(ran))

ran = random.randint(0,10) # 정수형의 난수 발생 # 0은 범위의 min, 2는 max 값
print('random - ',ran)

'''
숫자의 범위 1 ~ 10 
내가 입력한 숫자 > 난수 : 더 작은 수를 입력
내가 입력한 숫자 < 난수 : 더 큰 수를 입력
'''
ranNum = random.randint(1,10)
while True :
    guessNum = int(input("예상 숫자를 입력하세요:"))
    if ranNum == guessNum :
        print('success')
        break
    elif ranNum > guessNum :
        print('더 큰 수를 입력하세요')
    else :
        print('더 작은 수를 입력하세요')

'''
1 ~ 100 사이의 난수를 발생시킨다
도전횟수는 20회로 제한
출력 결과로는 
> 정답을 시도한 횟수
> 정답 
'''
from random import randint # 랜덤이란 모듈에 randint 함수만 가져오겠다 !
ranNum = random.randint(1,100)
tries = 1
while tries <= 20 : #tries 가 20회까지 돌 수 있는 loop 생성 하겠다
    guessNum = int(input('예상 숫자를 입력 하세요 :'))
    if ranNum == guessNum :
        break
    elif ranNum > guessNum:
        print('더 큰 수를 입력하세요')
    else:
        print('더 작은 수를 입력하세요')
    tries += 1 # 증가하는 것을 만들어줌
if guessNum == ranNum :
    print('정답 횟수 {}'.format(tries))
    print('정답{}'.format(ranNum))
else :                               # 20회 초과시, 정답 그냥 출력
    print('정답{}'.format(ranNum))

# random choices()
dataset = list(range(1,10001))
print(dataset)


# 모집단 dataset에서 k개의 데이터를 샘플링하고 싶다면?
import random
train = random.choices(dataset, k= 10)
print('sample dataset - ',train)