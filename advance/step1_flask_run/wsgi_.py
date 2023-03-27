
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "home page wsgi"

# cd 이폴더로 이동 -> 서버수행 단계 없이 터미널에서 flask run