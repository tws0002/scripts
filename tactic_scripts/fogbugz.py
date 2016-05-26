# -*- coding: utf-8 -*-
from fogbugz import FogBugz


fb = FogBugz("https://fb.vir888.com")
fb.logon("ART-Julio", "chicago")

resp = fb.search(q=u'(MCD)動畫製作',cols='ixBug,sTitle,ixPersonAssignedTo')
 

#%%
x = 0
for case in resp.cases.findAll('case'):
    x = x +1
    print "%s: %s %s" % (case.ixbug.string.encode('UTF-8'),case.stitle.string.encode('UTF-8'),case.ixPersonAssignedTo)
print x

