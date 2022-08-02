i=0
while i < 10:
    print(i)
    i+=1


while True:
    num = input("1에서부터 10까지의 숫자를 넣어보시오 : ")
    if num.isdecimal() and int(num) >= 1 and int(num) <= 10:
        print('굿잡')
        break
    else:
        print('잘못입력하셨습니다.{}'.format(num))

# 리스트(list)
for n in [1,2,3]:
   print(n)     #결과는 1,2,3
for n in [1,26,188]:
   print(n)     #결과는 1,26,188
for l in ['1','2','3']:
   print(l)     #결과는 1,2,3

# 튜플(tuple)
v4 = ('Spring', 'Summer', 'Fall', 'Winter')
for season in v4:
   print(season)     #결과는 Spring, Summer, Fall, Winter

# 집합(set)
v4 = {'Spring', 'Summer', 'Fall', 'Winter'}
for season in v4:
   print(season)    # 결과는 '랜덤으로' !!!!  # '중복제거 기능도 있음'


person = {'name':'py', 'age':100, 'age':1000}  

for item in person:
     print(item)           # 결과는 key가 나옴
     print(person[item])   # 결과는 value가 나옴 # but, key가 없으면 오류
     print(person.get(item))  # 결과는 value가 나옴  # key가 없어도 none이라고 나옴 ==> 이걸 쓰는게 좋음


RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

print(RED + 'while' + END)

