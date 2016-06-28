# -*- coding: utf-8 -*-
from pyVim.connect import SmartConnect
import time
import requests
import subprocess

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

#hosts[0].vm[0].ShutdownGuest()
#hosts[0].Shutdown(1)


#%%
#dir(hosts[0].vm[0].runtime.powerState)
#hosts[0].vm[0].runtime.powerState

#%%
#Shut down all the guest vms
for host in hosts:
    host.vm[0].ShutdownGuest()

time.sleep(30)

for host in hosts:    
    while host.vm[0].runtime.powerState == "poweredOn":
        host.vm[0].ShutdownGuest()
        time.sleep(30)

#%%    
def shutDownPicasso():
    for host in hosts:
        host.Shutdown(1)    
        time.sleep(5)

shutDownPicasso()
time.sleep(30)

for host in hosts:
    while host.runtime.powerState == "poweredOn":
        host.Shutdown(1)
        time.sleep(30)
            
#%%
