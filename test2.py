import time
from collections import Counter

from numpy import *

from boinc_peewee import *
import pytimber.dataquery

import matplotlib.pyplot as plt
import pytimber

now=time.time()
yesterday=now-24*3600

hosts=list(Host.select().where(Host.rpc_time>yesterday))
hosts=dict( (p.id,p) for p in hosts)
hosts_ip=dict( (p.external_ip_addr,p) for p in hosts.values())

sent=[ r.hostid for r in Result.select().where(Result.server_state==4,Result.appid==1)]
sent=Counter(sent)

sentn=array([ sent.get(i,0) for i in hosts])
print(sum(sentn==0))

sentn=array([ float(sent[0])/hosts[i].p_ncpus for i in hosts])
print(sum(sentn<1))
hist(sentn,bins=sentn.max())




sent=array([ r.sent_time for r in Result.select().where(Result.server_state==4,Result.appid==1)])
pytimber.dataquery.set_

returned=array([ r.sent_time for r in Result.select().where(Result.server_state==5,Result.appid==1)])


#sixtrack 1
app={'sixtrack':1,'lhcb':12,'alice':15,'atlas':14,'theory':13,'cms':11}

for name,appid in app.items():
  sent_times=[ r.sent_time for r in Result.select().where(Result.server_state>3,Result.appid==appid)]
  clf()
  hist(sent_times,bins=72,range=(now-72*3600,now))
  pytimber.dataquery.set_xaxis_date()
  title(name)
  savefig('sent_%s.png'%name)

#lhcb 12
sent_times=[ r.sent_time for r in Result.select().where(Result.server_state>3,Result.appid==12)]
clf()
hist(sent_times,bins=72,range=(now-72*3600,now))
pytimber.dataquery.set_xaxis_date()
title('lhcb')
savefig('sent_lhcb.png')


