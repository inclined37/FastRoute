# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # CORS 허용 (웹 브라우저에서 요청 가능하게)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 실제 배포시에는 도메인을 명시
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/send-data")
# async def receive_data(request: Request):
#     body = await request.json()
#     user_input = body.get("message", "")
#     print("사용자 입력:", user_input)
    
#     response_message = f"서버가 '{user_input}'를 받았어요!"
#     return JSONResponse(content={"response": response_message})

'''
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head><title>FastAPI Test</title></head>
        <body>
            <h1>Hello, FastAPI!</h1>
        </body>
    </html>
    """
'''

# import requests
# r = requests.get('http://localhost:8080/').text
# print("출력")
# print(text)
"""
print("Hello World!")

import requests
response = requests.get("http://www.naver.com")
html = response.text
print(html)
"""
