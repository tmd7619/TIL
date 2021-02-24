
'''
텍스트파일 입출력
open(file = '파일경로/파일명', mode = 'r|w|a|wb')
파일을 사용하기 위해서는 open함수로 파일을 열어야 한다.
파일을 다 사용했으면 close함수로 닫아야 한다. (반드시)
r - 읽기모드 (디폴트)
w - 쓰기모드, 파일이 있으면 모든 내용을 삭제
x - 쓰기모드, 파일이 있으면 오류 발생
a - 쓰기모드, 파일이 있으면 뒤에 내용을 추가
'''

file = open(file = 'hello.txt',mode='w')
file.write('hi seop')
file.close() #닫기

# with open() as file : # close를 자동으로 시켜주는 구문
with open(file= 'hello.txt', mode = 'r') as file :
    print(file.read())

# def fileStream(fileName, mode ) :
#     if mode == 'w' :
#         pass
#     elif mode == 'r' :
#         with open(file=fileName, mode=mode) as file :
#             line = file.read()
#             print('result read - ', line)
#     elif mode == 'a' :
#         pass
#
#     else :
#         raise Exception('모드를 확인하세요')


'''
readline으로 파일을 읽을 때는 while 반복문을 활용해야 합니다. 
왜냐하면 파일에 문자열이 몇 줄이나 있는지 모르기 때문입니다.
while은 특정 조건이 만족할 때 계속 반복하므로 
파일의 크기에 상관없이 문자열을 읽어올 수 있습니다.

readline은 더 이상 읽을 줄이 없을 때는 빈 문자열을 반환하는데, 
while에는 이런 특성을 이용하여 조건식을 만들어줍니다. 
즉, line != ''와 같이 빈 문자열이 아닐 때 계속 반복하도록 만듭니다. 
그리고 반복문 안에서는 line = file.readline()과 같이 
문자열 한 줄을 읽어서 변수 line에 저장해주면 됩니다.
'''

# 예외를 def 코드에서 적용하기
def fileStream(fileName, mode) :
    file = None     # 변수 file을 None으로 초기화
    try :
        if mode == 'w' :
            file=  open(file=fileName, mode=mode)
            file.write('samply txt')
        elif mode == 'r' :
             file=  open(file=fileName, mode=mode)
             line = file.read()
             print('result read - ', line)
        elif mode == 'a' :
            file = open(file=fileName, mode=mode)
            file.write('\nappend') # \ : 행을 새로 시작하는 뜻
        else :
            raise Exception('모드를 확인하세요')
    except Exception as e :
        print('error - ', e)
    finally:
        if file != None :
            file.close()



def withMultiWriter(fileName) :
    with open(fileName, 'w',encoding='utf-8') as file :
        for idx in range(3) :
            print('idx - ', idx)
            text = input('문자열 입력 요망! >>> ')
            file.write('{} - {}\n'.format(idx, text))


def withListFileWriter(fileName, dataset) :
    with open(fileName,'w',encoding='utf-8') as file :
        for idx in range(len(dataset)) :
            print('idx - ', idx)
            file.write('{} - {}\n'.format(idx,dataset[idx]))

def withListFileRead(fileName,mode) :
    with open(fileName,mode,encoding='utf-8') as file :
        #  line = None
        #  while line != '' :
        #      line = file.readline()
        #      print(line.strip('\n')) # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
        #
        # for line in file.readlines() :
        #     print(line.strip('\n'))
        #
        #
        # print(file,type(file))

        for line in file :
            print(line.strip('\n'))
