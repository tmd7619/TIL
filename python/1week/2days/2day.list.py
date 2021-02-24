# python sequence type - list
# 자료 구조에서 중요
# 파이썬에서는 배열이 존재하지 않는다(array)
# 1차원의 자료구조 R에서는 Vector
# 순서 0 (index 부여 0~), 중복 0 , 수정, 삭제 가능
#[]를 이용해서 변수를 선언할 수 있음.

a = list()
a = []

a = [1,2,3]
print(a, type(a))

# 요소를 추가하는 함수 : append(), insert()

a.append(4) #index의 마지막번째의 4를 추가로 기입

print(a)
a.insert(0,6) #특정 번째의 값을 넣거나 변경
print(a) # >>> [6,1,2,3,4]

a.sort()  #자동으로 오름차순으로 정렬
print(a) # >> [1,2,3,4,6]
a.reverse() #내림차순 정렬
print(a)

# pop() : 기존 리스트에서 요소를 가져오고 요소를 삭제시킨다
print('a - pop() : ', a.pop()) # 맨마지막 요소 삭제
print('a- print : ', a)

# extend()
a = [1,2,3,4]
ex = [4,3]
a.append(ex)
print('a - append :', a)
# >>>[1,2,3,4,[4,3]] # append로 병합하면 대괄호가 중첩되서 나옴
                        # list + list 일 경우,
a = [1,2,3,4] # list + list 병합할때는 extend 사용
a.extend(ex)
print('a - extend : ',a)

movieRank = ['원더우먼','해리포터','겨울왕국']
movieRank1 = ['원더우먼','해리포터','겨울왕국']
movieRank.append('베트맨')
movieRank1.extend('배트맨')
print(movieRank) # list + str 결합은 append
print(movieRank1)# list + str 결합시, str이 한글자씩 binding 됨

# 원더우먼과 해리포터 사이에 '씽'을 추가한다면?
movieRank.insert(1,'씽')
print(movieRank)

# 리스트에서 겨울왕국을 삭제한다면?
movieRank.remove('겨울왕국')
# pop()는 리스트의 맨 마지막 요소 뽑아 삭제하는 것
print(movieRank)

# 최대값 최소값 총합 평균
scoreData = [1,2,3,4,5,6,7,8]
print("max", max(scoreData))
print("min", min(scoreData))
print("sum", sum(scoreData))
print('mean',sum(scoreData)/len(scoreData))


