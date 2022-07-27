# request는 파이썬을 이용해서 간단히 http통신을 진행할 수 있는 라이브러리이다.



# 정보를 달라고 요청하기 GET

## requests 라이브러리를 불러온 후, naver의 홈페이지를 요청한 후 응답 받아보기
import requests
# res = requests.get("https://www.naver.com")
# print(res)
"""
<Response [200]> 
"""

## Header 확인 : .headers

# print(res.headers)
"""
{'Server': 'NWS', 'Date': 'Mon, 25 Jul 2022 12:17:49 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'P3P': 'CP="CAO DSP CURa ADMa TAIa PSAa OUR LAW STP PHY ONL UNI PUR FIN COM NAV INT DEM STA PRE"', 'X-Frame-Options': 'DENY', 'X-XSS-Protection': '1; mode=block', 'Content-Encoding': 'gzip', 'Strict-Transport-Security': 'max-age=63072000; includeSubdomains', 'Referrer-Policy': 'unsafe-url'}
"""

## Body를 텍스트형태로 확인 : .text, 굉장히 문자가 많으므로 슬라이싱으로 추출가능 [:1000]

# res.text[:1]

# print(res.text)


# @@@중요@@@@ 그러나 단순히 모든 텍스트를 불러오는 것은 문제가 있다. 왜냐하면 내가 원하는 정보만 불러오고 싶기 때문이다.
# 특정요소만 가져오고 싶은 것은 다른 얘기임.

#정보 갱신하는 것을 요청하기, POST

# get은 항상 정보를 가져오는 것인데, post는 우리의 정보를 제공해주면서 서버로 하여금 무언가 요청을 진행할 떄도 있다.
# 대표적으로 로그인이 그 예시이다.

# payload = {"name" : "Hello", "age" : 13 }
"""
res = requests.post("https://naver.com/robots.txt")
print(res.text)
"""

"""
- user-agent : * , 규칙이 적용되는 대상 사용자 에이전트, 누가 요청을 보냈냐 확인하는 부분
- Disallow : /, 크롤링을 금지할 웹 페이지
- Allow : /$, 크롤링을 허용할 웹 페이지

"""


