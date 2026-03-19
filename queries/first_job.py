from data.jobs import Jobs
from data import db_session

db_session.global_init("../db/mars_explorer.db")
db_sess = db_session.create_session()

job_1 = Jobs()
job_1.team_leader = 1
job_1.job = "Deployment of residential modules 1 and 2"
job_1.work_size = 15
job_1.collaborators = '2, 3'
job_1.is_finished = False
db_sess.add(job_1)
job_2 = Jobs()
job_2.team_leader = 2
job_2.job = "Distributes money for research"
job_2.work_size = 10
job_2.collaborators = '1, 3'
job_2.is_finished = False
db_sess.add(job_2)
job_3 = Jobs()
job_3.team_leader = 3
job_3.job = "Helps to collaborators 1 and 2"
job_3.work_size = 25
job_3.collaborators = '1, 2'
job_3.is_finished = False
db_sess.add(job_3)
job_4 = Jobs()
job_4.team_leader = 4
job_4.job = "Preparing medicaments for the colonists"
job_4.work_size = 5
job_4.collaborators = '2'
job_4.is_finished = False
db_sess.add(job_4)
db_sess.commit()
