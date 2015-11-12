#!/usr/bin/env python
import time
def changedate(data="2015-11-11 15:40:10"):
    a = data
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

if __name__ == '__main__':
    print changedate()
