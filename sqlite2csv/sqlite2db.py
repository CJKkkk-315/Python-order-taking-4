from sqlite3 import connect
from win32.win32crypt import CryptUnprotectData, CryptProtectData

# 看看cookies的字段有哪些
cookies_path=r'Cookies(1)' # 需补充齐全
infosql = "PRAGMA table_info('cookies')"
conn = connect(cookies_path)
cu = conn.cursor()
for each in cu.execute(infosql).fetchall():
    print(each)

# 得到解密后的 cookies
host='.amazon.com'
search_sql = "select * from cookies where host_key like '%{}%'".format(host)
cookies_l = list()
for each in cu.execute(search_sql).fetchall():
    ttl = list(each)
    print(ttl)
    print(ttl[0] /1000000  - 11644473600, ttl[5] /1000000  - 11644473600, ttl[8] /1000000  - 11644473600,)
print(cookies_l)