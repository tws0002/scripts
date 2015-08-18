import csv
from dateutil.parser import parse
from datetime import date, time
import datetime
f = "c:\\python27\pacer.csv"

col = ['Z_PK', 'Z_ENT', 'Z_OPT', 'ZACTIVITYTYPE', 'ZENDTIME', 'ZFLOORS', 'ZPAYLOADINT32', 'ZRECORDEDFORDATE', 'ZSTARTTIME', 'ZSTEPS', 'ZSYNCSTATUS', 'ZUSER', 'ZCALORIES', 'ZDISTANCEINMETERS', 'ZMET', 'ZPAYLOADFLOAT', 'ZPAYLOAD', 'ZPAYLOADSTRING']
print col[9]
st = []
test = []
with open(f, 'rb') as csvfile:
    next(csvfile)    
    reader = csv.reader(csvfile)
    for row in reader:
        #print datetime.utcfromtimestamp(float(row[7])) 
        #print row[9] #steps
        z_pk = row[0]
        try:
            print (float(row[13]) / float(row[9]))
        except:
            pass

print z_pk
|

#calories / step = 0.045
#distance / step = 0.62
#time / step = 

#average

sd = datetime.
datetime.today()
date.today()

d = date(2015, 8, 1)
t = time(0, 0)
print str(d)
dt = datetime.combine(d, t)
print dt
print datetime.utcfromtimestamp(float(dt))
date1, time1 = '1970-01-01', '12:23:33'
date2, time2 = '2012-09-08', '12:23:33'

dt1 = datetime.datetime.strptime(str(d) + ' ' + str(t), "%Y-%m-%d %H:%M:%S")

print dt1.total_seconds()
test = []
Z_PK = z_pk
Z_STARTTIME = str(random.randrange(9,855)) + "00"
ZENDTIME = int(Z_STARTTIME) + 900
for day in range(1,32):
    minute = 0
    hour = 0
    while hour < 24:
        minute = 0
        while minute < 60:
            Z_PK = Z_PK + 1
            #print str(day) + " " + str(hour) + ":" + str(minute)
            #test.append(str(day) + " " + str(hour) + ":" + str(minute))
            d = date(2015, 8, day)
            t = time(hour, minute)
            dt = datetime.combine(d, t)
            
            minute = minute + 5
            final = [Z_PK, 15, 1, 0, ZENDTIME, 0, NULL, ]
        hour = hour + 1

        

print len(test)
import random
random.randrange(0,20)