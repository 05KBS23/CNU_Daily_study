from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request): #어느경로로 와야 인덱스 함수를 사용하는가? 리퀘스트가 인자로 주어진다.
    number = 10
    return render(request, 'index.html',{"my_num" : number})
#이 뷰의 역할? 어떤 요청이 왔을 떄 "Hello world"라는 리스폰스를 주는 것

#템플릿? : 모델과 뷰와는 다르게 파이썬 파일을 만들지 않고 새로운 html파일을 만드는 것
# 이 파일을 관리하는 법은 여러가지가 있는데, 각 앱의  디렉토리에서 관리할 수 있음
# 목적에 따라 디렉토리 구조는 상이할 수 있음.

#이 다음엔 index.html이 어디있는지 알려줘야하는대,
# 파이썬 파일이 아니므로 import같이 쓸 수 없음,



