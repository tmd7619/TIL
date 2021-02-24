
from ai.file.fileProc import *

fileStream('hello.txt','r') # read모드로 작업

# # 예외사항 적용
# try :
#     fileStream('hello.txt','asdf')
# except Exception as e :
#     print('error - ', e)
# print('end')

# def에서 exception적용한 뒤 ,print
from ai.file.fileProc import *
# single line text inout
fileStream('./ai/file/hello.txt','aaa')
fileStream('./ai/file/hello.txt','w') # 경로 지정하는 법 .은 현재의 프로젝트디렉토리를 의미함
fileStream('./ai/file/hello.txt','r')
print('end')

# multi line text out
withMultiWriter('multiline.text')
print('end')

from ai.file.fileProc import *

lines = ['hello ', 'how are you','nice to meet you'
                                 ,'안녕하세요','반갑습니다']
withListFileWriter('listline.tex',lines)

# multi line text read
withListFileRead('listline.tex','r')

