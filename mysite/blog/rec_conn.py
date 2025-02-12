import pymysql

def mysql_rdb_conn():
    conn = pymysql.connect(
        host="localhost",  # 호스트 주소
        user="root",       # MySQL 사용자 이름
        password="1234",   # MySQL 비밀번호
        database="RECIPE",  # 데이터베이스 이름
        port=3306          # 포트 번호 (기본 MySQL 포트)
    )
    return conn


mysql_rdb_conn()