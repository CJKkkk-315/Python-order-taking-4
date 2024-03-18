from email import header
from tokenize import String
from xmlrpc.client import Boolean
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import calculate_core
from datetime import datetime

from lunar_python import LunarMonth, LunarYear
from lunar_python.util import LunarUtil

#创建Flask对象app并初始化
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
#app的路由地址"/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交

@app.route('/getLunarTime', methods=["GET", "POST", 'OPTIONS'])
def getLunarTime():
    print("getLunarTime")
    print(request.form)
    if request.method == "POST":
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")
    if request.method == "GET":
        year = request.args.get("year")
        month = request.args.get("month")
        day = request.args.get("day")
        hour = request.args.get("hour")
        minute = request.args.get("minute")
        second = request.args.get("second")
    if len(year) == 0 or len(month) ==0 or len(day) == 0 or len(hour) == 0 or len(minute) == 0 or len(second) == 0:
        return {'code':"1"}
    else:
        lunar_time, is_leap_month = get_lunar_time(int(year), int(month), int(day), int(hour), int(minute), int(second))
        lunar_time_year = lunar_time.year
        lunar_time_month = lunar_time.month
        lunar_time_day = lunar_time.day
        print('success')
        print('lunar_time_year')
        return {'code':"0",'lunar_time_year':lunar_time_year, 'lunar_time_month':lunar_time_month,'lunar_time_day':lunar_time_day, 'is_leap':is_leap_month}



@app.route('/submit', methods=["GET", "POST", 'OPTIONS'])
def submit():
#由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    print(request.form)

    if request.method == "POST":
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")
    if request.method == "GET":
        year = request.args.get("year")
        month = request.args.get("month")
        day = request.args.get("day")
        hour = request.args.get("hour")
        minute = request.args.get("minute")
        second = request.args.get("second")
    #如果获取的数据为空
    if len(year) == 0 or len(month) ==0 or len(day) == 0 or len(hour) == 0 or len(minute) == 0 or len(second) == 0:
        return {'code':"1"}
    else:
        current_info, jieqi_section = get_origin_data(int(year), int(month), int(day), int(hour), int(minute), int(second))
        print('success')
        return {'code':"0",'current_info':current_info,'jieqi_section':jieqi_section}

@app.route('/getSolarTime', methods=["POST", 'OPTIONS'])
def getSolarTime():
    print("getSolarTime")
    print(request.form)
    if request.method == "POST":
        is_leap_month = request.form.get("isLeap")
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")
        print(is_leap_month)
    if len(year) == 0 or len(month) ==0 or len(day) == 0 or len(hour) == 0 or len(minute) == 0 or len(second) == 0:
        return {'code':"1"}
    else:
        #判断某月是否是闰月
        print("11111")
        if is_leap_month:
            leap_month = LunarYear.fromYear(int(year)).getLeapMonth()
            print("1111[%d]"%(leap_month))
            if leap_month == int(month):
                solar_time = get_solar_time(year, month, day, hour, minute, second, True)
            else:
                return {'code':"3"}
                #solar_time = get_solar_time(year, month, day, hour, minute, second, False)
        else:
            solar_time = get_solar_time(year, month, day, hour, minute, second, False)
        solar_time_year = solar_time.year
        solar_time_month = solar_time.month
        solar_time_day = solar_time.day
        print('success')
        print('solar_time_year')
        return {'code':"0",'solar_time_year':solar_time_year, 'solar_time_month':solar_time_month,'solar_time_day':solar_time_day}




def get_lunar_time(year:String, month:String, day:String, hour:String, minute:String, second:String):
    lunar_time, is_leap_month = calculate_core.core_solar_to_lunar(datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)))
    return lunar_time, is_leap_month

def get_solar_time(year:String, month:String, day:String, hour:String, minute:String, second:String, isLeap:Boolean):
    solar_time = calculate_core.core_lunar_to_solar(datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)), isLeap)
    return solar_time

def get_origin_data(year:String, month:String, day:String, hour:String, minute:String, second:String):
    lunar_time, isLeapMonth = calculate_core.core_solar_to_lunar(datetime(int(year), int(month), int(day), int(hour), int(minute), int(second)))
    lunar_time_year_ganzhi = calculate_core.core_lunar_year_ganzhi(lunar_time)
    lunar_time_month_ganzhi = calculate_core.core_lunar_month_ganzhi(lunar_time)
    lunar_time_day_ganzhi = calculate_core.core_lunar_day_ganzhi(lunar_time)
    lunar_time_time_ganzhi = calculate_core.core_lunar_time_ganzhi(lunar_time)
    solar_time = calculate_core.core_lunar_to_solar(lunar_time)
    current_info = "阴历时间为：%s 年柱:%s 月柱:%s 日柱:%s 时柱:%s"%(lunar_time, lunar_time_year_ganzhi, lunar_time_month_ganzhi, lunar_time_day_ganzhi, lunar_time_time_ganzhi)
    calculate_core.logger.info("阴历时间为：%s 年柱:%s 月柱:%s 日柱:%s 时柱:%s"%(lunar_time, lunar_time_year_ganzhi, lunar_time_month_ganzhi, lunar_time_day_ganzhi, lunar_time_time_ganzhi))
    calculate_core.logger.info("阳历时间为：%s"%(solar_time))
    pre_jieqi_section, next_jieqi_section = calculate_core.core_get_current_jieqi_solar_section(lunar_time)
    calculate_core.logger.info("[%s] [%s]"%(pre_jieqi_section, next_jieqi_section))
    jieqi_section = "[%s] [%s]"%(pre_jieqi_section, next_jieqi_section)
    return current_info, jieqi_section
    
#定义app在8080端口运行
app.run(host='0.0.0.0', port=8080)
