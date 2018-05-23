from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pymysql
pymysql.install_as_MySQLdb()


Base = automap_base()

engine =create_engine("mysql://sixtadm:B01nclhc.@dbod-sixtrack.cern.ch:5513/sixt_production")

Base.prepare(engine, reflect=True)


Result=Base.classes.result
Workunit=Base.classes.workunit


session = Session(engine)

session.query(Result).limit(1000).count()


