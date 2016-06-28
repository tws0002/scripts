# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:06 2015

@author: julio
This script should be run after 9am everyday, it will shutdown machines if its on weekends or holidays
"""


from pyVim.connect import SmartConnect, Disconnect
import datetime
import subprocess
import time

import requests
requests.packages.urllib3.disable_warnings()

import ssl
ssl._create_unverified_https_context = ssl._create_unverified_context
ssl._create_default_https_context = ssl._create_unverified_https_context

import sys
sys.path.append("//Art-1405260002/d/assets/client")
#%%
si = SmartConnect(host="192.168.163.56", user="julio@vsphere.local", pwd="12345678", port=int(443))

content = si.RetrieveContent()
datacenters = content.rootFolder.childEntity
picasso = datacenters[3].hostFolder.childEntity[0]
hosts = picasso.host
#%%
today = datetime.date.today()

holidays = []
holidays.append(datetime.date(2016,2,29))
holidays.append(datetime.date(2016,4,4))
holidays.append(datetime.date(2016,4,5))
holidays.append(datetime.date(2016,6,10))
holidays.append(datetime.date(2016,9,16))
holidays.append(datetime.date(2016,10,9))

# shutdown if its during weekends
shutdown = False
if today.weekday() in [5,6]:
    shutdown = True

# shutdown if its during holidays
if today in holidays:
    shutdown = True
#%%
def shutDownPicasso():
    for host in hosts:
        host.Shutdown(1)    
        time.sleep(5)


if shutdown == True:
    still_on = ['first']
    while len(still_on) > 0:
        still_on = []
        time.sleep(30)
        for host in hosts:
            ping = subprocess.Popen(["ping", "-n", "1",host.name], stdout=subprocess.PIPE)    
            for line in ping.stdout.readlines():
                if "Reply from" in line:
                    if "Destination host unreachable" in line:
                        pass
                    else:
                        print host.name + "is still on"
                        still_on.append(host.name)
        
        for host in hosts:
            if host.name in still_on:
                host.Shutdown(1)
                time.sleep(5)