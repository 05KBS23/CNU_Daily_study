
"""
# 3-1 셀리니움 설치, 실행하기

selenium은 python을 이용해서 웹 브라우저를 조작할 수 있는 자동화프레임워크이다.
이를 사용하기 위해서는 먼저 selenium 프레임워크를 설치해야한다
pip install을 통해서 이를 간단하게 설치할 수 있다.

WebDriver는 웹브라우저를 제어할 수 있는 자동화 프레임워크이다. 이 실습에서는 chrome을 기준으로 한다.
pip install을 통해 webdriver를 관리하는 라이브러리인 webdriver-manager를 설치한다.
"""

""
# 3-2 셀리니움 시작하기


from selenium import webdriver
from selenium.webdriver.chrome.service import Service #웹드라이버 안에있는 크롬이라는 객체를 만들때 인자로 넣어줌

from webdriver_manager.chrome import ChromeDriverManager #사용하고 있는 크롬과 동일한 버전으로 싱크하기 위해 사용

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.naver.com") #driver.get() 겟을 이용하면 열었던 크롬브라우저에 요청을 보낼 수 있다. 마치 주소창에 뭔가를 친것과 마찬가지로.

# driver_path = "/Users/KBS/Documents/study/python-basic/chromedriver2.exe"
# driver = webdriver.Chrome("/Users/KBS/Documents/study/python-basic/chromedriver2.exe")


#selenium을 조작하기 위해서는 드라이버 객체를 만들어야한다. 드라이버는 각 특정 브라우저에 종속되어있다.

# 실행을 하게 되면 새로운 크롬창이 뜨게된다. 이러한 명령은 드라이버 객체를 만들, 그것은 곧 우선 크롬 브라우저를 띄어라와 같다
# 따라서 크롬브라우저를 파이썬으로 조작을 할 수 있는것이다.

driver.get("http://www.naver.com") #driver.get() 겟을 이용하면 열었던 크롬브라우저에 요청을 보낼 수 있다. 마치 주소창에 뭔가를 친것과 마찬가지로.

# 그러나 위 코드와 같이 get요청을 하면 바로 창이 닫혀버리는 에러 때문에 불가피하게 쥬피터 파일로 실행을 하게 되었다. 다음 수업 내용은 selenium_ju 파일에 기록할 것이다.,