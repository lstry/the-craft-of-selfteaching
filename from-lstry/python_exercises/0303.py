#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Try to print the day, month, year in the form “Today is 2/2/2016”.
import time
currentTime = time.strftime('%d/%m/%Y',time.localtime(time.time()))
print("Today is", currentTime)