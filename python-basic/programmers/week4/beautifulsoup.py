
# 2-1

"""
requests모듈을 이용하여 res.body를 하였을 때 문제점이 있었다
바로 해당 내용이 아주 긴 텍스트로 와서 분석하기 힘들다는 것이다
따라서 내가 원하는 요소만을 가져오고 싶을때는 어떡하면 좋을까>?

이를 가능케하는게 바로 HTML Parser, html코드를 분석해주는 친구, BeuatifulSoup4이다.
"""

# 2-2 BeuatifulSoup 객체 만들기

"""
import requests

res = requests.get("https://www.example.com")

# print(res.text)
이렇게 받은 res를 그대로 사용하지 말고, HTML parser에 전달하면 다음과 같다.


# 첫번째 인자로는 response의 body를 텍스트로 전달한다.
# 두번째 인자로는 "html"로 분석한다는 것을 명시해준다 = 어떤 형식으로 분석할 것인지 명시를 해줘야한다.

from bs4 import BeautifulSoup # 파이썬에서 대문자로 시작하면 보통 클래스이다.

soup = BeautifulSoup(res.text, "html.parser")

위 soup은 html정보를 붆석해서 가지고 있다. 확인을 해보자

soup.prettify()

#title 가져오기
print(soup.title)


# head 가져오기

print(soup.head)

#body 가져오기

print(soup.body)

# <h1> 태그로 감싸진 요소 하나 찾기

print(soup.find("h1"))

# <p> 태그로 감싸진 요소들 찾기

print(soup.find_all("p"))

# 태그 이름 가져오기

h1 = soup.find("h1")
print(h1.name)

# 태그 내용 가져오기

print(h1.text)

"""

# 2-3 원하는 요소 가져오기

import requests

res = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

(soup.prettify())
## <h3>태그에 해당하는 요소를 하나 찾아보자

# print(soup.find("h3"))

## <h3>태그에 해당하는 요소를 모두 찾아보자

h3_result = soup.find_all("h3")

# print(h3_result[0])

# book = soup.find("h3")
# print(book.a.text)

for book in h3_result:
	print(book.a["title"])

## book_list에서 우리가 원하는 제목(title)만 추출해보자

