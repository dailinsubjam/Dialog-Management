from flask import Flask, render_template, request
import json


app = Flask(__name__)

testInfo = {}


@app.route('/test_post/nn', methods=['GET', 'POST'])  # 路由
def test_post():
    print("send successfully!")
    print(request.form)
    testInfo['name'] = 'xiaoliao'
    testInfo['age'] = '28'
    return json.dumps(testInfo)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form-test')
def form_test():
    return render_template('form-test.html')


if __name__ == "__main__":
    app.run(debug=True)
