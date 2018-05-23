import time, os
from collections import Counter

import matplotlib.pyplot as plt
import pytimber

from boinc_peewee import *

now=time.time()
yesterday=now-48*3600

app={'sixtrack':1,'lhcb':12,'alice':15,'atlas':14,'theory':13,'cms':11}

os.path.isdir('figs') or os.mkdir('figs')

out=[]
plt.figure(figsize=(8,5))
lbl=pytimber.dumpdate(fmt='%Y%m%dT%H%M%S')
for name,appid in sorted(app.items()):
  sent_times=[ r.sent_time for r in Result.select().where(Result.server_state>3,Result.appid==appid)]
  plt.clf()
  plt.hist(sent_times,bins=72,range=(now-72*3600,now))
  pytimber.set_xaxis_date()
  plt.title('%s %s'%(name,lbl))
  figname='figs/sent_%s_%s.png'%(name,lbl)
  plt.ylabel('Sent tasks per hour ')
  print(figname)
  plt.savefig(figname)
  out.append(figname)

outname='figs/sent_%s.pdf'%lbl
os.system('convert %s %s'%(' '.join(out),outname))
print(outname)

