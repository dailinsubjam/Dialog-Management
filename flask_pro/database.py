import sqlite3
import json


def create_table(userID):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = "create table " + table_name + " ([nodeID] integer primary key, [info] text)"

        c.execute(sql)
        conn.commit()
        conn.close()
    except:
        pass


def get_info(userID, nodeID):
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


def insert_and_update(userID, nodeID, info):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = 'replace into ' + table_name + ' (nodeID, info) values (?, ?)'
        c.execute(sql, (nodeID, info))
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
    data = dict()
    for item in res:
        data[item[0]] = json.loads(item[1])
    print(data)
    with open("mid_ressult.json", 'w') as f:
        json.dump(data, f)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # delete_table('0')
    # create_table('0')
    make_json_file('0')
