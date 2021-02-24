
'''
palindrom(회문)
단어를 거꾸로 읽어도 제대로 읽는 것과 같은 단어 또는 문장
level, sos, rotator, nurses run
기준이 필요(중앙을 기준으로해서 첫 글자와 마지막 글자를 비교)
반복문
// - 몫을 취하는 연산자

'''

str = 'jslim9413'
idx = len(str) //2
print(idx, str[idx])

# 방법 1
def isPalindrom() :
    isFlag = True
    word = input('회문검사를 위한 단어를 입력하세요')
    for idx in range(len(word) // 2 ) :
        if word[idx] != word[-1 - idx] :
            isFlag = False
            break
    return isFlag

#방법 2
def reversedPalindrom() :
    word = input('회문검사를 위한 단어를 입력하세요')
    print(word == word[::-1])

# 방법 3
def reversedPalindrom() :
    word = input('회문검사를 위한 단어를 입력하세요')
    print(type(reversed(word)),reversed(word))
    print(list(word),list(reversed(word)))
    print(list(word)==list(reversed(word)))

# palindrom_words.txt 파일의 단어를 읽어서 회문인 단어만 출력

def palidromFile() :
    with open(file='./word/palindrome_words.txt',mode='r') as file :
        for line in file :
            line = line.strip('\n')
            if line == line[::-1] :
                print(line)

# 문자열에서 2 - gram 개의 연속된 요소를 추출한다면?
# 자연어처리
# hello -> he/el/ll/lo

text = 'hello'
for idx in range(len(text) -1) : # 두글자씩 출력인데  앞에 4번째까지만 출력하면 됨
    # print('idx - ', idx)
    print(text[idx],text[idx+1],  sep='')

text = 'this is python script'
textlist = text.split()  # 공백 단위로 쪼개서 list형식으로
print(type(textlist),textlist)

for idx in range(len(textlist) -1) :
    # print('idx - ', idx)
    print(textlist[idx], textlist[idx+1])

'''
zip ()
반복 가능한 객체 여러 개를 넣으면 요소 순서대로 
튜플로 묶어서 zip 객체를 반환
예) list(zip([1, 2, 3], [97, 98, 99]))는 [(1, 97), (2, 98), (3, 99)]
'''

num = [1,2,3,4]
name = ['hong','gil','dong','guy']
dic = {}
for key,value in zip(num,name) :
    dic[key] = value
print(dic)

'''
input 함수를 이용해서 문자열을 입력받고
예시) python is a programming language that lets your work quickly
input 함수를 이용해서 gram 할 숫자를 입력받고
예시) 2
입력된 숫자에 해당하는 단어 N-gram 형식으로 출력
주의) 입력된 문자열의 단어갯수가 입력된 정수 미만이라면 예외를 발생
'''
# 방법 1
def zipNgrom() :
    string = input('문자열을 입력하시오')
    gram = int(input('N-gram할 숫자를 입력하시오'))
    sentences = string.split()
    for idx in range(len(sentences)-gram+1 ) :
        print(sentences[idx : idx+gram]) #slicing
# 방법2
def zipNgrom01() :
    word = input('문자열을 입력하시오')
    gram = int(input('N-gram할 숫자를 입력하시오'))
    sentences = word.split()
    ngram = zip(*[ sentences[idx:] for idx in range(gram) ])  # * : 각 요소를 콤마로 구분해서 넣음
    # print(ngram) # >>> 주소번지 출력
    print(type(ngram))
    # print(list(ngram))
    for idx in ngram :
        print(idx)




