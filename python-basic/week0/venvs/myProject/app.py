from flask import Flask, jsonify, request
#jsonify는 파이썬에서 사용되는 딕셔너리 타입을 제이슨이라는 자바스크립트 타입으로 바꿔주는 함수
#request는 requests는 python사용자들을 위해 만들어진 간단한 Python용 HTTP 라이브러리이며, 간단하게는 HTTP, HTTPS 웹 사이트에 요청하기 위해 자주 사용되는 모듈 중 하나이고
#request 정리 블로그 : https://me2nuk.com/Python-requests-module-example/


app = Flask(__name__)

menus = [
    {"id": 1, "name" : "Espresso", "price": 3800},
    {"id": 2, "name" : "Americano", "price": 3800},
    {"id": 3, "name" : "Cafelatte", "price": 4600},
]

@app.route('/')
def hello_flask():
    return "hello"

# GET /menus | 자료를 가져온다, !!app.route에는 기본적으로 methods = [GET]이 설정되어 있다,
# 또한 리스트 형태로 담아두게 되는데, 이는 한꺼번에 여러 메소드를 실행시킬 수 있다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# Post / menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    #전달받은 자료를 menus 자원에 추가,
    # Request에는 자동으로 요청된 자료가 담겨있다. json이라는 기본적인 가정
    # get.json은 파이썬의 딕셔너리 타입을 변환시켜주는 함수이다. 변환과정이 필요함.
    request_data =  request.get_json()
    new_menu = {
        "id" : 4, #id 값이 파이참에서 고정되어 있다면 포스트맨에서 해당 id값으로만 생성된 것만 GET으로 조회가 가능하다
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

#알바생이 카페 메뉴를 추가하고 싶으면 사장님은 POST를 통해 새로운 메뉴를 추가하는 코드를 만들어서 알바생이 원할 때마다 추가시킬 수 있다.
#파이참에서 new_menu라는 변수를 선언하고 append함수를 이용해서 리스트에 추가하는 과정을 거친다.
#이 때 "
#따라서

@app.route('/menus/<int:id>', methods = ['PUT'])
def put_menu(id):
    request_data = request.get_json()
    new_menu = {
        "id": request.get_json()["id"],
        "name": request.get_json()["name"],
        "price": request.get_json()["price"]
    }
    menus[3] = new_menu
    return jsonify(new_menu)
#request는 postman에서 요청한 값을 의미한다...
#앞서 알바생이 카페 메뉴에 새롭게 추가한 부분에 대하여 수정이 요구될 때, Put으로 id,name,price의 밸류 값의 변경이 가능하다.
#포스트맨에서 PUT으로 요청할 수 있고, 변경된 결과를 GET을 통해 조회가 가능하다.
#한편 어느날 알바생이 주제넘게 KEY값(id,name,price)를 변경하고 싶다고 하자,
#그러기 위해서는 #9줄의 리스트를 수정해야 하는데, 사실 이는 '사장'의 권한이므로 파이참에서 수정을 해야한다.
#근데 보통 그런 일은 없을것 같다.

if __name__ == '__main__':
    app.run()

#api란? = 프로그램들이 서로 상호작용하는 것을 도와주는 매개체
# http uri (URL?)을 통해 자원을 명시하고 http method(요청방법 : get, post,put)를 통해 해당자원에 대한 crud를 진행
#GET/home, POST/shoes 같이 /뒤에 나오는 것을 자원으로 간주하는거다

# REST API 란? ( GET과 POST의 차이 ) : https://hoyeonkim795.github.io/posts/rest_api/
# http 메소드와 상태코드 정리 : https://kyun2da.dev/CS/http-%EB%A9%94%EC%86%8C%EB%93%9C%EC%99%80-%EC%83%81%ED%83%9C%EC%BD%94%EB%93%9C/
