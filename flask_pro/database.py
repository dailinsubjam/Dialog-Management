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
    


def insert_and_update(userID, nodeID, info):
    
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        table_name = 'USER_' + userID
        sql = 'replace into ' + table_name + ' (nodeID, info) values (?, ?)'
        c.execute(sql, (nodeID, info))
        conn.commit()
        conn.close()
    


def make_json_file():
    

if __name__ == '__main__':
    
    