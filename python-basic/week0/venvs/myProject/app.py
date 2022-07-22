"""""
api란? = 프로그램들이 서로 상호작용하는 것을 도와주는 매개체
# http uri (URL?)을 통해 자원을 명시하고 http method(요청방법 : get, post,put)를 통해 해당자원에 대한 crud를 진행
#GET/home, POST/shoes 같이 /뒤에 나오는 것을 자원으로 간주하는거다.
# REST API 란? ( GET과 POST의 차이 ) : https://hoyeonkim795.github.io/posts/rest_api/
# http 메소드와 상태코드 정리 : https://kyun2da.dev/CS/http-%EB%A9%94%EC%86%8C%EB%93%9C%EC%99%80-%EC%83%81%ED%83%9C%EC%BD%94
#jsonify는 파이썬에서 사용되는 딕셔너리 타입을 제이슨이라는 자바스크립트 타입으로 바꿔주는 함수
#request는 requests는 python사용자들을 위해 만들어진 간단한 Python용 HTTP 라이브러리이며, 간단하게는 HTTP, HTTPS 웹 사이트에 요청하기 위해 자주 사용되는 모듈 중 하나이고
#request 정리 블로그 : https://me2nuk.com/Python-requests-module-example/
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name" : "Espresso", "price": 3800},
    {"id": 2, "name" : "Americano", "price": 4000},
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
        "id" : request.get_json()["id"], #id 값이 파이참에서 고정되어 있다면 포스트맨에서 해당 id값으로만 생성된 것만 GET으로 조회가 가능하다
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

#알바생이 카페 메뉴를 추가하고 싶으면 사장님은 POST를 통해 새로운 메뉴를 추가하는 코드를 만들어서 알바생이 원할 때마다 추가시킬 수 있다.
#파이참에서 new_menu라는 변수를 선언하고 append함수를 이용해서 리스트에 추가하는 과정을 거친다.
#이 때 "
#따라서

@app.route('/menus/<int:KBS>', methods = ['PUT'])
#int는 알바생이 지정한 값. @@중요@@ int=KBS가 아닌 이유는 그냥 문법이라고 한다!!
#아무튼 포스트맨에서 menus/임의의 숫자(리스트 키에 해당하는 숫자를 입력하면 원하는 메뉴의 밸류값을 수정할 수 있다}
def put_menu(KBS):
    request_data = request.get_json()
    new_menu = {
        "id": KBS,
        "name": request.get_json()["name"],
        "price": request.get_json()["price"]
    }
    menus[KBS-1]= new_menu #PUT에서 알바생이 원하는 리스트의 키, 즉 메뉴의 번호(1,2,3,4)를 선택해서 따로 수정하기 위해 -1을 한다.
    return jsonify(new_menu)

#request는 postman에서 요청한 값을 의미한다...
#앞서 알바생이 카페 메뉴에 새롭게 추가한 부분에 대하여 수정이 요구될 때, Put으로 id,name,price의 밸류 값의 변경이 가능하다.
#포스트맨에서 PUT으로 요청할 수 있고, 변경된 결과를 GET을 통해 조회가 가능하다.
#한편 어느날 알바생이 주제넘게 KEY값(id,name,price)를 변경하고 싶다고 하자,
#그러기 위해서는 #9줄의 리스트를 수정해야 하는데, 사실 이는 '사장'의 권한이므로 파이참에서 수정을 해야한다.
#근데 보통 그런 일은 없을것 같다.

@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id):
    for i in range(len(menus)):
        if menus[i]["id"]==id:
            del menus[i]
            break
    return "ID{}삭제지롱ㅋㅋㅋㅋㅋㅋ개빡치쥬?ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ".format(id)


#그런데 충격적인 사실을 알았다. 예를들어 method가 =Delete라고는 하지만 삭제하는 기능이 자체적으로 없다는 것...
#그래서 뭔가 알듯 말듯 알쏭달쏭하다.. POST,GET,PUT코드를 작성할 때는 몰랐는데,
# 알고보니 해당하는 기능을 직접 코딩하고 있었던 것...
#아무튼 간에 처음엔 delete 함수를 아래와 같이 짰는데
"""
def put_delete(KBS):
    request_data = request.get_json()
    new_menu = {
        "id": KBS,
        "name": request.get_json()["name"],
        "price": request.get_json()["price"],
    }
    del menus[KBS-1]
    return jsonify(new_menu)
"""
#리스트가 순서대로 삭제가 안 되는 문제가 발생하였다.
#그이유는 예를 들어 3의 길이를 가진 리스트에서 하나를 삭제하게 되면 길이가 2가 된다.
#이렇게 del menus[KBS-1] 해당 위치의 리스트값 제거를 고정?시키는 바람에
#[1,2,3]에서 0번째 위치인 1을 삭제하게 되면, 다음에 삭제를 요청할 땐 [2,3]인 상태에서 1 의 위치인 3을 삭제하게 된다.
#그래서 이 문제는 도저히 풀 수 없어서 팀원의 도움을 받았다.휴휴

if __name__ == '__main__':
    app.run()
