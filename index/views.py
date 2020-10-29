from django.http import JsonResponse
from utils.db import Mysql

def nav(request):
    sql1 = "SELECT id, system FROM system;"
    navSecondClassData = Mysql.select(sql1)
    return JsonResponse({"navSecondClassData": navSecondClassData})

def contactus(request):
    sql2 = 'SELECT id, address, tel, Email, title, down, img FROM link;'
    contactus = Mysql.select(sql2)
    return  JsonResponse({"contactus": contactus})

def index(request):
    sql1 = 'SELECT Id, img, `where` FROM image;'
    rotateChart = Mysql.select(sql1)
    sql2 = 'SELECT Id, title, author, description, content, img FROM example;'
    successfulCases = Mysql.select(sql2)
    return JsonResponse({"rotateChart": rotateChart, "successfulCases": successfulCases})

def about(request):
    sql = 'SELECT id, title, descript, content, img FROM about;'
    aboutData = Mysql.select(sql)
    return JsonResponse({"aboutData": aboutData})

def newsInformation(request):
    sql = 'SELECT Id, title, author, description, content, typeId, img FROM article;'
    newsInformation = Mysql.select(sql)
    return JsonResponse({"newsInformation": newsInformation})

def goodstype(request):
    # 获取默认值的总体思路：
        # 1.第一次点击专业产品或者专业产品下的二级目录，返回一个值
        # 2.根据这个值获取手风琴的所有信息和第一个系列的商品
    try:
        system = request.GET.get("system")
        if system == '':
            system = '高端演出系统'
        print(system)
        # 当我点击'专业产品'或二级目录时，给一个默认值。
        sql1 = "SELECT series, GROUP_CONCAT(typename) typename " \
               "FROM goodstype " \
               "WHERE system = %s " \
               "GROUP BY series;"
        data1 = (system)
        catalog = Mysql.select(sql1, data1)
        for index in range(len(catalog)):
            goodsname = catalog[index]["typename"].split(",")[0]
            break
        sql2 = "SELECT id, name, img, description, content, type " \
               "FROM goods " \
               "WHERE type = %s"
        data2 = (goodsname)
        goodsfirstdata = Mysql.select(sql2, data2)
        if goodsfirstdata == ():
            goodsfirstdata = "当前类型下没有商品"
    except Exception as e:
        goodsfirstdata = "不知道出了啥错，需要程序员调试"
    return JsonResponse({"catalog": catalog,"goodsfirstdata": goodsfirstdata})

def goods(request):
    # 点击系列的时候思路
        # 1.点击系列返回某个系列的值
        # 2.根据系列接收返回的值
    try:
        type = request.GET.get("type")
        print(type)
        # 当我点击三级目录的时候是不关乎路由跳转的，只有点击四级目录的时候返回相应的数据
        sql1 = "SELECT id, name, img, description, content, type " \
               "FROM goods " \
               "WHERE type = %s"
        data1 = (type)
        goodseconddata = Mysql.select(sql1, data1)
        if goodseconddata == ():
            goodseconddata = "当前类型下没有商品"
    except Exception as e:
        goodseconddata = "不知道出了啥错，需要程序员调试"
    return JsonResponse({"goodseconddata": goodseconddata})
