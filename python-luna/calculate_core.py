#!/usr/bin/python3
# -*- coding: utf-8 -*-
# create by zhengzhengguo
from datetime import datetime
from sys import argv
from Util.log_module import Logger
from lunar_python import Solar, Lunar
from lunar_python.LunarMonth import LunarMonth

logger = Logger.singleton().logger

def core_solar_to_lunar(solar_date):
    '''
    阳历转阴历的接口
    '''
    #logger.debug(solar_date)
    solar = Solar.fromDate(solar_date)
    #logger.debug("当前时间：%s 阳历时间:%s"%(solar_date, solar))
    lunar = solar.getLunar()
    logger.debug("阴历时间：%s %s"%(lunar, lunar.getMonth()))
    isLeapMonth = LunarMonth.fromYm(lunar.getYear(), lunar.getMonth()).isLeap()
    logger.debug("是否闰月：%d"%isLeapMonth)
    lunar_time = datetime(abs(lunar.getYear()), abs(lunar.getMonth()), abs(lunar.getDay()), solar_date.hour, solar_date.minute, solar_date.second)
    #logger.debug("阴历时间：%s"%(lunar_time))
    return lunar_time, isLeapMonth

def core_lunar_to_solar(lunar_time, is_leap=False):
    '''
    阴历转阳历的接口
    '''
    if is_leap:
        lunar_object = Lunar.fromYmdHms(lunar_time.year, -lunar_time.month, lunar_time.day, lunar_time.hour, lunar_time.minute, lunar_time.second)
    else:
        lunar_object = Lunar.fromYmdHms(lunar_time.year, lunar_time.month, lunar_time.day, lunar_time.hour, lunar_time.minute, lunar_time.second)
    solar = lunar_object.getSolar()
    solar_object = datetime(abs(solar.getYear()), abs(solar.getMonth()), abs(solar.getDay()), lunar_time.hour, lunar_time.minute, lunar_time.second)
    #logger.debug("阴历时间:%s 对应的阳历时间:%s"%(lunar_time, solar_object))
    return solar_object


def core_lunar_year_ganzhi(lunar_time:datetime):
    '''
    获取阴历的年干支，新年以立春节气交接的时刻
    '''
    lunar_object = Lunar.fromYmdHms(lunar_time.year, lunar_time.month, lunar_time.day, lunar_time.hour, lunar_time.minute, lunar_time.second)
    lunar_year_ganzhi = lunar_object.getYearInGanZhiExact()
    #logger.debug("阴历时间 [%s] 的年干支为 [%s]"%(lunar_time, lunar_year_ganzhi))
    return lunar_year_ganzhi

def core_lunar_month_ganzhi(lunar_time:datetime):
    '''
    获取阴历的月干支，新月以节交接的时刻起算
    '''
    lunar_object = Lunar.fromYmdHms(lunar_time.year, lunar_time.month, lunar_time.day, lunar_time.hour, lunar_time.minute, lunar_time.second)
    lunar_month_ganzhi = lunar_object.getMonthInGanZhiExact()
    #logger.debug("阴历时间 [%s] 的月干支为 [%s]"%(lunar_time, lunar_month_ganzhi))
    return lunar_month_ganzhi

def core_lunar_day_ganzhi(lunar_time:datetime):
    '''
    获取阴历的日干支，晚子时日柱算是明天
    '''
    lunar_object = Lunar.fromYmdHms(lunar_time.year, lunar_time.month, lunar_time.day, lunar_time.hour, lunar_time.minute, lunar_time.second)
    lunar_day_ganzhi = lunar_object.getDayInGanZhiExact()
    #logger.debug("阴历时间 [%s] 的日干支为 [%s]"%(lunar_time, lunar_day_ganzhi))
    return lunar_day_ganzhi

def core_lunar_time_ganzhi(lunar_time:datetime):
    '''
    获取阴历的时辰干支
    '''
    lunar_object = Lunar.fromDate(core_lunar_to_solar(lunar_time))
    lunar_time_ganzhi = lunar_object.getEightChar().getTime()
    #logger.debug("阴历时间 [%s] 的时辰干支为 [%s]"%(lunar_time, lunar_time_ganzhi))
    return lunar_time_ganzhi

def core_get_current_jieqi_solar_section(lunar_time:datetime):
    '''
    获取当前的阳历节气时间区间
    '''
    lunar_object = Lunar.fromDate(core_lunar_to_solar(lunar_time))
    #current_jieqi = lunar_object.getCurrentJieQi()
    next_jieqi = lunar_object.getNextJieQi(False)
    pre_jieqi = lunar_object.getPrevJieQi(False)
    pre_jieqi_section = pre_jieqi.getName() + ' ' + pre_jieqi.getSolar().toYmdHms()
    next_jieqi_section = next_jieqi.getName() + ' ' + next_jieqi.getSolar().toYmdHms()

    return pre_jieqi_section, next_jieqi_section


if __name__ == "__main__":
    if len(argv) < 2:
        d = input('请输入阴/阳历以及日期:')
        argv = d.split()
        argv.insert(0,0)
    # 阳历转换为阴历
    if argv[1] == "阳历":
        lunar_time, isLeapMonth = core_solar_to_lunar(datetime(int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]), int(argv[7])))
    elif argv[1] == "阴历":
        lunar_time = datetime(int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]), int(argv[7]))
    else:
        print("python3 xxxx.py 阴历 1948 8 28 1 50 20")
        print("python3 xxxx.py 阳历 1948 8 28 1 50 20")
        exit(1)
    lunar_time_year_ganzhi = core_lunar_year_ganzhi(lunar_time)
    lunar_time_month_ganzhi = core_lunar_month_ganzhi(lunar_time)
    lunar_time_day_ganzhi = core_lunar_day_ganzhi(lunar_time)
    lunar_time_time_ganzhi = core_lunar_time_ganzhi(lunar_time)
    solar_time = core_lunar_to_solar(lunar_time)
    print("阴历时间为：%s 年柱:%s 月柱:%s 日柱:%s 时柱:%s"%(lunar_time, lunar_time_year_ganzhi, lunar_time_month_ganzhi, lunar_time_day_ganzhi, lunar_time_time_ganzhi))
    logger.info("阴历时间为：%s 年柱:%s 月柱:%s 日柱:%s 时柱:%s"%(lunar_time, lunar_time_year_ganzhi, lunar_time_month_ganzhi, lunar_time_day_ganzhi, lunar_time_time_ganzhi))
    logger.info("阳历时间为：%s"%(solar_time))
    pre_jieqi_section, next_jieqi_section = core_get_current_jieqi_solar_section(lunar_time)
    logger.info("[%s] [%s]"%(pre_jieqi_section, next_jieqi_section))