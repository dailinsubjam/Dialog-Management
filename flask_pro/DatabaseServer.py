from flask import Flask, render_template, request
import json
import database

app = Flask(__name__)

testInfo = {}


<<<<<<< HEAD
#<<<<<<< HEAD
#@app.route('/main/form', methods=['GET', 'POST'])
#def test_post():
#=======
@app.route('/main/form', methods=['POST'])
=======
@app.route('/main/form', methods=['POST'])  # 路由
>>>>>>> origin/master
def form_submmit():
    data = request.form.get('data')
    data = json.loads(data)
    nodeID = data['nodeID']
    userID = '0'
    info = dict()
    info['Name'] = data['Name']
    info['nodeType'] = data['nodeType']
    info['global'] = data['global']
    info['local'] = data['local']
    info['db'] = data['db']
    info['logic'] = data['logic']
    print(nodeID)
    print(json.dumps(info))
    database.insert_and_update(userID, nodeID, json.dumps(info))
<<<<<<< HEAD
#>>>>>>> origin/master
=======
>>>>>>> origin/master
    print("send successfully!")

    return "OK"


@app.route('/database/search', methods=['GET'])
def init_form():
    data = {}
    nodeID, userID = request.args.get('nodeID'), '0'
    ans = database.get_info(userID, nodeID)
    if ans:
        info = json.loads(ans)
        data['name'] = info['Name']
        data['global'] = info['global']
        data['local'] = info['local']
        data['db'] = info['db']
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
