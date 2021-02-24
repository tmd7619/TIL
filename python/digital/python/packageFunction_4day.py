#함수를 정의할 때는 인자=매개변수=파라미터
#함수를 사용할 때 들어가는 값은 인수
# 매개변수 X, 리턴값이 X

def printCoins() :
    print('bitcoin')

# 매개변수X 리턴값이 O
def returnFunc() :
    return '호출한 쪽으로 값이 전달됩니다'

# 매개변수 o , 리턴값 o
def sayEcho(name) : #name은 인자값
    return name+'님, 반갑습니다~'

def calculator(op01,operator,op02) :  # 인자값 3개로 받음
    pass
def makeUrl(url) :
    return "www."+url+".com"

# 매개변수 o , 리턴값 x
def badFunc(name) :   # 아무런 결과도 나오지 않음
    pass

# 인자에 *가 들어감
def tupleFunc(*args) :  # *은 가변인자로 개수가 정해지지 x
    result = 0
    for idx in range(len(args)) :
        result += args[idx]
    return result

def dictFunc(**args) : # 딕셔너리 변수를 전달할때는 **
    for key, value in args.items() :
        print('{}= {}'.format(key,value))

#범위내에 있는 값의 홀, 짝의 합을 구해서 리턴
def cntSum(start,end) : #인자 값을 두개 받음
    odd = even = 0
    for x in range(start,end+1) :
        if x %2== 0 :
            even += x
        else :
            odd += x
    return (odd,even)

def leapYearFunc(startYear,endYear) :
    yearList = []
    for year in range(startYear,endYear+1) :
        if year%4==0 and year %100 !=0 or year%400==0:
            yearList.append(year)
    return yearList

def rtnDictFunc(x):
    y01 = x * 10
    y02 = x * 20
    y03 = x * 30
    return{'val01' : y01 , 'val02' : y02, 'val03' : y03}