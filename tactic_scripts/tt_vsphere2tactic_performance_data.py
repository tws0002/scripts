# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:55:06 2015

@author: julio
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:54:55 2015

@author: julio
"""

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import datetime
from dateutil import parser

import requests
requests.packages.urllib3.disable_warnings()

import ssl
ssl._create_unverified_https_context = ssl._create_unverified_context
ssl._create_default_https_context = ssl._create_unverified_https_context

import time
import sys
import socket
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub

server = TacticServerStub.get()
tactic_server_ip = socket.gethostbyname("vg.com")
server.set_server(tactic_server_ip)
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

si = SmartConnect(host="192.168.200.56", user="julio@vsphere.local", pwd="12345678", port=int(443))

content = si.RetrieveContent()
datacenters = content.rootFolder.childEntity

#create metricID object
perfManager = content.perfManager
perf_dict = {} 
perfList = content.perfManager.perfCounter #this is a list of all counters(benchmarks) from vcenter
for counter in perfList: #build the vcenter counters for the objects
    counter_full = "{}.{}.{}".format(counter.groupInfo.key,counter.nameInfo.key,counter.rollupType)
    perf_dict[counter_full] = counter.key
counter_name = 'cpu.usage.average'
counterId = perf_dict[counter_name]
metricId = vim.PerformanceManager.MetricId(counterId=counterId, instance="*")
#startTime = datetime.datetime.now()-datetime.timedelta(hours=168) # past week
#endTime = datetime.datetime.now()
exp = "@MAX(simpleslot/renderfarm_performance.time)"
db_max_date = server.eval(exp)
db_max_date = parser.parse(db_max_date)

for datacenter in datacenters:
    hostFolder = datacenter.hostFolder
    cluster = hostFolder.childEntity
    if "Cluster" in cluster[0].name:
        query = vim.PerformanceManager.QuerySpec(intervalId=7200, maxSample=1, entity=cluster[0], metricId=[metricId], format="csv")
        perfResults = perfManager.QueryPerf(querySpec=[query])
        dates = [x for x in perfResults[0].sampleInfoCSV.split(",") if x != "7200"]
        values = perfResults[0].value[0].value.split(",")        
        for x in range(len(dates)):
            date = parser.parse(dates[x]).replace(tzinfo=None)
            if date > db_max_date:
                data = {'name': cluster[0].name, 'time': dates[x], 'usage': values[x]}
                st = "simpleslot/renderfarm_performance"
                server.insert(st, data)


