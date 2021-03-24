import MySQLdb

# ユーザ情報取得処理
def insert_account(data):
    conn = get_connection()
    cur = conn.cursor()

    sql = "INSERT INTO account2 VALUES(%s,%s,%s,%s,%s)"

    try:
        cur.execute(sql, (data[0], data[1], data[2], data[3], data[4]))
    except Exception as e:
        print("SQL実行に失敗：" , e)
        return False

    cur.close()
    conn.commit()
    conn.close()

    return True

# DBとのコネクションを取得
def get_connection():
    return MySQLdb.connect(user='root',passwd='pass',host='localhost',db='flasktest',charset="utf8")

