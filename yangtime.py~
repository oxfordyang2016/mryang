# this is used to del with time
'''
ref url:
https://stackoverflow.com/questions/3316882/how-do-i-get-a-string-format-of-the-current-date-time-in-python
https://stackoverflow.com/questions/20573459/getting-the-date-of-7-days-ago-from-current-date-in-python
'''

import datetime as DT



def dayslots(count):
	'''
	example
	deletelog(7)
	['20170818',
     '20170817',
     '20170816',
     '20170815',
     '20170814',
     '20170813',
     '20170812']
	'''

    today = DT.date.today()
    days = []
    for k in range(count):
        yesterday = today - DT.timedelta(days=int(k))
        days.append(yesterday.strftime("%Y%m%d"))
        print(yesterday)
    return days
