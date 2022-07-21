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

# GET /menus | 자료를 가져온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# Post / menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    #전달받은 자료를 menus 자원에 추가
    request_data =  request.get_json()
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
    app.run()