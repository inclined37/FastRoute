# 1차 코드 (단순 index.html 실행, 같은 디렉토리 내 존재 필수)
'''
import http.server
import socketserver

PORT = 8080     # 사용할 포트

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print("server at port", PORT)
    httpd.serve_forever()
'''

# 2차 코드 (flask 사용)
from flask import Flask, send_from_directory, jsonify   # send_from_directory: 특정 폴더 내 파일 브라우저로 보내는 함수 / jsonify : 파이썬 딕셔너리 JSON 응답으로 변환하는 함수
import os

app = Flask(__name__, static_folder="../client")        # Flask(__name__) : Flask 앱 객체 생성. (웹 서버 핵심 엔진) / 
                                                        # static_folder="../client" : 정적파일(HTML 등)을 불러올 기본 폴더 client로 지정.

@app.route("/")                                         # 라우드 데코레이터 : "/" 경로로 요청 들어오면 아래 함수 실행
def serve_index():                                      # 함수 정의, app_static_folder(../client)에서  index.html 파일 찾아서 클라이언트에 반환.
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")                              # 모든 경로에 해당.
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# 간단한 API 추가 예시
@app.route("/api/hello")                                # 특정 경로에 해당.
def api_hello():
    return jsonify({"message" : "hello from api"})

# AJAX 데이터 전송 예시
@app.route("/api/data", methods=["POST"])               # method 안에 배열 넣을거면 복수형으로 써야함.
def api_data():
    data = request.json
    name = data.get("name", "익명")
    return jsonify({"message": f"{name}님, 데이터 잘 받았어요!"})

if __name__ == "__main__":                              # 이 파일을 직접 실행했을 때만 서버 실행
    app.run(host="0.0.0.0", port=8080, debug=True)      # host: 접속 가능한 IP 주소(0.0.0.0: 외부 PC 허용), debug: 코드 수정 시 서버 자동 재시작. 에러 메시지 상세 표시.