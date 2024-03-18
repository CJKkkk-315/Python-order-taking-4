
# -*- coding: utf-8 -*-

from lunar_python import Lunar, Solar
from lunar_python.util import HolidayUtil
from lunar_python import LunarYear
from datetime import datetime
from Util.log_module import Logger



def get_Spring_begins(year):
    '''
    获取当年的立春时间
    '''
    Yearlunar = LunarYear.fromYear(year)
    jieQiJulianDays = Yearlunar.getJieQiJulianDays()
    lichun_Sun = Solar.fromJulianDay(jieQiJulianDays[4]).toYmdHms() #国历立春
    lichun_Lunar = Solar.fromJulianDay(jieQiJulianDays[4]).getLunar() #农历立春
    time = lichun_Sun.split( )[1]
    return lichun_Sun, lichun_Lunar, time

def get_Year_TianGanDiZhi(year):
    '''
    获取当年的立春时间, 天干地支
    '''
    lichun_Sun, lichun_Lunar, time = get_Spring_begins(year)
    tian_gan_di_zhi = LunarYear.fromYear(year).getGanZhi()
    print("%s年立春 国历时间:%s 农历时间:%s 当天时间:%s"%(year, lichun_Sun, lichun_Lunar, time))
    print("%s年的天干地支：%s"%(year, tian_gan_di_zhi))
    return lichun_Sun, lichun_Lunar, time, tian_gan_di_zhi



if __name__ == '__main__':

    Year = 1996
    Month = 12
    Day = 7
    hour = 1
    minute = 50
    second = 12
    #获取年柱
    lichun_Sun, lichun_Lunar, time, tian_gan_di_zhi = get_Year_TianGanDiZhi(Year)
    #获取月柱
    mother_column = Lunar.fromYmdHms(2022, 2, 17, 1, 50, 12)
    print(mother_column.getYearInGanZhiByLiChun())
    print("2022年2月27日%s"%(mother_column.getMonthInGanZhiExact()))