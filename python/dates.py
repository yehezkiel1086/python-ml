#!/bin/python3

import datetime

now = datetime.datetime.now()
independence = datetime.datetime(1776, 7, 4)

print(now)
print(now.year)
print(now.strftime("%A"))

print(f"American Independence day: {independence.date()}")