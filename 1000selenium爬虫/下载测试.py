from datetime import datetime, timedelta

# 获取今天的日期
today = datetime.now() + timedelta(days=1)

# 获取7天后的日期
seven_days_later = today + timedelta(days=7)

# 格式化日期为'XXXX-XX-XX'的形式
today_formatted = today.strftime('%Y-%m-%d')
seven_days_later_formatted = seven_days_later.strftime('%Y-%m-%d')

print("今天的日期:", today_formatted)
print("7天后的日期:", seven_days_later_formatted)
