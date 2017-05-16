from pymongo import MongoClient
import random
import string
import hashlib
import utils

#connect to mongo
connection = MongoClient("127.0.0.1")
db = connection['database']
students = db['students']
teachers = db['teachers']
classes = db['classes']

#get secret data
secrets = utils.getSecretData()

#hashes text, used for sensitive data
def hash(text):
    return hashlib.sha256(text).hexdigest()

#generate a random alphanumeric verification link / id
def getVerificationLink():
    link = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    #check if any other users have this id
    check = db.students.count(
        {
            'verificationID': link
        }
    )
    #if the id isn't unique, recursively run and get another id
    if check:
        link = getVerificationLink()
        return link
    else:
        return link

#finds account from email which is psuedo id since it's unique
#returns false if failed, or if more than 1 acc with that email
def getStudent(email):
    count = db.students.count(
        {
            'email': email
        }
    )
    if count != 1:
        return False
    else:
        return db.students.find(
            {
                'email': email
            }
        )

def getTeacher(email):
    count = db.teachers.count(
        {
            'email': email
        }
    )
    if count != 1:
        return False
    else:
        return db.teachers.find(
            {
                'email': email
            }
        )
    
def createClass( teacher, className, groupLimit ):
    db.classes.insert_one(
        {
            'teacher': teacher,
            'className': className,
            'groupLimit': groupLimit,
            'students': [],
            'groups': [],
            'classCode': generateClassCode()
        })
