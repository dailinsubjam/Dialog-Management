from flask import Flask, render_template, request
import json


app = Flask(__name__)

testInfo = {}


@app.route('/main/form', methods=['GET', 'POST'])  # 路由
def test_post():
    print("send successfully!")
    for item in request.form:
        print(item)
    print(111)
    testInfo['name'] = 'xiaoliao'
    testInfo['age'] = '28'
    return json.dumps(testInfo)


@app.route('/main')
def main_page():
    return render_template('tab-test.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form-test')
def form_test():
    return render_template('form-test.html')


if __name__ == "__main__":
    app.run(debug=True)
