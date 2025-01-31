"""
1. 1 ~ 100 더하기 (sum 하지 말고 사칙연산만 이용하기)

k = 0
for i in range(1,101):
    k = k + i
print(k)

2. counter 함수 구현하기 : list 가 주어졌을 때, list 요소들의 갯수 구하기

    e.g., 아래와 같이 1 부터 5까지의 수들로 이루어진 L 이라는 리스트가 주어졌을 때,

           각 숫자의 갯수를 Dictionary 형태로 반환되는 함수를 구해보자.

      L = [ 1, 3, 5, 3, 2, 3, 4, 5, 3]

      (출력값: D = {1 : 1, 2 : 1, 3 : 4, 4 : 1, 5 : 2}

3. list comprehension 여러 줄 코드로 작성하기

    L = [ k for k in range (5) ] —> ?

4. 파이썬의 자료형 중 Dictionary에 { key: value} 추가하기, 대입하기

"""

import random

style = ["양식", "중식", "일식", "한식"]

westurn = ["치킨", "피자", "파스타", "귀가"]
chinese = ["마라탕","짬뽕","짜장면", "탕수육"]
japanese = ["초밥","리멘", "오꼬노미야끼","텐동"]
korean = ["제육", "찜닭", "삼겹살", "김밥"]

a = random.choice(style)

w = random.choice(chinese)
j = random.choice(japanese)
k = random.choice(korean)
c = random.choice(chinese)

if a == "양식":
    print(w)
elif a == "중식":
    print(c)
elif a == "일식":
    print(j)
else :
    print(k)









