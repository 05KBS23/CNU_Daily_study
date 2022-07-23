"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
#위에는 원래 없었음
from homepage.views import index
from homepage.views import index
#여기 모듈에는 뷰에 대한 정보가 없기에, 그 정보를 불러와야한다. 그 폴더는 view.py에 있기 때문에
# 위 같은 함수를 요 경로를 들어오면 index함수를 실행하라고 명시.

urlpatterns = [
    path('', index), #127.0.0.1
    path('admin/', admin.site.urls),
]
#이미 어드민에 요청에 대해 리스폰스를 주라는 로직이 있는데
#다음과 같은 로직을 설정한다. 아무런 경로를 설정하지 않으면 기본 #127.0.0.1이다.
