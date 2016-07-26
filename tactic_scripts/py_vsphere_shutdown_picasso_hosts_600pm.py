# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:06 2015

@author: julio
This script should be run after 9am everyday, it will shutdown machines if its on weekends or holidays
"""


from pyVim.connect import SmartConnect
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
#Shut down all the guest vms
try:
    for host in hosts:
        if len(host.vm) != 0:
            if host.vm[0].runtime.powerState == "poweredOff":
                print host.vm[0].name + " us Powered Off"
                pass
            else:
                print "Shutting Down " + host.vm[0].name
                host.vm[0].ShutdownGuest()
except:
    e = sys.exc_info()[0]
    print e
time.sleep(30)
try:
    for host in hosts:
        while host.vm[0].runtime.powerState == "poweredOn":
            host.vm[0].ShutdownGuest()
            print "Trying to Shut Down " + host.vm[0].name + " again."
            time.sleep(30)
except:
    print "All ok"
#%%


for host in hosts:
    if host.runtime.powerState == "poweredOff":
        print "ESXI Host " + host.name + " is powered off."
        pass
    else:
        print "Shutting Down ESXI Host " + host.name
        host.Shutdown(1)

time.sleep(60)
#check again
for host in hosts:
    hosts[0].name
    
    while host.runtime.powerState == "poweredOn":
        print "Shutting Down ESXI Host " + host.name + " again."
        host.Shutdown(1)
        time.sleep(30)





