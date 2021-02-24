
# python date type

from datetime import date, datetime #datetime이란 패키지에서 date와 datetime 모듈을 가져오겠다

today = date.today()
print('date - ',type(today),today.year,today.month,today.day)
print('{}년도,{}월,{}일'.format(today.year,today.month,today.day))

# 시간
todayDateTime = datetime.today()
print('datetime -',todayDateTime)
print('{}시,{}분,{}초'.format(todayDateTime.hour,todayDateTime.minute,todayDateTime.second))

# pip | conda install
# dateutil

from datetime import date, datetime, timedelta

today = date.today()

days1 = timedelta(days=-1) # timedelta(days= ~)
print(days1)

# timedelta에는 weeks, days, hours, minutes, seconds 밖에 없음

print('오늘 이전 하루 -{}'.format(today+days1)) # 오늘날짜에 timedelta를 써서 -1일 값을 출력

# year, month 관련된 옵션을 필요로 한다면
#  relativedelta
from dateutil.relativedelta import relativedelta # from ~ 패키지, import ~ 모듈 or 함수

days = relativedelta(months=-2)

print('두달 전 오늘 - {}'.format(today+days))

days = relativedelta(years=-2)
print('일년 전 오늘 -{}'.format(today+days))

from dateutil.parser import parse #parser에서 parse함수를 가져오겠다

userDate = parse("2021-06-04") # 원하는 날짜 출력
print('parse date - ',userDate,type(userDate))

userDate = datetime(2021,12,25)
print('datetime date - ', userDate,type(userDate))

# 날짜 객체의 출력형식을 원하는 것으로 변경

today = datetime.today()
today = datetime.strftime(today,'%m-%d-%y') # 'str'형식으로 변환
type(today)
#날짜형식 -> 문자열형식의 포맷으로 지정
#strftime() 함수사용
print("{}".format(today.strftime('%m-%d-%y'))) # % 십진법
print("{}".format(today.strftime('%m-%d-%Y'))) # Y대문자로하면 4자리로

# 문자열 형식 ㅡ> 날짜형식 <strptime() 함수>
strDate = '2021,01,06-11:12:40' # 문자열로된 날짜
userDate = datetime.strptime(strDate,'%Y,%m,%d-%H:%M:%S')
print( type(userDate),userDate)