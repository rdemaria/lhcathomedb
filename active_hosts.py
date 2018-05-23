import time,os
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

returned=array([ r.hostid for r in Result.select().where(Result.server_state==5,Result.appid==1)])
returned=Counter(returned)

sentn=array([ float(sent[i])/hosts[i].p_ncpus for i in hosts])
sentnn=array([ float(sent[i]) for i in hosts])

print(time.asctime())

print("Active hosts in last 24h: %d"%(len(hosts)))
print("Hosts with pending results: %d"%(len(sent)))
print("Active hosts with no pending tasks: %d"%sum(sentn==0))
print("Active Hosts with pending tasks/Ncores<1: %d"%sum((sentn>0) & (sentn<1)))
print("Active Hosts with pending tasks/Ncores>3: %d"%sum(sentn>3))

plt.hist(sentn,bins=int(sentn.max()))

os.path.isdir('figs') or os.mkdir('figs')
figname='figs/pending_%s.png'%time.strftime('%Y%m%dT%H%M%S')
plt.savefig(figname)


