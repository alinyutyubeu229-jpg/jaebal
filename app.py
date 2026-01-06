from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Docker World!"

if __name__ == '__main__':
    # 괄호 안에 host='0.0.0.0'을 꼭 넣어야 도커 밖에서 접속이 됩니다!
    app.run(host='0.0.0.0', port=5000, debug=True)