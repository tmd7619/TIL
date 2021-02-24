#coment
#변수 - 데이터를 담는 공간 또는 그릇
#모듈=변수+함수+클래스
'''
python의 장점
-상대적으로 쉽다
-interactive programing
-분석, 통계에 관련된 library가 풍부하다
-Open source(무료)
-R에 비하여 범용적

python의 단점
-하위 호환성이 없음

'''

# keyword module loading 파이썬은 하나의 모듈

import keyword
print(keyword.kwlist)

# 변수(숫자로 시작할 수 없다. 특수문자 허용되는데, _와 $만 사용가능)의 생성 및 삭제
# 파이썬은 인터프리터 기반의 언어

# 변수선언 방법
# - Camel Case : 함수, 변수 정의시 많이 사용하는 언어 numberOfCollageGraduates
# - Pascal Case : 클래스 정의시 사용하는 방법 NumberOfCollageGradua
# - Snake Case : 권장하지 않는다 number_of_collage_graduates

a  = 100
print(a)

# python data type(Built-in Types)
# - Numeric
# - Sequence (List, tuple, range)
# - Text Sequence (str)
# - Mapping (dict)
# - Set (set)
# - Bool (True(T), False(F), not, and, |, ~(비교))
# - date, time

# 허용하는 변수 선언 법
# 예악어 변수명으로 사용 불가
# 금지목록
""" 
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""
#sep 옵션
print('p','y','t')
print('p','y','t',sep="") # sep="" 옵션은 공백을 없애주는 기능
print('p','y','t',sep='-') # 변수 사이마다 '-'를 붙임
'''
참고 Escape 코드
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
'''

# end 옵션
print('Welcome To',end=' ') # 가로로 출력
print('IT News',end=' ')
print('Web Sites',end=' ')

#format 사용법(d,s,f) # 이해안됨
one = 1
two = 2
print('%d %d' % (one, two))

one = 'one'
two = 'two'
print('%s %s' % (one, two)) # 자릿수 제한일때 좋음

print("{},{}".format(one,two)) #여러개의 변수들을 결합시켜 하나의 문장으로 만들때 좋음

print('%10s' % ('nice',)) # 10의 자리 수 중 뒤에 네자리에 nice
print('%-10s' % ('nice',))

#시퀀스 객체의 각 요소는 순서가 정해져 있으며, 이 순서를 인덱스라고 부릅니다.
'''
컴퓨터 과학에서 객체 또는 오브젝트(object)는 
클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것으로 
프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 
변수, 자료 구조, 함수 또는 메소드가 될 수 있다. 
프로그래밍 언어는 변수를 이용해 객체에 접근하므로 
객체와 변수라는 용어는 종종 함께 사용된다. 
그러나 메모리가 할당되기 전까지 객체는 존재하지 않는다.
'''
'''
메모리에 저장된 자료를 객체(object)라고 합니다.
변수(Variable)와 변수명(Variable Name)
객체를 저장한 공간을 변수, 변수의 이름을 변수명이라고 합니다. 
변수에 객체를 넣을 때 등호 '='을 이용합니다. 등호 왼쪽에는 변수명, 등호 오른쪽에는 객체를 적습니다.
'''