import string
# t = int(input("Please enter number"))
# day = 86400
# hour = 3600
# minute = 60
period = (0, 224930, 466289, 950400, 1209600, 1900800, 8639999, 22493, 7948799)
for t in period:
    if 0 <= t < 8640000:
        day = str(t // 86400)
        hours = str(t % 86400 // 3600)
        minute = str(t % 86400 % 3600 // 60)
        seconds = str(t % 86400 % 3600 % 60)
        if int(day) <= 1:
            print(day.zfill(1), "day", ",", hours.zfill(2), ":", minute.zfill(2), ":", seconds.zfill(2))
        else:
            print(day, "days", ",", hours.zfill(2), ":", minute.zfill(2), ":", seconds.zfill(2))

for t in period:
    if 0<= t < 8640000:
        day, hours_first = divmod(t, 86400)
        day = str(day)
        hours, minute_first = divmod(hours_first, 3600)
        hours = str(hours)
        minute, seconds = divmod(minute_first, 60)
        minute = str(minute)
        seconds = str(seconds)
        if int(day) <= 1:
            print(day.zfill(1), "day", ",", hours.zfill(2), ":", minute.zfill(2), ":", seconds.zfill(2))
        else:
            print(day, "days", ",", hours.zfill(2), ":", minute.zfill(2), ":", seconds.zfill(2))


# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59