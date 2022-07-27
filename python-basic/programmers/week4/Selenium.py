
"""
# 3-1 셀리니움 설치, 실행하기

selenium은 python을 이용해서 웹 브라우저를 조작할 수 있는 자동화프레임워크이다.
이를 사용하기 위해서는 먼저 selenium 프레임워크를 설치해야한다
pip install을 통해서 이를 간단하게 설치할 수 있다.

WebDriver는 웹브라우저를 제어할 수 있는 자동화 프레임워크이다. 이 실습에서는 chrome을 기준으로 한다.
pip install을 통해 webdriver를 관리하는 라이브러리인 webdriver-manager를 설치한다.
"""

"""
# 3-2 셀리니움 시작하기

#selenium을 조작하기 위해서는 드라이버 객체를 만들어야한다. 드라이버는 각 특정 브라우저에 종속되어있다.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
cd Documents./study./python-basic./programmers

라고 하니, 

ERROR: Could not find a version that satisfies the requirement webdriver (from versions: none)
ERROR: No matching distribution found for webdriver
WARNING: You are using pip version 22.0.4; however, version 22.2 is available.
You should consider upgrading via the '/usr/local/bin/python3.10 -m pip install --upgrade pip' command.

라는 오류가 발생하였다.

"""

