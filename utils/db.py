import pymysql
from msounduk import settings
from datetime import datetime

class Mysql(object):
    connect = None
    cursor = None

    def __init__(self):
        pass

    @staticmethod
    def link():
        try:
            if Mysql.connect == None:
                Mysql.connect = pymysql.Connect(
                    host=settings.MYSQL_DATA.get("host"),
                    port=settings.MYSQL_DATA.get("port"),
                    user=settings.MYSQL_DATA.get("user"),
                    passwd=settings.MYSQL_DATA.get("passwd"),
                    db=settings.MYSQL_DATA.get("db"),
                    charset=settings.MYSQL_DATA.get("charset"),
                )

                Mysql.cursor = Mysql.connect.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print("即将进入错误日志")

    @staticmethod
    def select(sql, data=(), type=0):
        Mysql.link()
        Mysql.cursor.execute(sql, data)
        if type == 0:
            return Mysql.cursor.fetchall()
        else:
            return Mysql.cursor.fetchone()

    @staticmethod
    def insertinto(sql, data):
        Mysql.link()
        try:
            ret = Mysql.cursor.execute(sql, data)
            Mysql.connect.commit()
            return ret
        except Exception as e:
            MyError.error(e)
class MyError(Exception):
    def writeErrorLog(self, filename, lineno, info):
        # 得到时间
        errortime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error = "出错的时间：" + errortime + ";出错所在的文件：" + filename + ";出错所在的行数：" + str(lineno) + ";出错的信息：" + info
        with open("utils/error.log", "a+", encoding="utf-8") as logfile:
            logfile.write(error + "\n")

    @staticmethod
    def error(e):
        filename = e.__traceback__.tb_frame.f_globals["__file__"]
        lineno = e.__traceback__.tb_lineno
        e.writeErrorLog(filename, lineno, e.args[0])