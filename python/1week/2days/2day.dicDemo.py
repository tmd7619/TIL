
# python mapping type = dict
# dictionary는 key와 value의 대응관계 type
# hash 또는 Associative Array와 유사한 구조
# {}

#순서 x, 키 중복x, 수정,삭제 가능

temp = {}
print(type(temp))

dict02 = {      #dict 만들기 1
    'name' : 'seop',
    'age' : 49,
    'address' : 'kwangju',
    'birth' : '730910' ,
    'gender' : 'm'
}

dict03 = dict([('name','seop'),('age','49'),('address','kwangju')]) #tuple을 활용한 dict만들기 2

dict03 = dict(           #dict 만들기 3
    name = 'seop',
    age = 49,
    address = 'kwangju')
print(type(dict03),dict03)
print('dict -',type(dict02),dict02)

# dict 요소를 추가하는 방법
dict02['marriage'] = True
print('dict -',type(dict02),dict02)

# 키 유무를 판단
print('marriage' in dict02)


# 데이터 확인
print('address - ', dict02['address'])
print(dict03.get('name'))

# dict_keys, dict_values, dict_items
print('dict_key -',dict03.keys()) #키값만 추출
print('dict_values -',dict03.values())


print('dict_key -',list(dict03.keys()),type(list(dict03.keys()))) # key값들을 list형식으로 변한
print('dict_key -',type(dict03.items()),list(dict03.items()),type(list(dict03.items()))) # key값들을 list형식으로 변한

# looping
'''
for(초기식; 조건식; 증감식){

}

for item in collection :
    statement
'''
for key in dict03.keys() :
    print('key : {},value : {}'.format(key,dict03.get(key)))
    # .get(key)는 key값을 불러오는게 아니라, key의 value값을 불러와주는 함수

for value in dict03.values() :
    print('value : {}'.format(value))

for (key, value) in dict03.items() : # 각각 key와 value에 키밸류값 넣기 for구문에 넣어진 key value는 str형식임
    print('key : {},value :{}'.format(key,value))

# 삭제 pop(), del
print('dict03-',type(dict03),dict03)
del dict03['name']
print('dict03-',type(dict03),dict03) # name key의 value 값 까지 모두 제거
print('dict03 pop -',dict03.pop('birth'))

dict03.clear()
print(dict03)

# format() 형식을 갖춘 문자열을 만들어주는 메소드
'''
"{}".format(데이터)
ex) "{}원".format(1000)
>>>1000원

여러데이터 변환시,
"{}{}{}".format(데이터1,데이터2,데이터3)
'''

