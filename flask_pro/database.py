import sqlite3
import json


def create_table(userID):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = "create table " + table_name + " ([nodeID] integer , [name] text primary key, [info] text)"

        c.execute(sql)
        conn.commit()
        conn.close()
    except:
        pass


def get_info_by_ID(userID, nodeID):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = "select info from " + table_name + " where nodeID = " + nodeID
        res = c.execute(sql)
        ans = ''
        for item in res:
            ans = item[0]
        conn.commit()
        conn.close()
        return ans
    except:
        return 0
    
def get_info_by_name(userID, name):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = "select * from " + table_name + " where name = '" + name + "'"
        res = c.execute(sql)
        ans = tuple()
        for item in res:
            ans = (item[0], item[2])
        conn.commit()
        conn.close()
        return ans
    except:
        return 0


def insert_and_update(userID, nodeID, name, info):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = 'replace into ' + table_name + ' (nodeID, info, name) values (?, ?, ?)'
        c.execute(sql, (nodeID, info, name))
        conn.commit()
        conn.close()
    except:
        pass


def delete_table(userID):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = 'drop table ' + table_name
        c.execute(sql)
        conn.commit()
        conn.close()
    except:
        pass


def make_json_file(userID):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    table_name = 'USER_' + userID
    sql = 'select * from ' + table_name
    res = c.execute(sql)
    data = []
    globalVar = dict()
    globalVar['Variable'] = dict()
    data.append(globalVar)
    for item in res:
        # print(item)
        ID = item[0]
        name = item[1]
        info = json.loads(item[2])
        cur = dict()
        cur['ID'] = int(ID)
        cur['name'] = name
        cur['type'] = info['nodeType']
        cur['Variable'] = info['local']
        for var in info['global']:
            data[0]['Variable'][var['Variable']] = var['Value']
        tmp = info['logic']

        tmp.sort(key=lambda x: (x['Priority']))

        cur['logic'] = []

        temp = dict()
        for lo in tmp:
            # print(lo)
            temp['condition'] = lo['Condition']
            temp['operation'] = lo['Operation']
            temp['output'] = lo['Action']
            temp['nextState'] = lo['NextState']
            cur['logic'].append(json.dumps(temp))

        for i in range(len(cur['logic'])):
            cur['logic'][i] = json.loads(cur['logic'][i])
        print(cur)
        data.append(cur)

    with open("mid_result.json", 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    # delete_table('0')
    # create_table('0')
    make_json_file('0')