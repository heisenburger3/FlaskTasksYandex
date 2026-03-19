from data.user import User
from data import db_session

db_session.global_init("../db/mars_explorer.db")
db_sess = db_session.create_session()

captain = User()
captain.surname = "Scott"
captain.name = "Ridley"
captain.age = 21
captain.position = "captain"
captain.speciality = "research engineer"
captain.address = "module_1"
captain.email = "scott_chief@mars.org"
db_sess.add(captain)

big_boss = User()
big_boss.surname = "Unknown"
big_boss.name = "John"
big_boss.age = 29
big_boss.position = "boss"
big_boss.speciality = "head of the company"
big_boss.address = "module_1"
big_boss.email = "themanwhosoldtheworld@mars.org"
db_sess.add(big_boss)

engineer = User()
engineer.surname = "Ridley"
engineer.name = "Scott"
engineer.age = 22
engineer.position = "engineer"
engineer.speciality = "research engineer"
engineer.address = "module_1"
engineer.email = "ridley@mars.org"
db_sess.add(engineer)

doctor = User()
doctor.surname = "Pork"
doctor.name = "John"
doctor.age = 23
doctor.position = "doctor"
doctor.speciality = "doctor"
doctor.address = "module_1"
doctor.email = "doctor@mars.org"
db_sess.add(doctor)

db_sess.commit()
