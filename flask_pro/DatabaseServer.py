from flask import Flask, render_template, request
import json
import database

app = Flask(__name__)

testInfo = {}


@app.route('/main/form', methods=['POST'])  # 路由
def form_submmit():
    data = request.form.get('data')
    data = json.loads(data)
    nodeID = data['nodeID']
    userID = '0'
    info = dict()
    info['sys'] = data['sys']
    info['diy'] = data['diy']
    info['logic'] = data['logic']
    print(nodeID)
    print(json.dumps(info))
    database.insert_and_update(userID, nodeID, json.dumps(info))
    print("send successfully!")

    return "OK"


@app.route('/database/search', methods=['GET'])
def init_form():
    data = {}
    nodeID, userID = request.args.get('nodeID'), '0'
    ans = database.get_info(userID, nodeID)
    info = json.loads(ans)
    data['sys'] = info['sys']
    data['diy'] = info['diy']
    data['logic'] = info['logic']
    return json.dumps(data)


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
