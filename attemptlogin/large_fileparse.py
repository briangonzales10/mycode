#!/usr/bin/env python3

loginfail = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
                loginfail += 1
print("Failed login attempts:", loginfail)