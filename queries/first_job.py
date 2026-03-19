from data.jobs import Jobs
from data import db_session
import datetime

db_session.global_init("../db/mars_explorer.db")
db_sess = db_session.create_session()

job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = '2, 3'
job.start_date = datetime.datetime.now()
job.is_finished = False
db_sess.add(job)
db_sess.commit()