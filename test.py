import random
import time
from datetime import datetime

'''
class RanDate():
    def strTimeProp(self, start, end, prop, frmt):
        stime = time.mktime(time.strptime(start, frmt))
        etime = time.mktime(time.strptime(end, frmt))
        ptime = stime + prop * (etime - stime)
        return int(ptime)

    def randomDate(self, frmt='%Y-%m-%d %H:%M:%S'):    
        start = '1950-01-01 00:00:00'
        end = '2000-12-31 23:59:59'
        return time.strftime(frmt, 
            time.localtime(self.strTimeProp(start, end, random.random(), frmt)))

print(RanDate().randomDate())
'''

# def strTimeProp(start, end, prop, frmt):
#     stime = time.mktime(time.strptime(start, frmt))
#     etime = time.mktime(time.strptime(end, frmt))
#     ptime = stime + prop * (etime - stime)
#     return int(ptime)

# def randomDate(frmt='%Y-%m-%d %H:%M:%S'):    
#     start = '1950-01-01 00:00:00'
#     end = '2000-12-31 23:59:59'
#     return time.strftime(frmt, 
#         time.localtime(strTimeProp(start, end, random.random(), frmt)))

# randomDate = randomDate()
# # print(randomDate())

# qs = datetime.strptime(randomDate, "%Y-%m-%d %H:%M:%S")
# print(type(qs))

def fun(a, *args, **kwargs):
    print(f'a={a}')
    for arg in args:
        print(f'Optional argument: {arg}')

    for k, v in kwargs.items():
        print(f'Optional kwargs argument key: {k} value {v}')

# print("")
# args = [1, 2, 3, 4]
# fun(*args)

# print("")
# kwargs = {'k1':10, 'k2':11}
# fun(1, **kwargs)

print("")
args = [1, 2, 3, 4]
kwargs = {'k1':10, 'k2':11}
fun(1, *args, **kwargs)