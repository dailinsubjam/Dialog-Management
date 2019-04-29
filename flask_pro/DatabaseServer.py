from flask import Flask, render_template, request
import json
import database

app = Flask(__name__)

testInfo = {}

INPUT = ''


def reply():
    return "hello"


@app.route('/main/form', methods=['POST'])  # 路由
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
    info['logic'] = data['logic']
    print(nodeID)
    print(json.dumps(info))
    database.insert_and_update(userID, nodeID, info['Name'], json.dumps(info))
    print("send successfully!")

    return "OK"


@app.route('/main/chat', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        INPUT = json.loads(request.form.get('data'))
        print(INPUT)
        return "OK"
    else:
        ans = reply()
        return json.dumps(ans)


@app.route('/database/search', methods=['GET'])
def init_form():
    data = {}
    nodeID, userID = request.args.get('nodeID'), '0'
    ans = database.get_info_by_ID(userID, nodeID)
    if ans:
        info = json.loads(ans)
        data['name'] = info['Name']
        data['global'] = info['global']
        data['local'] = info['local']
        data['logic'] = info['logic']
    return json.dumps(data)


@app.route('/main/import', methods=['GET'])
def get_import_node():
    name = json.loads(request.args.get('data'))

    info = []
    for item in name:
        item_info = database.get_info_by_name('0', item)
        item_id = item_info[0]
        item_inf = item_info[1]
        item_info = json.loads(item_inf)
        item_info['nodeID'] = item_id
        info.append(item_info)
    print(info)
    data = {}
    data['info'] = info
    return json.dumps(data)



@app.route('/main')
def main_page():
    return render_template('tab-test.html')


@app.route('/chat')
def test_chat():
    return render_template('chat-test.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form-test')
def form_test():
    return render_template('form-test.html')

@app.route('/import-test')
def import_test():
    return render_template('import-test.html')


if __name__ == "__main__":
    app.run(debug=True)
