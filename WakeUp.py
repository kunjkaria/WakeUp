23# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 04:29:47 2012

@author: kunj
"""

import os
import time
timer=raw_input("Alarm should ring at: ")
hour=timer[:2]
minute=timer[2:]
def run():
    t=time.ctime()
    currenttime_hour=t[11:13]
    currenttime_minute=t[14:16]
    if currenttime_hour==hour and currenttime_minute==minute:
        os.system('banshee --play &')
        time.sleep(4)
        os.system('banshee --play')
        raw_input('press spacebar key')
    else:
        time.sleep(60)
        run()
def main():
    run()
if __name__== '__main__':
    main()