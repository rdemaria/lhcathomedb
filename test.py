from boinc_peewee import *



outliers=Result.select().where(Result.runtime_outlier!=0).limit(1000)
outliers.count()

for res in Result.select().where(Result.runtime_outlier!=0).limit(10):
    print res.name

res=Result.select().where(Result.runtime_outlier!=0).get()
work=Workunit.get(Workunit.id==res.workunitid)



App.select().get()



Result.select().where(Result.cpu_time<100).count()


Result.select().where(Result.appid==1).order_by(Result.create_time.desc()).first()


Workunit.select().order_by(


Result.select().where(Result.server_state==4).group_by(Result.appid).count()

Result.select().where(Result.server_state==4).group_by(Result.appid).count()

for i in range(100):
  count=Result.select().where(Result.server_state==4,Result.appid==1).count()
  print time.asctime(), count
  time.sleep(5)


list(Result.select(Result.sent_time).where(Result.appid==1))

aa=[ res.sent_time for res in Result.select().where(Result.appid==1,Result.server_state==4)]



