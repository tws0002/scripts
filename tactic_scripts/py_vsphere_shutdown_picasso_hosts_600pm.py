# -*- coding: utf-8 -*-
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

def shutDownPicasso():
    for host in hosts:
        host.Shutdown(1)    
        time.sleep(5)


hosts[0].vm[0].name        
#%%
#Shut down all the guest vms

try:
    for host in hosts:
        if host.vm[0].runtime.powerState == "poweredOff":
            print host.vm[0].name + " us Powered Off"
            pass
        else:
            host.vm[0].ShutdownGuest()
            print "Shutting Down " + host.vm[0].name
except:
    print "All ok"
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
    while host.runtime.powerState == "poweredOn":
        print "Shutting Down ESXI Host " + host.name + " again."
        host.Shutdown(1)
        time.sleep(30)



           

