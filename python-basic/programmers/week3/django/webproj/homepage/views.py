from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request): #어느경로로와야 인덱스 함수를 사용하는가?
    return HttpResponse("<h1>Hello World</h1>") #리스폰스에는 에치엠엘 마크업 랭귀지 적용이 가능하다.
